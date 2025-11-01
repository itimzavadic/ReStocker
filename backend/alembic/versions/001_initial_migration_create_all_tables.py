"""Initial migration: create all tables

Revision ID: 001
Revises: 
Create Date: 2024-01-15 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Создание ENUM типов (сначала создаем типы, потом используем их в таблицах)
    op.execute("CREATE TYPE userrole AS ENUM ('менеджер', 'владелец')")
    op.execute("CREATE TYPE subscriptiontype AS ENUM ('бесплатная', 'премиум', 'пробная')")
    op.execute("CREATE TYPE triggertype AS ENUM ('товар', 'категория', 'ключевое_слово')")
    op.execute("CREATE TYPE actiontype AS ENUM ('списание', 'добавление')")
    op.execute("CREATE TYPE sourcetype AS ENUM ('ручное', 'CRM', 'кнопка')")
    
    # Создание таблицы users
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('role', postgresql.ENUM('менеджер', 'владелец', name='userrole'), nullable=True),
        sa.Column('subscription', postgresql.ENUM('бесплатная', 'премиум', 'пробная', name='subscriptiontype'), nullable=True),
        sa.Column('telegram_id', sa.BigInteger(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_telegram_id'), 'users', ['telegram_id'], unique=True)
    
    # Создание таблицы products
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('unit', sa.String(), nullable=False),
        sa.Column('quantity', sa.Float(), nullable=True),
        sa.Column('threshold', sa.Float(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    op.create_index(op.f('ix_products_category'), 'products', ['category'], unique=False)
    
    # Создание таблицы rules
    op.create_table(
        'rules',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('trigger_type', postgresql.ENUM('товар', 'категория', 'ключевое_слово', name='triggertype'), nullable=False),
        sa.Column('trigger_value', sa.String(), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rules_id'), 'rules', ['id'], unique=False)
    
    # Создание таблицы rule_items
    op.create_table(
        'rule_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('rule_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.ForeignKeyConstraint(['rule_id'], ['rules.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rule_items_id'), 'rule_items', ['id'], unique=False)
    
    # Создание таблицы manual_buttons
    op.create_table(
        'manual_buttons',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_manual_buttons_id'), 'manual_buttons', ['id'], unique=False)
    
    # Создание таблицы manual_button_items
    op.create_table(
        'manual_button_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('button_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(['button_id'], ['manual_buttons.id'], ),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_manual_button_items_id'), 'manual_button_items', ['id'], unique=False)
    
    # Создание таблицы sales_logs
    op.create_table(
        'sales_logs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('datetime', sa.DateTime(), nullable=True),
        sa.Column('action', postgresql.ENUM('списание', 'добавление', name='actiontype'), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Float(), nullable=False),
        sa.Column('source', postgresql.ENUM('ручное', 'CRM', 'кнопка', name='sourcetype'), nullable=False),
        sa.Column('source_details', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sales_logs_id'), 'sales_logs', ['id'], unique=False)
    op.create_index(op.f('ix_sales_logs_datetime'), 'sales_logs', ['datetime'], unique=False)


def downgrade() -> None:
    # Удаление таблиц в обратном порядке
    op.drop_index(op.f('ix_sales_logs_datetime'), table_name='sales_logs')
    op.drop_index(op.f('ix_sales_logs_id'), table_name='sales_logs')
    op.drop_table('sales_logs')
    
    op.drop_index(op.f('ix_manual_button_items_id'), table_name='manual_button_items')
    op.drop_table('manual_button_items')
    
    op.drop_index(op.f('ix_manual_buttons_id'), table_name='manual_buttons')
    op.drop_table('manual_buttons')
    
    op.drop_index(op.f('ix_rule_items_id'), table_name='rule_items')
    op.drop_table('rule_items')
    
    op.drop_index(op.f('ix_rules_id'), table_name='rules')
    op.drop_table('rules')
    
    op.drop_index(op.f('ix_products_category'), table_name='products')
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    
    op.drop_index(op.f('ix_users_telegram_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    
    # Удаление ENUM типов (после удаления всех таблиц, которые их используют)
    op.execute("DROP TYPE IF EXISTS sourcetype CASCADE")
    op.execute("DROP TYPE IF EXISTS actiontype CASCADE")
    op.execute("DROP TYPE IF EXISTS triggertype CASCADE")
    op.execute("DROP TYPE IF EXISTS subscriptiontype CASCADE")
    op.execute("DROP TYPE IF EXISTS userrole CASCADE")


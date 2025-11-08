# Скрипт для автоматического перезапуска туннелей
# Запускает оба туннеля и перезапускает их при закрытии

Write-Host "Запуск туннелей для ReStocker..." -ForegroundColor Green

# Функция для запуска туннеля
function Start-Tunnel {
    param(
        [string]$Port,
        [string]$Name
    )
    
    Write-Host "`nЗапуск $Name туннеля (порт $Port)..." -ForegroundColor Yellow
    
    while ($true) {
        try {
            $process = Start-Process -FilePath "ssh" -ArgumentList "-R", "80:localhost:$Port", "nokey@localhost.run" -NoNewWindow -PassThru -RedirectStandardOutput "tunnel-$Name-output.txt" -RedirectStandardError "tunnel-$Name-error.txt"
            
            Write-Host "Туннель $Name запущен (PID: $($process.Id))" -ForegroundColor Green
            Write-Host "Проверьте файл tunnel-$Name-output.txt для получения URL" -ForegroundColor Cyan
            
            # Ждем завершения процесса
            $process.WaitForExit()
            
            Write-Host "Туннель $Name закрыт, перезапускаю через 5 секунд..." -ForegroundColor Red
            Start-Sleep -Seconds 5
        }
        catch {
            Write-Host "Ошибка при запуске туннеля $Name : $_" -ForegroundColor Red
            Start-Sleep -Seconds 10
        }
    }
}

# Запускаем туннели в фоне через отдельные окна PowerShell
Write-Host "`nЗапуск backend туннеля в новом окне..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\..'; ssh -R 80:localhost:8000 nokey@localhost.run"

Start-Sleep -Seconds 2

Write-Host "Запуск frontend туннеля в новом окне..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\..'; ssh -R 80:localhost:3000 nokey@localhost.run"

Write-Host "`nТуннели запущены в отдельных окнах PowerShell" -ForegroundColor Green
Write-Host "Закройте это окно, туннели продолжат работать" -ForegroundColor Yellow


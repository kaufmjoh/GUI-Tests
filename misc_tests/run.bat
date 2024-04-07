@echo off
setlocal

set "psScript=%~dp0get_file.ps1"

:: Check if PowerShell is available
where powershell >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: PowerShell is not installed or not in the system PATH.
    exit /b 1
)

:: Execute the PowerShell script and capture the output
for /f "delims=" %%A in ('powershell -ExecutionPolicy Bypass -File "%psScript%"') do set "selectedFile=%%A"

:: Print the selected file name
echo Selected file: %selectedFile%

pause

endlocal

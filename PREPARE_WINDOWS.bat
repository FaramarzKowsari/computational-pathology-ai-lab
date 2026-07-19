@echo off
setlocal
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python was not found. Install Python 3.11 or newer and try again.
  pause
  exit /b 1
)
python scripts\migrate_legacy.py
python scripts\create_checksums.py
echo.
echo Preparation complete. Review changes in GitHub Desktop before committing.
pause

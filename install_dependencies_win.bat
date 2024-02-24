@echo off
echo Checking for Python installation...
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed.
    echo Please install Python from https://www.python.org/downloads/ and ensure it's added to the PATH.
    goto :end
)

echo Checking for pip installation...
py -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo pip is not installed.
    echo Please ensure Python is properly installed with pip included.
    goto :end
)
echo Installing necessary modules...
pip install googletrans==4.0.0-rc1
pip install discord.py
:end
echo Installation completed.
pause
@echo off
echo ============================================================
echo  FP Sensor Lab - EXE Builder
echo  This will take 5-10 minutes. Do not close this window.
echo ============================================================
echo.

cd /d "%~dp0.."

echo [1/3] Installing build tools...
pip install pyinstaller --quiet

echo [2/3] Building standalone EXE...
python -m PyInstaller --noconfirm --clean ^
  --name FPSensorLab ^
  --onedir ^
  --collect-all streamlit ^
  --collect-all plotly ^
  --copy-metadata streamlit ^
  --copy-metadata plotly ^
  --copy-metadata numpy ^
  --copy-metadata pandas ^
  --copy-metadata scipy ^
  --add-data "app.py;." ^
  --add-data "core;core" ^
  --add-data "views;views" ^
  --add-data "assets;assets" ^
  --add-data ".streamlit;.streamlit" ^
  packaging\launcher.py

echo.
echo [3/3] Done!
echo.
echo Your EXE is in:  dist\FPSensorLab\FPSensorLab.exe
echo.
echo Zip the entire  dist\FPSensorLab\  folder and share it.
echo Teammates just unzip and double-click FPSensorLab.exe
echo No Python needed on their computers.
echo.
pause

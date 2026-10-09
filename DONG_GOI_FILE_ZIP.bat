@echo off
chcp 65001 >nul
title Đóng Gói Bộ Cài Đặt Sạch Sẽ Ra File ZIP
color 0D
cls

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python dong_goi_zip.py
echo.
pause

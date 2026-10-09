@echo off
chcp 65001 >nul
title Kiểm Tra Kết Nối Hệ Thống Blogger Auto Poster
color 0E
cls

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python kiem_tra_ket_noi.py
echo.
pause

@echo off
chcp 65001 >nul
title Blogger Auto Poster - Chạy Đăng Bài
color 0A
cls

echo ==============================================================================
echo    🚀 KHỞI ĐỘNG CỖ MÁY VIẾT BÀI & ĐĂNG LÊN BLOGGER TỰ ĐỘNG
echo ==============================================================================
echo.

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

set POSTS_COUNT=1
python main.py

echo.
echo ==============================================================================
echo Đã hoàn tất tiến trình!
echo ==============================================================================
pause

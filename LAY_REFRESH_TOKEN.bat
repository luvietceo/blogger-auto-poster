@echo off
chcp 65001 >nul
title Lấy Google Refresh Token Cho Blogger API
color 0B
cls

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python get_refresh_token.py

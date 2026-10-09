@echo off
chcp 65001 >nul
title Cài Đặt Tự Động Blogger Gemini AI Cloud Poster - LuViet
color 0B
cls

echo ==============================================================================
echo    ☁️ BỘ CÀI ĐẶT TỰ ĐỘNG - BLOGGER GEMINI AI CLOUD AUTO-POSTER ☁️
echo             Hệ Thống Tự Động Hóa Viết Bài & Đăng Lên Blogger 24/7
echo ==============================================================================
echo.

:: 1. KIỂM TRA PYTHON TRÊN MÁY TÍNH
echo [1/4] Đang kiểm tra môi trường Python trên máy tính của bạn...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    py --version >nul 2>&1
    if %errorlevel% neq 0 (
        color 0C
        echo.
        echo ==============================================================================
        echo ❌ CHƯA TÌM THẤY PYTHON TRÊN MÁY TÍNH!
        echo ==============================================================================
        echo Ứng dụng cần môi trường Python 3.10 trở lên để hoạt động.
        echo.
        echo ⚠️ LƯU Ý CỰC KỲ QUAN TRỌNG KHI CÀI ĐẶT:
        echo    Ở màn hình cài đặt đầu tiên của Python, bạn BẮT BUỘC PHẢI TÍCH CHỌN:
        echo    [v] "Add python.exe to PATH" (hoặc "Add Python to environment variables")
        echo ==============================================================================
        echo.
        set /p OPEN_PY="Bạn có muốn mở trang tải Python chính thức ngay bây giờ? (Y/N): "
        if /i "%OPEN_PY%"=="Y" (
            start https://www.python.org/downloads/
        )
        echo.
        echo Sau khi cài đặt xong Python, vui lòng bấm mở lại file "CAI_DAT.bat" này!
        echo.
        pause
        exit /b 1
    )
)

for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PY_VER=%%i
echo     -> Đã phát hiện: %PY_VER% (Hợp lệ)
echo.

:: 2. TẠO MÔI TRƯỜNG ẢO VENV (NẾU CHƯA CÓ)
echo [2/4] Kiểm tra môi trường ảo độc lập (Virtual Environment)...
if not exist "venv\Scripts\activate.bat" (
    echo     -> Đang khởi tạo thư mục môi trường ảo venv...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo     ⚠️ Không tạo được venv riêng, chuyển sang sử dụng Python trực tiếp.
    ) else (
        echo     -> Đã tạo venv thành công!
    )
) else (
    echo     -> Môi trường ảo venv đã sẵn sàng.
)
echo.

:: 3. KÍCH HOẠT VENV VÀ CÀI ĐẶT THƯ VIỆN PHỤ THUỘC
echo [3/4] Đang kiểm tra và cài đặt các thư viện cần thiết (requirements.txt)...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo ⚠️ Có cảnh báo khi cài thư viện. Đang thử cài đặt các gói chính...
    pip install google-api-python-client google-auth-oauthlib google-auth requests python-dotenv Pillow openpyxl
)
echo     -> Cài đặt thư viện hoàn tất!
echo.

:: 4. KIỂM TRA FILE CẤU HÌNH .ENV
echo [4/4] Kiểm tra tệp cấu hình tài khoản (.env)...
if not exist ".env" (
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo     -> Đã tạo file .env từ mẫu .env.example.
    )
)
echo.

echo ==============================================================================
echo 🎉 MÔI TRƯỜNG ĐÃ ĐƯỢC THIẾT LẬP THÀNH CÔNG!
echo Đang mở Trợ lý cấu hình tương tác (Setup Wizard) để giúp bạn kết nối tài khoản...
echo ==============================================================================
echo.
timeout /t 2 >nul

:: KHỞI CHẠY SETUP WIZARD
python setup_wizard.py

echo.
echo ==============================================================================
echo 👉 Bạn có thể mở file "MENU_CHINH.bat" bất kỳ lúc nào để quản trị hệ thống!
echo ==============================================================================
pause

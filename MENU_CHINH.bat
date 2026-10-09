@echo off
chcp 65001 >nul
title Blogger Gemini AI Cloud Poster - Menu Quản Trị
color 0F

:menu
cls
echo ==============================================================================
echo    ☁️ BLOGGER GEMINI AI CLOUD AUTO-POSTER - MENU QUẢN TRỊ CHÍNH ☁️
echo ==============================================================================
echo.
echo   [1] Cài đặt & Cập nhật thông số tài khoản (Setup Wizard)
echo   [2] Kiểm tra kết nối toàn bộ hệ thống (Diagnostic Test)
echo   [3] Lấy lại Google Refresh Token (OAuth Helper)
echo   --------------------------------------------------------------------------
echo   [4] Chạy đăng 1 bài viết ngay trên máy tính (Chạy thử nghiệm)
echo   [5] Chạy đăng bài tùy chọn số lượng (1, 2, 3... bài)
echo   --------------------------------------------------------------------------
echo   [6] Mở file danh sách đề tài (topics.txt)
echo   [7] Mở file lịch sử bài đã đăng (posted_history.json)
echo   --------------------------------------------------------------------------
echo   [8] Xem hướng dẫn cài đặt GitHub Actions (Chạy trên mây 24/7 Miễn phí)
echo   [9] Đóng gói bộ cài đặt sạch ra file .ZIP (Để gửi cho người khác)
echo   --------------------------------------------------------------------------
echo   [0] Thoát chương trình
echo.
echo ==============================================================================
set /p OPT="👉 Vui lòng chọn một chức năng [0-9]: "

if "%OPT%"=="1" goto opt1
if "%OPT%"=="2" goto opt2
if "%OPT%"=="3" goto opt3
if "%OPT%"=="4" goto opt4
if "%OPT%"=="5" goto opt5
if "%OPT%"=="6" goto opt6
if "%OPT%"=="7" goto opt7
if "%OPT%"=="8" goto opt8
if "%OPT%"=="9" goto opt9
if "%OPT%"=="0" exit /b 0

echo ⚠️ Lựa chọn không hợp lệ, vui lòng chọn lại!
timeout /t 2 >nul
goto menu

:opt1
cls
if exist "venv\Scripts\activate.bat" call venv\Scripts\activate.bat
python setup_wizard.py
goto menu

:opt2
cls
if exist "venv\Scripts\activate.bat" call venv\Scripts\activate.bat
python kiem_tra_ket_noi.py
goto menu

:opt3
cls
if exist "venv\Scripts\activate.bat" call venv\Scripts\activate.bat
python get_refresh_token.py
goto menu

:opt4
cls
if exist "venv\Scripts\activate.bat" call venv\Scripts\activate.bat
echo ==============================================================================
echo 🚀 ĐANG TIẾN HÀNH TẠO VÀ ĐĂNG 1 BÀI VIẾT LÊN BLOGGER...
echo ==============================================================================
set POSTS_COUNT=1
python main.py
echo.
echo Hoàn thành! Bấm phím bất kỳ để quay lại menu...
pause >nul
goto menu

:opt5
cls
if exist "venv\Scripts\activate.bat" call venv\Scripts\activate.bat
echo ==============================================================================
echo 🚀 TÙY CHỌN SỐ LƯỢNG BÀI VIẾT MUỐN ĐĂNG
echo ==============================================================================
set /p PCOUNT="Nhập số lượng bài muốn đăng (Mặc định: 1): "
if "%PCOUNT%"=="" set PCOUNT=1
set POSTS_COUNT=%PCOUNT%
echo.
echo Chế độ phát hành:
echo   [1] schedule - Lên lịch hẹn giờ theo Khung Giờ Vàng
echo   [2] publish  - Đăng công khai ngay lập tức
echo   [3] draft    - Lưu ở dạng bản nháp
set /p PMODE="Chọn chế độ [1/2/3] (Enter để dùng mặc định): "
if "%PMODE%"=="1" set POST_MODE=schedule
if "%PMODE%"=="2" set POST_MODE=publish
if "%PMODE%"=="3" set POST_MODE=draft
echo.
python main.py
echo.
echo Hoàn thành! Bấm phím bất kỳ để quay lại menu...
pause >nul
goto menu

:opt6
start notepad.exe "topics.txt"
goto menu

:opt7
start notepad.exe "posted_history.json"
goto menu

:opt8
cls
echo Đang mở tài liệu hướng dẫn trên trình duyệt...
if exist "HUONG_DAN_CAI_DAT.html" (
    start "" "HUONG_DAN_CAI_DAT.html"
) else (
    start notepad.exe "HUONG_DAN_CAI_DAT_CHO_NGUOI_MOI.md"
)
goto menu

:opt9
cls
if exist "venv\Scripts\activate.bat" call venv\Scripts\activate.bat
python dong_goi_zip.py
echo.
echo Bấm phím bất kỳ để quay lại menu...
pause >nul
goto menu

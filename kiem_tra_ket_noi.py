#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
  🔍 CÔNG CỤ CHẨN ĐOÁN & KIỂM TRA KẾT NỐI TOÀN DIỆN HỆ THỐNG
==============================================================================
Kiểm tra chi tiết:
1. Tệp cấu hình .env
2. Kết nối Google Gemini AI API
3. Kết nối Blogger API v3 (OAuth & Refresh Token)
4. Kết nối Telegram Bot (Nếu có)
5. Nguồn đề tài topics.txt & Lịch sử posted_history.json
==============================================================================
"""

import os
import sys
import json
import requests

# Đảm bảo mã hóa UTF-8 trên Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
except ImportError:
    Credentials = None
    build = None

def clean_val(v):
    if not v:
        return ''
    return str(v).strip().strip('"').strip("'").replace('\n', '').replace('\r', '').replace(' ', '')

def mask(s, show=4):
    if not s:
        return "(Trống)"
    if len(s) <= show * 2:
        return "***"
    return f"{s[:show]}...{s[-show:]}"

def main():
    print("=" * 72)
    print("      🔍 KIỂM TRA KẾT NỐI HỆ THỐNG BLOGGER GEMINI AI CLOUD")
    print("=" * 72)

    has_error = False

    # 1. KIỂM TRA TỆP .ENV
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    print("\n[1] Kiểm tra file môi trường .env:")
    if os.path.exists(env_path):
        print(f"    ✅ Tìm thấy file .env: {env_path}")
    else:
        print(f"    ⚠️ Chưa tìm thấy file .env. Hệ thống đang đọc từ biến môi trường hệ thống.")
        print(f"    👉 Bạn hãy chạy file 'CAI_DAT.bat' để tạo file .env.")

    # 2. KIỂM TRA GOOGLE GEMINI AI API KEYS (HỖ TRỢ NHIỀU KEY XOAY VÒNG)
    import re
    raw_keys = os.environ.get('GEMINI_API_KEY', '')
    backups = os.environ.get('GEMINI_API_KEYS', '') + ',' + os.environ.get('GEMINI_BACKUP_API_KEY', '')
    tokens = re.split(r'[,;\n\r]+', raw_keys + ',' + backups)
    gemini_pool = []
    for t in tokens:
        clean_k = clean_val(t)
        if clean_k and clean_k not in gemini_pool:
            gemini_pool.append(clean_k)

    for k in sorted(os.environ.keys()):
        if k.startswith('GEMINI_API_KEY_') or k.startswith('GEMINI_KEY_'):
            clean_k = clean_val(os.environ.get(k, ''))
            if clean_k and clean_k not in gemini_pool:
                gemini_pool.append(clean_k)

    print("\n[2] Kiểm tra Google Gemini AI API Key (Key Pool xoay vòng):")
    if not gemini_pool:
        print("    ❌ THIẾU GEMINI_API_KEY! Gemini là bộ não viết bài nên bắt buộc phải có ít nhất 1 key.")
        print("    👉 Lấy miễn phí tại: https://aistudio.google.com/app/apikey")
        has_error = True
    else:
        print(f"    🔑 Phát hiện {len(gemini_pool)} API Key trong hồ chứa (Key Pool):")
        valid_key_count = 0
        for idx, k in enumerate(gemini_pool, 1):
            k_masked = mask(k, 6)
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models?key={k}"
                res = requests.get(url, timeout=10)
                if res.status_code == 200:
                    print(f"       + Key #{idx} [{k_masked}]: ✅ Hoạt động tốt! (HTTP 200 OK)")
                    valid_key_count += 1
                else:
                    print(f"       + Key #{idx} [{k_masked}]: ❌ Lỗi kết nối (HTTP {res.status_code}): {res.text[:80]}")
            except Exception as e:
                print(f"       + Key #{idx} [{k_masked}]: ❌ Lỗi mạng: {e}")

        if valid_key_count > 0:
            print(f"    ✅ Đã kiểm tra xong: Có {valid_key_count}/{len(gemini_pool)} Key sẵn sàng hoạt động tự động xoay vòng!")
        else:
            print("    ❌ Tất cả các API Key đều không khả dụng. Vui lòng kiểm tra lại trên Google AI Studio.")
            has_error = True

    # 3. KIỂM TRA BLOGGER OAUTH V3
    blog_id = clean_val(os.environ.get('BLOGGER_BLOG_ID', ''))
    client_id = clean_val(os.environ.get('GOOGLE_CLIENT_ID', ''))
    client_secret = clean_val(os.environ.get('GOOGLE_CLIENT_SECRET', ''))
    refresh_token = clean_val(os.environ.get('GOOGLE_REFRESH_TOKEN', ''))

    print("\n[3] Kiểm tra thông số kết nối Blogger API v3:")
    print(f"    - Blogger Blog ID:    {blog_id or '(Trống)'}")
    print(f"    - Google Client ID:   {mask(client_id, 8)}")
    print(f"    - Client Secret:      {mask(client_secret, 4)}")
    print(f"    - Refresh Token:      {mask(refresh_token, 6)}")

    if not (blog_id and client_id and client_secret and refresh_token):
        print("    ❌ THIẾU THÔNG SỐ OAUTH BLOGGER!")
        if not blog_id:
            print("       + Thiếu BLOGGER_BLOG_ID (Lấy từ URL quản trị Blogger)")
        if not client_id or not client_secret:
            print("       + Thiếu GOOGLE_CLIENT_ID hoặc GOOGLE_CLIENT_SECRET (Tạo tại Google Cloud Console)")
        if not refresh_token:
            print("       + Thiếu GOOGLE_REFRESH_TOKEN (Chạy file LAY_REFRESH_TOKEN.bat để lấy)")
        has_error = True
    else:
        if build is None or Credentials is None:
            print("    ❌ Chưa cài đặt thư viện 'google-api-python-client' và 'google-auth'!")
            has_error = True
        else:
            try:
                creds = Credentials(
                    token=None,
                    refresh_token=refresh_token,
                    token_uri="https://oauth2.googleapis.com/token",
                    client_id=client_id,
                    client_secret=client_secret
                )
                service = build('blogger', 'v3', credentials=creds)
                binfo = service.blogs().get(blogId=blog_id).execute()
                print("    ✅ KẾT NỐI BLOGGER API THÀNH CÔNG RỰC RỠ!")
                print(f"       + Tên Blog:    {binfo.get('name')}")
                print(f"       + Địa chỉ URL: {binfo.get('url')}")
                print(f"       + Bài viết:    {binfo.get('posts', {}).get('totalItems', 0)} bài")
            except Exception as e:
                err_str = str(e)
                print(f"    ❌ LỖI KẾT NỐI BLOGGER API: {err_str}")
                if "invalid_grant" in err_str.lower():
                    print("       👉 Nguyên nhân: Refresh Token đã hết hạn hoặc bị hủy.")
                    print("       👉 Khắc phục: Chạy 'LAY_REFRESH_TOKEN.bat' để cấp quyền lại.")
                elif "404" in err_str:
                    print("       👉 Nguyên nhân: Blog ID không tồn tại hoặc tài khoản không có quyền truy cập.")
                elif "accessNotConfigured" in err_str:
                    print("       👉 Nguyên nhân: Bạn chưa bật Blogger API v3 trong Google Cloud Console.")
                has_error = True

    # 4. KIỂM TRA TELEGRAM (TÙY CHỌN)
    tg_token = clean_val(os.environ.get('TELEGRAM_BOT_TOKEN', ''))
    tg_chat = clean_val(os.environ.get('TELEGRAM_CHAT_ID', ''))
    print("\n[4] Kiểm tra thông báo Telegram (Tùy chọn):")
    if tg_token and tg_chat:
        try:
            res = requests.get(f"https://api.telegram.org/bot{tg_token}/getMe", timeout=8)
            if res.status_code == 200:
                bname = res.json().get('result', {}).get('first_name', 'Bot')
                print(f"    ✅ Kết nối Telegram Bot [{bname}] thành công!")
            else:
                print(f"    ⚠️ Telegram Bot Token không phản hồi đúng (HTTP {res.status_code})")
        except Exception as e:
            print(f"    ⚠️ Không kết nối được đến máy chủ Telegram: {e}")
    else:
        print("    ℹ️ Chưa cấu hình Telegram (Hệ thống vẫn hoạt động bình thường mà không cần Telegram).")

    # 5. KIỂM TRA ĐỀ TÀI & LỊCH SỬ
    topics_file = os.path.join(os.path.dirname(__file__), 'topics.txt')
    history_file = os.path.join(os.path.dirname(__file__), 'posted_history.json')
    print("\n[5] Kiểm tra tệp dữ liệu đề tài & lịch sử:")
    
    posted_count = 0
    if os.path.exists(history_file):
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                hdata = json.load(f)
                posted_count = len(hdata.get('history', []))
            print(f"    ✅ File lịch sử bài đăng: Đã lưu {posted_count} bài.")
        except Exception:
            print("    ⚠️ File posted_history.json bị lỗi định dạng.")
    else:
        print("    ℹ️ Chưa có file posted_history.json (Sẽ tự tạo khi đăng bài đầu tiên).")

    if os.path.exists(topics_file):
        with open(topics_file, 'r', encoding='utf-8') as f:
            t_lines = [l.strip() for l in f if l.strip() and not l.strip().startswith('#')]
        print(f"    ✅ File đề tài (topics.txt): Hiện có {len(t_lines)} đề tài dự phòng.")
    else:
        print(f"    ⚠️ Không tìm thấy file: {topics_file}")

    # 5b. KIỂM TRA GOOGLE SHEETS (NẾU CÓ CẤU HÌNH)
    sheet_url = os.environ.get('GOOGLE_SHEET_URL', '').strip()
    if sheet_url:
        print("\n[5b] Kiểm tra đồng bộ đề tài Google Sheets:")
        try:
            import re
            m = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', sheet_url)
            sid = m.group(1) if m else sheet_url[:15]
            gid_m = re.search(r'[#&?]gid=([0-9]+)', sheet_url)
            gid = gid_m.group(1) if gid_m else '0'
            csv_url = f"https://docs.google.com/spreadsheets/d/{sid}/gviz/tq?tqx=out:csv&gid={gid}"
            res = requests.get(csv_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if res.status_code == 200 and '<html' not in res.text.lower():
                print(f"    ✅ Kết nối Google Sheets thành công! Đã cấp quyền xem công khai chuẩn xác.")
            elif '<html' in res.text.lower():
                print(f"    ⚠️ CẢNH BÁO: Bảng tính Google Sheets chưa được BẬT quyền 'Bất kỳ ai có liên kết đều có thể xem'!")
            else:
                print(f"    ⚠️ Không thể tải dữ liệu Google Sheets (HTTP {res.status_code}).")
        except Exception as e:
            print(f"    ⚠️ Lỗi kết nối Google Sheets: {e}")

    print("\n" + "=" * 72)
    if not has_error:
        print("🎉 KẾT QUẢ: HỆ THỐNG HOÀN TOÀN KHỎE MẠNH VÀ SẴN SÀNG HOẠT ĐỘNG!")
        print("👉 Bạn có thể chạy ngay 'CHAY_DANG_BAI.bat' để kiểm tra viết & đăng bài.")
    else:
        print("⚠️ KẾT QUẢ: PHÁT HIỆN LỖI CẤU HÌNH CẦN KHẮC PHỤC!")
        print("👉 Bạn hãy chạy 'CAI_DAT.bat' để được hướng dẫn sửa lại các thông số.")
    print("=" * 72)

if __name__ == '__main__':
    main()
    if sys.platform.startswith('win') and sys.stdin.isatty():
        input("\nBấm phím Enter để đóng...")

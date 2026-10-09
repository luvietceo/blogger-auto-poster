#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Công cụ hỗ trợ lấy GOOGLE_REFRESH_TOKEN cho Blogger API v3
Chỉ cần chạy script này một lần duy nhất để lấy mã Refresh Token vĩnh viễn!
Tự động lưu vào file .env trên máy tính.
"""

import sys
import os

# Đảm bảo mã hóa UTF-8 trên Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdin.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    print("Vui lòng cài đặt thư viện trước bằng lệnh:")
    print("pip install google-auth-oauthlib")
    sys.exit(1)

SCOPES = [
    'https://www.googleapis.com/auth/blogger',
    'https://www.googleapis.com/auth/blogger.readonly'
]

ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

def update_env_variable(key, val):
    """Cập nhật hoặc thêm biến vào file .env"""
    lines = []
    found = False
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.strip().startswith(f"{key}=") or line.strip().startswith(f"#{key}="):
                lines[i] = f"{key}={val}\n"
                found = True
                break
    if not found:
        lines.append(f"{key}={val}\n")
    with open(ENV_FILE, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"💾 Đã tự động cập nhật {key} vào file .env!")

import argparse

def main():
    parser = argparse.ArgumentParser(description="Tự động tạo Google Refresh Token cho Blogger API")
    parser.add_argument('--client-id', type=str, help="Google OAuth Client ID")
    parser.add_argument('--client-secret', type=str, help="Google OAuth Client Secret")
    parser.add_argument('--port', type=int, default=8080, help="Local OAuth server port")
    parser.add_argument('--non-interactive', action='store_true', help="Chạy không chờ nhập từ bàn phím (cho AI/Script)")
    args = parser.parse_args()

    print("=" * 68)
    print("🔑 CÔNG CỤ TỰ ĐỘNG TẠO GOOGLE REFRESH TOKEN CHO BLOGGER API")
    print("=" * 68)
    print("\nTrước khi chạy, bạn cần có:")
    print("1. Google Client ID (dạng: xxxx.apps.googleusercontent.com)")
    print("2. Google Client Secret (dạng: GOCSPX-xxxx)")
    print("(Nếu chưa có, hãy tạo tại: https://console.cloud.google.com/apis/credentials)\n")

    client_id = args.client_id or os.environ.get('GOOGLE_CLIENT_ID', '').strip()
    client_secret = args.client_secret or os.environ.get('GOOGLE_CLIENT_SECRET', '').strip()

    if client_id and client_secret and not args.non_interactive and not args.client_id:
        print(f"👉 Tìm thấy thông tin sẵn có trong .env:")
        print(f"   - Client ID: {client_id[:10]}...{client_id[-10:]}")
        use_exist = input("   Sử dụng thông tin này để đăng nhập? (Y/n): ").strip().lower()
        if use_exist == 'n':
            client_id = ''
            client_secret = ''

    if not client_id:
        if args.non_interactive:
            print("❌ Lỗi: Thiếu Client ID trong chế độ non-interactive!")
            sys.exit(1)
        client_id = input("Nhập Google Client ID: ").strip()
    if not client_secret:
        if args.non_interactive:
            print("❌ Lỗi: Thiếu Client Secret trong chế độ non-interactive!")
            sys.exit(1)
        client_secret = input("Nhập Google Client Secret: ").strip()

    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [f"http://localhost:{args.port}/"]
        }
    }

    print("\n🌐 Đang mở trình duyệt để bạn đăng nhập và cấp quyền cho Blogger...")
    print("👉 Vui lòng đăng nhập tài khoản Google quản lý Blog.")
    print("💡 MẸO VƯỢT CẢNH BÁO GOOGLE: Nếu màn hình hiện 'Google chưa xác minh ứng dụng này'")
    print("   -> Bấm vào chữ 'Nâng cao' (Advanced) ở góc dưới")
    print("   -> Bấm 'Chuyển đến [Tên ứng dụng] (không an toàn)'")
    print("   -> Tích chọn ủy quyền Blogger và bấm 'Tiếp tục' / 'Cho phép (Allow)'.")
    try:
        flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
        creds = flow.run_local_server(port=args.port, prompt='consent', access_type='offline')
    except Exception as e:
        print(f"\n❌ Lỗi khi xác thực OAuth: {e}")
        if not args.non_interactive and sys.stdin.isatty():
            input("\nBấm Enter để thoát...")
        sys.exit(1)

    print("\n" + "=" * 68)
    print("🎉 ĐĂNG NHẬP THÀNH CÔNG! ĐÂY LÀ MÃ REFRESH TOKEN CỦA BẠN:")
    print("=" * 68)
    print(f"\nGOOGLE_REFRESH_TOKEN={creds.refresh_token}\n")
    
    # Tự động lưu vào .env
    update_env_variable('GOOGLE_CLIENT_ID', client_id)
    update_env_variable('GOOGLE_CLIENT_SECRET', client_secret)
    update_env_variable('GOOGLE_REFRESH_TOKEN', creds.refresh_token)
    
    print("\n👉 Hãy sao chép chuỗi mã trên nếu bạn muốn cài đặt vào GitHub Secrets (chạy trên mây)!")
    print("=" * 68)
    if not args.non_interactive and sys.stdin.isatty():
        input("\nBấm phím Enter để đóng...")

if __name__ == '__main__':
    main()

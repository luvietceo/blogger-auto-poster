#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
  ☁️ TRỢ LÝ CÀI ĐẶT & THIẾT LẬP TỰ ĐỘNG - BLOGGER GEMINI AI CLOUD POSTER
==============================================================================
Tự động hướng dẫn cấu hình:
1. Google Gemini AI API Key (Miễn phí)
2. Blogger Blog ID
3. Google Cloud OAuth (Client ID & Client Secret)
4. Tự động lấy Refresh Token 1-Click qua trình duyệt
5. Cấu hình Telegram, Google Sheets, Chế độ đăng bài
6. Tự động kiểm tra và xác thực toàn diện kết nối hệ thống
==============================================================================
"""

import os
import sys
import json
import re
import time
import webbrowser

# Đảm bảo mã hóa UTF-8 trên Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stdin.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    import requests
except ImportError:
    print("❌ Thiếu thư viện 'requests'. Vui lòng chạy: pip install requests")
    sys.exit(1)

try:
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    print("❌ Thiếu thư viện Google API. Vui lòng chạy: pip install -r requirements.txt")
    sys.exit(1)

ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
ENV_EXAMPLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env.example')
SCOPES = [
    'https://www.googleapis.com/auth/blogger',
    'https://www.googleapis.com/auth/blogger.readonly'
]

def load_current_env():
    """Đọc file .env nếu có, trả về dict cấu hình"""
    config = {}
    target = ENV_FILE if os.path.exists(ENV_FILE) else (ENV_EXAMPLE if os.path.exists(ENV_EXAMPLE) else None)
    if target and os.path.exists(target):
        with open(target, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    config[k.strip()] = v.strip().strip('"').strip("'")
    return config

def save_env_file(config):
    """Lưu cấu hình chuẩn hóa vào file .env"""
    content = f"""# ==============================================================================
# CẤU HÌNH TỰ ĐỘNG HÓA BLOGGER GEMINI AI CLOUD AUTO-POSTER
# Tạo tự động bởi Setup Wizard vào: {time.strftime('%Y-%m-%d %H:%M:%S')}
# ==============================================================================

# 1. Thông tin thương hiệu, lĩnh vực & kênh chuyển đổi (Custom Prompt Engine)
BRAND_NAME={config.get('BRAND_NAME', '')}
WEBSITE_NICHE={config.get('WEBSITE_NICHE', '')}
WEBSITE_URL={config.get('WEBSITE_URL', '')}
ZALO_URL={config.get('ZALO_URL', '')}
HOTLINE={config.get('HOTLINE', '')}
FANPAGE_URL={config.get('FANPAGE_URL', '')}
CTA_URL={config.get('CTA_URL', config.get('ZALO_URL', ''))}
REGISTER_URL={config.get('REGISTER_URL', config.get('CTA_URL', ''))}

# 2. Google Gemini AI API Key (Lấy miễn phí tại: https://aistudio.google.com/app/apikey)
GEMINI_API_KEY={config.get('GEMINI_API_KEY', '')}
GEMINI_API_KEYS={config.get('GEMINI_API_KEYS', '')}

# 3. ID Blog trên Blogger (Dãy số trên URL quản trị: https://www.blogger.com/blog/posts/XXXXX)
BLOGGER_BLOG_ID={config.get('BLOGGER_BLOG_ID', '')}

# 4. Google Cloud OAuth 2.0 Credentials (Tạo tại: https://console.cloud.google.com/apis/credentials)
GOOGLE_CLIENT_ID={config.get('GOOGLE_CLIENT_ID', '')}
GOOGLE_CLIENT_SECRET={config.get('GOOGLE_CLIENT_SECRET', '')}
GOOGLE_REFRESH_TOKEN={config.get('GOOGLE_REFRESH_TOKEN', '')}

# 5. Chế độ phát hành: 'schedule' (Lên lịch giờ vàng) | 'publish' (Đăng ngay) | 'draft' (Lưu nháp)
POST_MODE={config.get('POST_MODE', 'schedule')}
SCHEDULE_HOURS_AHEAD={config.get('SCHEDULE_HOURS_AHEAD', '24')}

# 6. Thông báo Telegram báo cáo tức thì (Tùy chọn)
TELEGRAM_BOT_TOKEN={config.get('TELEGRAM_BOT_TOKEN', '')}
TELEGRAM_CHAT_ID={config.get('TELEGRAM_CHAT_ID', '')}

# 7. Đồng bộ đề tài Google Sheets & Webhook báo cáo (Tùy chọn)
GOOGLE_SHEET_URL={config.get('GOOGLE_SHEET_URL', '')}
GOOGLE_SHEET_WEBHOOK_URL={config.get('GOOGLE_SHEET_WEBHOOK_URL', '')}
"""
    with open(ENV_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n💾 Đã lưu cấu hình vào: {ENV_FILE}")

def mask_secret(s, show_chars=4):
    if not s:
        return "(Chưa có)"
    if len(s) <= show_chars * 2:
        return "***"
    return f"{s[:show_chars]}...{s[-show_chars:]}"

def test_gemini_key(api_key):
    """Kiểm tra Gemini API Key"""
    if not api_key:
        return False, "Chưa nhập API Key"
    
    clean_k = api_key.strip().replace('\n', '').replace(' ', '')
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={clean_k}"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return True, "Kết nối thành công! API Key hợp lệ và sẵn sàng hoạt động."
        elif resp.status_code == 400:
            return False, "API Key không hợp lệ (Mã 400 - Invalid API Key)."
        elif resp.status_code == 403:
            return False, "API Key bị từ chối truy cập (Mã 403 - Permission Denied)."
        else:
            return False, f"Lỗi HTTP {resp.status_code}: {resp.text[:100]}"
    except Exception as e:
        return False, f"Không thể kết nối đến máy chủ Google: {e}"

def test_blogger_connection(client_id, client_secret, refresh_token, blog_id):
    """Kiểm tra kết nối Blogger API v3 và lấy thông tin blog"""
    if not (client_id and client_secret and refresh_token and blog_id):
        return False, "Thiếu một trong các thông số: Client ID, Secret, Refresh Token hoặc Blog ID"
    
    try:
        creds = Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri="https://oauth2.googleapis.com/token",
            client_id=client_id,
            client_secret=client_secret
        )
        service = build('blogger', 'v3', credentials=creds)
        blog_info = service.blogs().get(blogId=blog_id).execute()
        blog_name = blog_info.get('name', 'Không xác định')
        blog_url = blog_info.get('url', '')
        total_posts = blog_info.get('posts', {}).get('totalItems', 0)
        return True, {
            "name": blog_name,
            "url": blog_url,
            "total_posts": total_posts
        }
    except Exception as e:
        err_msg = str(e)
        if "404" in err_msg:
            return False, f"Không tìm thấy Blog ID: {blog_id}. Vui lòng kiểm tra lại dãy số Blog ID."
        elif "invalid_grant" in err_msg.lower():
            return False, "Refresh Token không hợp lệ hoặc đã hết hạn! Vui lòng lấy lại Token mới."
        elif "unauthorized" in err_msg.lower() or "401" in err_msg:
            return False, "Client ID hoặc Client Secret không chính xác."
        elif "accessNotConfigured" in err_msg:
            return False, "Chưa bật Blogger API v3 trên Google Cloud Console! Vui lòng vào bật API."
        return False, f"Lỗi kết nối Blogger: {err_msg}"

def run_oauth_flow(client_id, client_secret):
    """Mở trình duyệt để người dùng đăng nhập và tự động lấy Refresh Token"""
    print("\n🌐 Chuẩn bị mở trình duyệt đăng nhập Google...")
    print("👉 Hãy đăng nhập tài khoản Google đang quản lý Blogger của bạn.")
    print("💡 MẸO VƯỢT CẢNH BÁO GOOGLE: Nếu màn hình hiện 'Google chưa xác minh ứng dụng này'")
    print("   -> Bấm vào chữ 'Nâng cao' (Advanced) ở góc dưới")
    print("   -> Bấm 'Chuyển đến [Tên ứng dụng] (không an toàn)'")
    print("   -> Tích chọn ủy quyền và bấm 'Tiếp tục' / 'Cho phép (Allow)'.")
    
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost:8080/"]
        }
    }
    
    flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
    creds = flow.run_local_server(port=8080, prompt='consent', access_type='offline')
    
    if creds and creds.refresh_token:
        print("\n🎉 LẤY REFRESH TOKEN THÀNH CÔNG!")
        print(f"🔑 GOOGLE_REFRESH_TOKEN: {mask_secret(creds.refresh_token, 6)}")
        return creds.refresh_token
    else:
        print("\n⚠️ Không nhận được Refresh Token. Đang thử lại với quyền force consent...")
        return None

def interactive_wizard():
    print("=" * 72)
    print("    ☁️ TRỢ LÝ CÀI ĐẶT & THIẾT LẬP TỰ ĐỘNG BLOGGER GEMINI CLOUD ☁️")
    print("              (Dành cho mọi người - Cài đặt chỉ mất 3-5 phút)")
    print("=" * 72)
    print("Hệ thống sẽ hướng dẫn bạn cấu hình từng thông số một cách dễ dàng nhất.\n")

    cfg = load_current_env()

    # BƯỚC 1: THÔNG TIN SHOP, WEBSITE & NGÀNH NGHỀ (TẠO PROMPT AI ĐỘC QUYỀN)
    print("-" * 72)
    print("📌 BƯỚC 1: THÔNG TIN SHOP, WEBSITE & NGÀNH NGHỀ (TẠO PROMPT AI)")
    print("-" * 72)
    print("AI sẽ dùng các thông tin này để 'may đo' phong cách viết bài chuẩn SEO & CRO,")
    print("đóng vai chuyên gia đúng ngành và chèn link chuyển đổi về chính shop của bạn.\n")

    current_brand = cfg.get('BRAND_NAME', '')
    print(f"1. Tên website / shop / thương hiệu: {current_brand or '(Chưa có)'}")
    nhap_brand = input("   Nhập tên thương hiệu (VD: Điện Máy Xanh, Đất Vàng Land, Spa Thảo Mộc...): ").strip()
    if nhap_brand:
        cfg['BRAND_NAME'] = nhap_brand

    current_niche = cfg.get('WEBSITE_NICHE', '')
    print(f"\n2. Lĩnh vực / ngành nghề chính: {current_niche or '(Chưa có)'}")
    nhap_niche = input("   Nhập ngành nghề (VD: Điện máy gia dụng, Bất động sản, Spa - Làm đẹp, Thời trang...): ").strip()
    if nhap_niche:
        cfg['WEBSITE_NICHE'] = nhap_niche

    current_url = cfg.get('WEBSITE_URL', '')
    print(f"\n3. Link website / blog chính thức: {current_url or '(Chưa có)'}")
    nhap_url = input("   Nhập link website (VD: https://shopcuaban.com hoặc link blogspot): ").strip()
    if nhap_url:
        cfg['WEBSITE_URL'] = nhap_url

    current_zalo = cfg.get('ZALO_URL', cfg.get('CTA_URL', ''))
    print(f"\n4. Kênh tư vấn Zalo / Hotline chốt khách: {current_zalo or '(Chưa có)'}")
    nhap_zalo = input("   Nhập link Zalo hoặc SĐT tư vấn (VD: https://zalo.me/0987xxxxxx): ").strip()
    if nhap_zalo:
        if not nhap_zalo.startswith('http') and nhap_zalo.replace('.', '').replace(' ', '').isdigit():
            nhap_zalo = f"https://zalo.me/{nhap_zalo.replace('.', '').replace(' ', '')}"
        cfg['ZALO_URL'] = nhap_zalo
        cfg['CTA_URL'] = nhap_zalo
        cfg['REGISTER_URL'] = nhap_zalo

    current_hotline = cfg.get('HOTLINE', '')
    nhap_hotline = input(f"\n5. Hotline tư vấn nhanh (Enter để bỏ qua) [{current_hotline}]: ").strip()
    if nhap_hotline:
        cfg['HOTLINE'] = nhap_hotline

    print(f"\n✨ ĐÃ MAY ĐO XONG PROMPT AI ĐỘC QUYỀN:")
    print(f"   🏢 Ngành nghề: [{cfg.get('WEBSITE_NICHE', 'Chuyên gia tư vấn')}]")
    print(f"   🏷️ Thương hiệu: [{cfg.get('BRAND_NAME', 'Website')}]")
    print(f"   🌐 Website:    [{cfg.get('WEBSITE_URL', 'Chưa có')}]")
    print(f"   💬 Kênh chốt:  [{cfg.get('CTA_URL', 'Chưa có')}]")

    # BƯỚC 2: GEMINI API KEY
    print("\n" + "-" * 72)
    print("📌 BƯỚC 2: KHÓA GOOGLE GEMINI AI API KEY (Miễn phí)")
    print("-" * 72)
    print("Gemini AI sẽ là 'bộ não' tự động viết nội dung chuẩn SEO 1500+ từ.")
    print("👉 Lấy khóa miễn phí tại: https://aistudio.google.com/app/apikey")
    current_gemini = cfg.get('GEMINI_API_KEY', '')
    print(f"Giá trị hiện tại: {mask_secret(current_gemini)}")
    
    nhap_gemini = input("Nhập Gemini API Key mới (Bấm Enter để giữ nguyên hiện tại): ").strip()
    if nhap_gemini:
        cfg['GEMINI_API_KEY'] = nhap_gemini
    
    # Kiểm tra key
    if cfg.get('GEMINI_API_KEY'):
        print("⏳ Đang kiểm tra tính hợp lệ của Gemini API Key...")
        ok, msg = test_gemini_key(cfg['GEMINI_API_KEY'])
        if ok:
            print(f"✅ {msg}")
        else:
            print(f"⚠️ Cảnh báo: {msg}")
            print("Bạn vẫn có thể tiếp tục và kiểm tra lại key sau.")

    # BƯỚC 3: BLOGGER BLOG ID
    print("\n" + "-" * 72)
    print("📌 BƯỚC 3: BLOGGER BLOG ID")
    print("-" * 72)
    print("Mã số định danh trang Blogger của bạn.")
    print("👉 Cách lấy: Mở blogger.com -> Nhìn lên thanh URL trình duyệt web:")
    print("   Ví dụ: https://www.blogger.com/blog/posts/1444221897689962852")
    print("   => Blog ID chính là dãy số dài: 1444221897689962852")
    current_blog_id = cfg.get('BLOGGER_BLOG_ID', '')
    print(f"Giá trị hiện tại: {current_blog_id or '(Chưa có)'}")
    
    nhap_blog_id = input("Nhập Blogger Blog ID (Bấm Enter để giữ nguyên): ").strip()
    if nhap_blog_id:
        cfg['BLOGGER_BLOG_ID'] = re.sub(r'[^0-9]', '', nhap_blog_id)
        print(f"✅ Đã ghi nhận Blog ID: {cfg['BLOGGER_BLOG_ID']}")

    # BƯỚC 4: GOOGLE OAUTH CLIENT ID & CLIENT SECRET
    print("\n" + "-" * 72)
    print("📌 BƯỚC 4: GOOGLE CLOUD OAUTH (CLIENT ID & CLIENT SECRET)")
    print("-" * 72)
    print("Cấp quyền cho robot thay mặt bạn đăng bài lên Blogger.")
    print("👉 Tạo tại: https://console.cloud.google.com/apis/credentials")
    print("   (Chọn dự án -> Bật Blogger API v3 -> Tạo OAuth Client ID loại 'Desktop App')")
    
    current_cid = cfg.get('GOOGLE_CLIENT_ID', '')
    current_sec = cfg.get('GOOGLE_CLIENT_SECRET', '')
    print(f"Client ID hiện tại:     {mask_secret(current_cid, 8)}")
    print(f"Client Secret hiện tại: {mask_secret(current_sec, 4)}")
    
    nhap_cid = input("Nhập Google Client ID (Enter để giữ nguyên): ").strip()
    if nhap_cid:
        cfg['GOOGLE_CLIENT_ID'] = nhap_cid
    
    nhap_sec = input("Nhập Google Client Secret (Enter để giữ nguyên): ").strip()
    if nhap_sec:
        cfg['GOOGLE_CLIENT_SECRET'] = nhap_sec

    # BƯỚC 5: TỰ ĐỘNG LẤY GOOGLE REFRESH TOKEN
    print("\n" + "-" * 72)
    print("📌 BƯỚC 5: GOOGLE REFRESH TOKEN (ỦY QUYỀN ĐĂNG BÀI)")
    print("-" * 72)
    current_rf = cfg.get('GOOGLE_REFRESH_TOKEN', '')
    print(f"Refresh Token hiện tại: {mask_secret(current_rf, 6)}")
    
    need_token = True
    if current_rf:
        choice = input("Bạn đã có Refresh Token. Có muốn lấy lại Token mới không? (y/N): ").strip().lower()
        if choice != 'y':
            need_token = False
    
    if need_token:
        if cfg.get('GOOGLE_CLIENT_ID') and cfg.get('GOOGLE_CLIENT_SECRET'):
            choice_login = input("Bạn có muốn mở trình duyệt để lấy Refresh Token tự động ngay bây giờ? (Y/n): ").strip().lower()
            if choice_login != 'n':
                try:
                    rf_token = run_oauth_flow(cfg['GOOGLE_CLIENT_ID'], cfg['GOOGLE_CLIENT_SECRET'])
                    if rf_token:
                        cfg['GOOGLE_REFRESH_TOKEN'] = rf_token
                except Exception as e:
                    print(f"⚠️ Quá trình mở OAuth gặp sự cố: {e}")
                    print("Bạn có thể nhập thủ công hoặc chạy lại sau bằng file: LAY_REFRESH_TOKEN.bat")
        else:
            print("⚠️ Cần có Client ID và Client Secret ở Bước 4 trước khi lấy Refresh Token.")

    # BƯỚC 6: CẤU HÌNH PHÁT HÀNH BÀI VIẾT
    print("\n" + "-" * 72)
    print("📌 BƯỚC 6: CHẾ ĐỘ PHÁT HÀNH BÀI VIẾT")
    print("-" * 72)
    print("Chọn cách hệ thống xử lý khi viết bài xong:")
    print("  [1] schedule : Lên lịch hẹn giờ tự động vào các Khung Giờ Vàng (Khuyên dùng)")
    print("  [2] publish  : Đăng công khai ngay lập tức lên Blogger")
    print("  [3] draft    : Lưu ở dạng Bản Nháp để bạn tự duyệt lại trước khi đăng")
    current_mode = cfg.get('POST_MODE', 'schedule')
    print(f"Chế độ hiện tại: {current_mode}")
    
    mode_input = input("Chọn chế độ [1/2/3] (Enter để giữ nguyên): ").strip()
    if mode_input == '1':
        cfg['POST_MODE'] = 'schedule'
    elif mode_input == '2':
        cfg['POST_MODE'] = 'publish'
    elif mode_input == '3':
        cfg['POST_MODE'] = 'draft'

    # BƯỚC 7: THÔNG BÁO TELEGRAM (TÙY CHỌN)
    print("\n" + "-" * 72)
    print("📌 BƯỚC 7: BÁO CÁO QUA TELEGRAM (Tùy chọn - Có thể bỏ qua)")
    print("-" * 72)
    print("Nhận thông báo bài đăng và link trực tiếp về điện thoại.")
    current_tg_token = cfg.get('TELEGRAM_BOT_TOKEN', '')
    current_tg_chat = cfg.get('TELEGRAM_CHAT_ID', '')
    print(f"Telegram Bot Token hiện tại: {mask_secret(current_tg_token, 6)}")
    print(f"Telegram Chat ID hiện tại:   {current_tg_chat or '(Chưa có)'}")
    
    ask_tg = input("Bạn có muốn cấu hình Telegram không? (y/N): ").strip().lower()
    if ask_tg == 'y':
        nhap_tg_token = input("Nhập Bot Token (từ @BotFather): ").strip()
        if nhap_tg_token:
            cfg['TELEGRAM_BOT_TOKEN'] = nhap_tg_token
        nhap_tg_chat = input("Nhập Chat ID nhóm/kênh: ").strip()
        if nhap_tg_chat:
            cfg['TELEGRAM_CHAT_ID'] = nhap_tg_chat

    # BƯỚC 8: CẤU HÌNH ĐỀ TÀI GOOGLE SHEETS (TÙY CHỌN)
    print("\n" + "-" * 72)
    print("📌 BƯỚC 8: QUẢN LÝ ĐỀ TÀI QUA GOOGLE SHEETS (Tùy chọn)")
    print("-" * 72)
    print("🌟 Link template mẫu chuẩn cho người mới (1-Click tạo bản sao):")
    print("👉 https://docs.google.com/spreadsheets/d/1VTsUaq33Wt-YBekNBUGS7pphOsJ7W4-ai5zwy9WEnkY/copy")
    current_sheet = cfg.get('GOOGLE_SHEET_URL', '')
    print(f"Link Sheet hiện tại: {current_sheet or '(Chưa cài - Đang dùng topics.txt)'}")
    ask_sheet = input("Nhập link Google Sheet của bạn (Enter để bỏ qua/giữ nguyên): ").strip()
    if ask_sheet:
        cfg['GOOGLE_SHEET_URL'] = ask_sheet

    # LƯU FILE .ENV
    save_env_file(cfg)

    # BƯỚC 9: KIỂM TRA CHẨN ĐOÁN TOÀN DIỆN
    print("\n" + "=" * 72)
    print("🔍 ĐANG KIỂM TRA KẾT NỐI TOÀN DIỆN HỆ THỐNG...")
    print("=" * 72)
    
    # 1. Test Gemini
    gemini_ok, gemini_msg = test_gemini_key(cfg.get('GEMINI_API_KEY'))
    print(f"1. Google Gemini AI API:    {'[OK] Thành công' if gemini_ok else '[LỖI] ' + gemini_msg}")
    
    # 2. Test Blogger
    blogger_ok, blogger_res = test_blogger_connection(
        cfg.get('GOOGLE_CLIENT_ID'),
        cfg.get('GOOGLE_CLIENT_SECRET'),
        cfg.get('GOOGLE_REFRESH_TOKEN'),
        cfg.get('BLOGGER_BLOG_ID')
    )
    if blogger_ok:
        print(f"2. Kết nối Blogger API:      [OK] Thành công")
        print(f"   - Tên Blog: {blogger_res['name']}")
        print(f"   - Địa chỉ URL: {blogger_res['url']}")
        print(f"   - Tổng số bài hiện có: {blogger_res['total_posts']} bài")
    else:
        print(f"2. Kết nối Blogger API:      [LỖI] {blogger_res}")

    print("\n" + "=" * 72)
    if gemini_ok and blogger_ok:
        print("🎉 XIN CHÚC MỪNG! HỆ THỐNG ĐÃ SẴN SÀNG HOẠT ĐỘNG 100%!")
        print("Bạn có thể:")
        print("👉 Chạy 'CHAY_DANG_BAI.bat' để bắt đầu đăng bài ngay trên máy tính.")
        print("👉 Hoặc xem tài liệu 'HUONG_DAN_CAI_DAT_CHO_NGUOI_MOI.md' để đưa lên")
        print("   GitHub Actions chạy tự động trên đám mây 24/7 hoàn toàn miễn phí!")
    else:
        print("⚠️ Có một vài thông số chưa chính xác. Vui lòng kiểm tra lại thông báo ở trên.")
        print("Bạn có thể chạy lại file 'CAI_DAT.bat' bất kỳ lúc nào để điều chỉnh.")
    print("=" * 72)
    input("\nBấm phím Enter để quay lại menu...")

if __name__ == '__main__':
    try:
        interactive_wizard()
    except KeyboardInterrupt:
        print("\n\n👋 Đã hủy thao tác.")

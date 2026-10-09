#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
  📦 KỊCH BẢN TỰ ĐỘNG ĐÓNG GÓI BỘ CÀI ĐẶT SẠCH RA FILE .ZIP
==============================================================================
Chức năng:
- Tự động nén toàn bộ mã nguồn hệ thống thành file ZIP hoàn chỉnh.
- Tự động LOẠI TRỪ các dữ liệu nhạy cảm hoặc file rác:
  + .env (Không lộ khóa API cá nhân, chỉ giữ .env.example)
  + .git/ (Không dính commit lịch sử riêng)
  + venv/ (Môi trường ảo của máy gốc)
  + __pycache__/ (File biên dịch tạm)
  + thumbnails/*.webp (Xóa ảnh đã tạo trước, chỉ giữ .gitkeep)
  + posted_history.json (Tự reset về lịch sử trắng mới tinh)
==============================================================================
"""

import os
import sys
import zipfile
import json

# Đảm bảo mã hóa UTF-8 trên Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_NAME = "Blogger_Auto_Cloud_Tron_Goi.zip"
ZIP_PATH = os.path.join(ROOT_DIR, ZIP_NAME)

EXCLUDE_DIRS = {
    '.git',
    'venv',
    '.venv',
    'env',
    '__pycache__',
    '.idea',
    '.vscode',
    'dist',
    'build',
}

EXCLUDE_EXTENSIONS = {
    '.pyc',
    '.pyo',
    '.log',
    '.tmp',
    '.zip',
    '.xml',    # Loại trừ 100% toàn bộ mẫu giao diện web/theme Blogger cá nhân
    '.xlsx',   # Loại trừ 100% toàn bộ file Excel kế hoạch riêng
}

EXCLUDE_PATTERNS = [
    '.env',
    '.env.local',
    'BNI',
    'LuViet',
    'Ke_Hoach_Dang_Bai',
    'sample_bg',
    'create_excel_plan',
    'BAI_DANG_BLOGGER',
    'HUONG_DAN_CAI_DAT_BLOGGER_TU_DONG',
    'client_secret',
    'service_account',
    'credentials',
    'token.json',
    'token.pickle',
]

def should_exclude(rel_path):
    parts = rel_path.replace('\\', '/').split('/')
    for part in parts:
        if part in EXCLUDE_DIRS:
            return True
        if part.endswith('_backup') or part.startswith('.gemini'):
            return True
            
    base_name = os.path.basename(rel_path)
    if base_name == '.env.example':
        return False  # BẮT BUỘC GIỮ: File cấu hình mẫu sạch cho người dùng mới

    if base_name == '.env' or base_name.startswith('.env.'):
        return True   # BẢO MẬT TUYỆT ĐỐI: Loại trừ toàn bộ file chứa khóa thật

    _, ext = os.path.splitext(base_name)
    if ext.lower() in EXCLUDE_EXTENSIONS:
        return True

    for pat in EXCLUDE_PATTERNS:
        if pat == '.env':
            continue
        if pat.lower() in base_name.lower():
            return True

    if rel_path.startswith('thumbnails/') or rel_path.startswith('thumbnails\\'):
        if base_name != '.gitkeep':
            return True

    return False

def make_clean_package():
    print("=" * 72)
    print("       📦 BẮT ĐẦU ĐÓNG GÓI BỘ CÀI ĐẶT SẠCH SẼ CHO NGƯỜI DÙNG")
    print("=" * 72)
    print(f"Thư mục nguồn: {ROOT_DIR}")
    print(f"Tên file nén:  {ZIP_NAME}\n")

    # Xóa file zip cũ nếu có
    if os.path.exists(ZIP_PATH):
        try:
            os.remove(ZIP_PATH)
        except Exception:
            pass

    count = 0
    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(ROOT_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ROOT_DIR)

                if should_exclude(rel_path):
                    continue

                # Nếu là posted_history.json, ghi bản trắng sạch
                if file == 'posted_history.json':
                    clean_history = {
                        "total_posted": 0,
                        "last_updated": None,
                        "history": []
                    }
                    clean_json_str = json.dumps(clean_history, ensure_ascii=False, indent=2)
                    zipf.writestr(rel_path.replace('\\', '/'), clean_json_str)
                    print(f"  [+] Reset sạch lịch sử: {rel_path}")
                    count += 1
                    continue

                # Thêm file bình thường
                zipf.write(full_path, rel_path.replace('\\', '/'))
                print(f"  [+] Nén file: {rel_path}")
                count += 1

    file_size_mb = os.path.getsize(ZIP_PATH) / (1024 * 1024)
    print("\n" + "=" * 72)
    print("🎉 ĐÓNG GÓI THÀNH CÔNG RỰC RỠ!")
    print(f"📁 Tệp nén thành phẩm: {ZIP_PATH}")
    print(f"📊 Tổng số file:       {count} tệp")
    print(f"💾 Dung lượng:         {file_size_mb:.2f} MB")
    print("=" * 72)
    print("\n👉 BÂY GIỜ BẠN CÓ THỂ:")
    print("1. Gửi file zip này qua Zalo, Google Drive hoặc Telegram cho bất kỳ ai.")
    print("2. Người nhận chỉ cần giải nén ra và bấm 'CAI_DAT.bat' là dùng được ngay!")
    print("=" * 72)

if __name__ == '__main__':
    make_clean_package()

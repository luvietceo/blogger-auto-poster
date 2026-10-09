import json
import os
import re
import sys
from dotenv import load_dotenv

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

load_dotenv()

creds = Credentials(
    token=None,
    refresh_token=os.getenv('GOOGLE_REFRESH_TOKEN'),
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    token_uri='https://oauth2.googleapis.com/token'
)
service = build('blogger', 'v3', credentials=creds)
blog_id = os.getenv('BLOGGER_BLOG_ID')

with open('posted_history.json', 'r', encoding='utf-8') as f:
    history = json.load(f)

print(f"Bắt đầu kiểm tra và cập nhật cho {len(history.get('history', []))} bài viết...")

for item in history.get('history', []):
    post_id = item['post_id']
    try:
        post = service.posts().get(blogId=blog_id, postId=post_id, view='AUTHOR').execute()
        content = post.get('content', '')
        title = post.get('title', '')
        updated = False

        # 1. Sửa link ảnh từ owner/blogger-auto-cloud sang luvietceo/blogger-auto-poster
        if 'owner/blogger-auto-cloud' in content:
            content = content.replace('owner/blogger-auto-cloud', 'luvietceo/blogger-auto-poster')
            updated = True
            print(f"  [FIX IMAGE URL] Đã sửa link ảnh trong bài '{title}' ({post_id})")

        # 2. Bọc [tintuc] nếu chưa có
        if '[tintuc]' not in content:
            content = f"[tintuc]{content}[/tintuc]"
            updated = True
            print(f"  [FIX TINTUC] Đã bọc [tintuc] cho bài '{title}' ({post_id})")

        if updated:
            service.posts().patch(blogId=blog_id, postId=post_id, body={'content': content}).execute()
            print(f"  -> Cập nhật bài '{title}' thành công!")
        else:
            print(f"  [OK] Bài '{title}' đã chuẩn [tintuc] và link ảnh.")
    except Exception as e:
        print(f"Lỗi khi xử lý bài {post_id}: {e}")

print("Hoàn tất kiểm tra!")

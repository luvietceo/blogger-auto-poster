# 🚀 Blogger Gemini AI Auto-Poster Cloud 24/7 (Đám Mây Tự Động Hóa)
## Nền Tảng Tự Động Hóa Viết Bài Chuẩn SEO & Lên Lịch Đăng Blogger Đa Ngành Nghề

Hệ thống **Blogger Gemini AI Auto-Poster Cloud** giúp tự động hóa 100% quy trình sản xuất nội dung website chất lượng cao: từ quét đề tài trên Google Sheets, gọi AI viết bài chuyên sâu 1.500 - 2.000 từ, tự tạo ảnh bìa 16:9 WebP chuẩn SEO, bọc shortcode tương thích theme, đến lên lịch phát bài vào **4 Khung Giờ Vàng** mỗi ngày (`07:00`, `11:00`, `15:00`, `19:00`) và cập nhật ngược lại Google Sheets / Telegram.

> 🌟 **Áp dụng linh hoạt cho MỌI LOẠI WEBSITE:** Điện máy, Bất động sản, Spa / Thẩm mỹ, Thời trang, Đồ gia dụng, Dịch vụ Doanh nghiệp, Du lịch, B2B...

---

## ⚡ Điểm Nổi Bật Của Hệ Thống

* 🧠 **Bộ não AI Google Gemini 2.5 / Flash:** Viết bài tiếng Việt tự nhiên, giàu trải nghiệm thực chiến, cấu trúc H2/H3 chặt chẽ, Bảng so sánh thông số kỹ thuật (HTML `<table>`), FAQ Schema chuẩn SEO và Khối Call-To-Action (CTA) dẫn khách về Zalo / Website.
* 🕒 **Lên lịch tự động 4 Khung Giờ Vàng:** Đăng đều đặn vào `07:00`, `11:00`, `15:00`, `19:00` (Giờ Việt Nam). Hỗ trợ chạy theo mẻ 10 bài/ngày trải đều liên tục không trùng slot.
* 🖼️ **Thumbnail 16:9 WebP Siêu Nén:** Tự động tạo ảnh bìa chất lượng cao bám sát nội dung, tối ưu chuẩn Google Core Web Vitals và lưu trữ CDN vĩnh viễn trên GitHub.
* 🎨 **Tương thích 100% Theme Blogspot:** Tự động bao bọc shortcode `[tintuc]...[/tintuc]` giúp bài viết hiển thị hoàn hảo trên tất cả các template Bizweb / Sapo / Blogspot.
* 📊 **Đồng bộ 2 Chiều Google Sheets & Webhook Apps Script:** Tự động đổi trạng thái sang "Đã đăng", bôi xanh dòng và điền trực tiếp link bài viết Blogger vào Google Sheet theo thời gian thực.
* 🔑 **Xoay Vòng API Key (Key Pool):** Hỗ trợ nhiều key Gemini (`GEMINI_API_KEY_1`, `GEMINI_API_KEY_2`...) tự động đảo key khi gặp giới hạn hạn ngạch (Quota limit).
* ☁️ **100% Miễn Phí Trọn Đời:** Hoạt động hoàn toàn trên GitHub Actions, không cần thuê máy chủ VPS hay bật máy tính cá nhân.

---

## 📁 Cấu Trúc Thư Mục

```text
blogger-auto-poster/
├── .github/workflows/
│   └── auto_post.yml              # Kịch bản tự động hóa đám mây GitHub Actions
├── main.py                        # Bộ máy chính: Quét đề tài, gọi Gemini AI, bọc [tintuc], đăng Blogger
├── generate_executive_thumbnail.py# Engine dựng ảnh Thumbnail 16:9 WebP chuẩn SEO
├── google_sheets_webhook.js       # Webhook Google Apps Script tự cập nhật 2 chiều Google Sheets
├── get_refresh_token.py           # Công cụ lấy Google Refresh Token tự động trong 30 giây
├── fix_all_posts.py               # Script hỗ trợ bọc [tintuc] và chuẩn hóa link ảnh cho các bài cũ
├── topics.txt                     # Danh sách đề tài dự phòng khi không dùng Google Sheets
├── posted_history.json            # Nhật ký lịch sử bài viết đã đăng (chống trùng lặp 100%)
├── thumbnails/                    # Thư mục lưu trữ ảnh Thumbnail WebP được đẩy lên GitHub CDN
├── HUONG_DAN_CAI_DAT_CHO_NGUOI_MOI.md # Sổ tay hướng dẫn cài đặt chi tiết từ A đến Z cho người mới
└── requirements.txt               # Danh sách thư viện Python cần thiết
```

---

## 📖 Hướng Dẫn Cài Đặt Chi Tiết

👉 **Xem hướng dẫn từng bước đầy đủ nhất tại:** [**`HUONG_DAN_CAI_DAT_CHO_NGUOI_MOI.md`**](file:///c:/Users/Admin/Downloads/Blogger_Auto_Cloud_Tron_Goi/HUONG_DAN_CAI_DAT_CHO_NGUOI_MOI.md)

### Tóm tắt 5 bước cài đặt nhanh:

1. **Chuẩn bị Blog Blogger:** Tạo blog tại [blogger.com](https://www.blogger.com) ➔ Bật **Nội dung mô tả tìm kiếm** ➔ Đổi múi giờ sang **(GMT+07:00) Hà Nội**. Lấy `BLOGGER_BLOG_ID`.
2. **Lấy Gemini API Key:** Đăng ký miễn phí tại [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
3. **Lấy OAuth Refresh Token:** Tạo OAuth Client ID trên [Google Cloud Console](https://console.cloud.google.com/) ➔ Chạy `python get_refresh_token.py` để lấy `GOOGLE_REFRESH_TOKEN`.
4. **Tạo Google Sheet & Apps Script Webhook:**
   * Tạo bảng tính gồm 9 cột: *STT, Tiêu Đề, Từ Khóa, Nhãn, Gợi Ý, Link CTA, Trạng Thái, Ngày Lên Lịch, Link Bài Viết*.
   * Chia sẻ quyền: *Bất kỳ ai có liên kết đều có thể xem*.
   * Cài file `google_sheets_webhook.js` vào Apps Script ➔ Triển khai Web App quyền *Anyone* để lấy URL Webhook `/exec`.
5. **Cài GitHub Repository & Secrets:**
   * Tạo repository trên GitHub ở chế độ **PUBLIC** *(bắt buộc Public để ảnh Thumbnail WebP hiển thị)*.
   * Thêm các thông số vào **Settings ➔ Secrets and variables ➔ Actions**.
   * Bật quyền **Read and write permissions** trong **Actions ➔ General**.
   * Vào tab **Actions** ➔ Bấm **Run workflow** để hệ thống tự động bắt đầu viết bài!

---

## ⚙️ Bảng Tham Số GitHub Secrets

| Tên Secret | Ý Nghĩa | Bắt Buộc |
| :--- | :--- | :---: |
| `GEMINI_API_KEY` | Khóa Google Gemini AI chính | ✅ |
| `GEMINI_API_KEY_1`, `2` | Khóa Gemini dự phòng (xoay tua chống hết hạn ngạch) | Tùy chọn |
| `BLOGGER_BLOG_ID` | Dãy số ID của blog Blogger | ✅ |
| `GOOGLE_CLIENT_ID` | Client ID Google Cloud OAuth | ✅ |
| `GOOGLE_CLIENT_SECRET` | Client Secret Google Cloud OAuth | ✅ |
| `GOOGLE_REFRESH_TOKEN` | Token cấp quyền xuất bản vĩnh viễn | ✅ |
| `GOOGLE_SHEET_URL` | Link bảng tính đề tài Google Sheets | ✅ |
| `GOOGLE_SHEET_WEBHOOK_URL` | Link Web App Apps Script `/exec` | ✅ |
| `TELEGRAM_BOT_TOKEN` | Token bot Telegram nhận thông báo | Tùy chọn |
| `TELEGRAM_CHAT_ID` | ID nhóm/người dùng Telegram nhận báo cáo | Tùy chọn |

---

## 💡 Tùy Biến Cho Website & Ngành Nghề Khác

Để đổi ngành nghề (ví dụ từ Điện máy sang Bất động sản, Mỹ phẩm, Du lịch...), bạn chỉ cần:
1. **Google Sheets:** Nhập các tiêu đề và từ khóa của ngành nghề bạn muốn làm vào cột Tiêu đề & Từ khóa.
2. **File `main.py`:**
   * Đổi URL website, Zalo, Fanpage tại dòng `155`.
   * Tùy chỉnh phần vai trò chuyên gia trong Prompt AI (`generate_seo_article()`) tại dòng `255`.
   * Đổi khung giờ tại `GOLDEN_SLOTS` (dòng `115`) nếu muốn giờ đăng khác.
3. Commit và Push lên GitHub ➔ Hệ thống sẽ tự động cập nhật và viết bài theo phong cách mới!

---

*Hệ thống được phát triển và tối ưu hóa bởi Trợ Lý AI Chuyên Sâu.*

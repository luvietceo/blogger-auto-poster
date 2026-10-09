# 🌐 HƯỚNG DẪN CÀI ĐẶT & TRIỂN KHAI TRỌN GÓI HỆ THỐNG BLOGGER AUTO CLOUD
## Áp Dụng Cho Mọi Website & Ngành Nghề (Điện Máy, Bất Động Sản, Spa, Thời Trang, Dịch Vụ, B2B...)

> 💡 **Dành cho mọi đối tượng:** Tài liệu này được biên soạn theo nguyên tắc "Cầm tay chỉ việc", từng bước chi tiết từ A đến Z. Dù bạn là chủ shop, marketer, SEOer hay người mới bắt đầu chưa từng lập trình, bạn đều có thể tự tay đưa cỗ máy viết bài tự động này lên Cloud hoạt động 24/7 chỉ sau **10 - 15 phút**!

---

## 📑 MỤC LỤC HƯỚNG DẪN

1. [Tổng Quan Kiến Trúc & Nguyên Lý Hoạt Động](#1-tổng-quan-kiến-trúc--nguyên-lý-hoạt-động)
2. [Bước 1: Chuẩn Bị Trang Blogger & 2 Cài Đặt SEO Bắt Buộc](#bước-1-chuẩn-bị-trang-blogger--2-cài-đặt-seo-bắt-buộc)
3. [Bước 2: Lấy Google Gemini API Key (Key Pool Đa Tầng)](#bước-2-lấy-google-gemini-api-key-key-pool-đa-tầng)
4. [Bước 3: Tạo Google Cloud OAuth & Lấy Refresh Token Đăng Bài](#bước-3-tạo-google-cloud-oauth--lấy-refresh-token-đăng-bài)
5. [Bước 4: Tạo Kho Đề Tài Google Sheets & Cài Webhook 2 Chiều](#bước-4-tạo-kho-đề-tài-google-sheets--cài-webhook-2-chiều)
6. [Bước 5: Tùy Biến Thương Hiệu & Nội Dung Theo Ngành Nghề Của Bạn](#bước-5-tùy-biến-thương-hiệu--nội-dung-theo-ngành-nghề-của-bạn)
7. [Bước 6: Triển Khai Đám Mây GitHub Actions 24/7 (Miễn Phí Trọn Đời)](#bước-6-triển-khai-đám-mây-github-actions-247-miễn-phí-trọn-đời)
8. [Bước 7: Kiểm Tra Vận Hành & Khắc Phục Sự Cố Thường Gặp](#bước-7-kiểm-tra-vận-hành--khắc-phục-sự-cố-thường-gặp)

---

## 🌟 1. TỔNG QUAN KIẾN TRÚC & NGUYÊN LÝ HOẠT ĐỘNG

Hệ thống **Blogger Auto Cloud** là giải pháp tự động hóa nội dung toàn diện, kết nối các dịch vụ đám mây hàng đầu thế giới:

```mermaid
graph TD
    A[Google Sheets: Kho 100-500 Đề Tài] -->|Đọc Đề Tài & Từ Khóa| B[GitHub Actions Cloud Runner]
    B -->|Gọi AI Viết Bài Chuẩn SEO| C[Google Gemini AI 2.5/Flash]
    B -->|Tự Động Sinh Thumbnail 16:9 WebP| D[GitHub Raw CDN]
    C -->|Bọc Shortcode [tintuc] & Format HTML| B
    B -->|Xuất Bản / Lên Lịch Khung Giờ Vàng| E[Blogger API v3]
    E -->|Trả Về URL Bài Viết| B
    B -->|Gửi Webhook HTTP POST| F[Google Apps Script]
    F -->|Đổi Trạng Thái 'Đã Đăng' & Điền Link| A
    B -->|Gửi Báo Cáo Thời Gian Thực| G[Telegram Bot & Email]
```

### ✨ Ưu điểm vượt trội:
* **Hoàn toàn miễn phí trọn đời:** Chạy trên GitHub Actions với 2.000 phút miễn phí/tháng, không tốn tiền mua máy chủ VPS hay Hosting.
* **Tự động đăng vào 4 Khung Giờ Vàng:** `07:00`, `11:00`, `15:00`, `19:00` (Giờ Việt Nam).
* **Bài viết đỉnh cao chuẩn SEO & CRO:** Độ dài 1.500 - 2.000 từ, cấu trúc thẻ Heading H2/H3, Bảng so sánh thông số kỹ thuật (HTML `<table>`), FAQ Schema giải đáp thắc mắc, khối Call To Action (CTA) dẫn khách về Zalo / Hotline / Website.
* **Tự động bọc shortcode `[tintuc]...[/tintuc]`:** Tương thích 100% với tất cả theme Blogspot (Bizweb, Sapo, Blogspot thương mại điện tử...).
* **Đồng bộ 2 chiều với Google Sheets:** Bài nào đăng xong tự động đổi màu xanh, điền ngày giờ hẹn và chèn link bài viết trực tiếp vào bảng tính. Không bao giờ bị đăng trùng bài!

---

## 📝 BƯỚC 1: CHUẨN BỊ TRANG BLOGGER & 2 CÀI ĐẶT SEO BẮT BUỘC

### 1.1. Tạo Blog mới (Nếu chưa có)
1. Truy cập: [blogger.com](https://www.blogger.com) và đăng nhập bằng tài khoản Gmail của bạn.
2. Bấm **Tạo blog (Create Blog)**:
   * **Tiêu đề:** Tên website / thương hiệu của bạn (Ví dụ: *Điện Máy Gia Dụng Mava*, *Bất Động Sản Nhà Phố*...).
   * **Địa chỉ URL:** Chọn tên miền con miễn phí (Ví dụ: `mava-dienmay.blogspot.com`). Về sau bạn có thể trỏ tên miền riêng (`.com`, `.vn`) hoàn toàn dễ dàng.
   * **Tên hiển thị:** Tên tác giả hiển thị dưới bài viết.

### 1.2. 2 Cài đặt SEO sống còn trên Blogger (BẮT BUỘC PHẢI BẬT)
Nếu không bật 2 mục này, bài viết AI sẽ bị mất mô tả tìm kiếm và bị lệch giờ đăng:
1. **Bật Thẻ Meta Mô Tả Tìm Kiếm (Search Description):**
   * Vào menu bên trái ➔ Chọn **Cài đặt (Settings)**.
   * Cuộn xuống mục **Thẻ meta (Meta tags)**.
   * **BẬT công tắc:** `Bật nội dung mô tả tìm kiếm (Enable search description)`.
   * Nhập mô tả chung cho blog (dưới 150 ký tự) ➔ Bấm **Lưu**.
2. **Cài Đặt Múi Giờ Việt Nam (GMT+07:00):**
   * Trong mục Cài đặt ➔ Cuộn xuống phần **Định dạng (Formatting)**.
   * Bấm vào **Múi giờ (Time zone)** ➔ Chọn chính xác: `(GMT+07:00) Giờ Đông Dương (Hà Nội, Băng Cốc, Jakarta)`.
   * Bấm **Lưu**.

### 1.3. Lấy `BLOGGER_BLOG_ID`
* Khi bạn đang ở trang quản trị Blog (`blogger.com`), hãy nhìn lên thanh địa chỉ (URL) của trình duyệt:
  ```text
  https://www.blogger.com/blog/posts/2831151491518297988
  ```
* Dãy số nằm ngay sau chữ `/posts/` chính là **`BLOGGER_BLOG_ID`** của bạn. Hãy lưu lại dãy số này!

---

## 🔑 BƯỚC 2: LẤY GOOGLE GEMINI API KEY (KEY POOL ĐA TẦNG)

Hệ thống hỗ trợ cơ chế **Key Pool Rotation** (Xoay vòng nhiều API Key). Nếu Key 1 hết hạn ngạch (quota limit) hoặc bị lỗi tạm thời, bot sẽ tự động chuyển sang Key 2, Key 3 mà tiến trình không bao giờ bị dừng!

1. Truy cập: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
2. Đăng nhập tài khoản Google của bạn.
3. Bấm nút màu xanh **Create API Key** (hoặc *Get API key*).
4. Chọn **Create API key in new project**.
5. Sao chép chuỗi mã bắt đầu bằng `AIzaSy...`.
6. *(Khuyên dùng)* Bạn có thể tạo từ **2 đến 3 API Key** trên các project khác nhau để dự phòng:
   * Key 1: Lưu vào `GEMINI_API_KEY` (hoặc `GEMINI_API_KEY_1`)
   * Key 2: Lưu vào `GEMINI_API_KEY_2`
   * Key 3: Lưu vào `GEMINI_API_KEY_3`

---

## 🔐 BƯỚC 3: TẠO GOOGLE CLOUD OAUTH & LẤY REFRESH TOKEN ĐĂNG BÀI

Để bot có quyền đăng bài tự động lên Blogger thay bạn 24/7 mà không cần bạn phải ngồi duyệt, chúng ta cần tạo Google OAuth Client ID:

### 3.1. Tạo Project & Bật Blogger API v3 trên Google Cloud
1. Truy cập: [console.cloud.google.com](https://console.cloud.google.com/).
2. Tạo một Project mới (đặt tên ví dụ: `Blogger-Auto-Bot`).
3. Vào menu **APIs & Services (API và Dịch vụ)** ➔ **Library (Thư viện)**.
4. Tìm kiếm từ khóa `Blogger API v3` ➔ Bấm vào và chọn nút **Enable (Bật)**.

### 3.2. Cấu hình Màn hình chấp thuận OAuth (OAuth Consent Screen)
1. Vào menu **APIs & Services** ➔ **OAuth consent screen (Màn hình chấp thuận OAuth)**.
2. Chọn loại người dùng: **External (Bên ngoài)** ➔ Bấm **Create**.
3. Điền các trường cơ bản:
   * **App name:** `Blogger Auto Poster`
   * **User support email:** Chọn email của bạn.
   * **Developer contact information:** Nhập lại email của bạn.
   * Bấm **Save and continue** qua các bước Scopes.
4. Tại bước **Test users (Người dùng thử nghiệm)**:
   * Bấm **+ Add users** ➔ Nhập chính địa chỉ Gmail sở hữu trang Blogger của bạn ➔ Bấm **Save**.

### 3.3. Tạo Client ID & Client Secret
1. Vào menu **Credentials (Thông tin xác thực)** ➔ Bấm **+ Create Credentials (+ Tạo thông tin xác thực)** ➔ Chọn **OAuth client ID**.
2. Mục **Application type (Loại ứng dụng)**: Chọn **Desktop app (Ứng dụng cho máy tính)** hoặc **Web application**.
   * *Nếu chọn Web application:* Thêm URI chuyển hướng được ủy quyền: `http://localhost:8080/` và `https://developers.google.com/oauthplayground`.
3. Bấm **Create (Tạo)**.
4. Hệ thống sẽ hiển thị:
   * **Client ID:** Dạng `xxxxxx.apps.googleusercontent.com`
   * **Client Secret:** Dạng `GOCSPX-xxxxxx`
   * 👉 Hãy sao chép 2 thông số này lại!

### 3.4. Lấy `GOOGLE_REFRESH_TOKEN` tự động (Chỉ mất 30 giây)
Trong thư mục mã nguồn đã có sẵn script lấy token tự động:
1. Mở Terminal / PowerShell trong thư mục dự án và chạy:
   ```bash
   python get_refresh_token.py
   ```
2. Dán `Client ID` và `Client Secret` của bạn vào khi được hỏi.
3. Trình duyệt trên máy tính sẽ tự động bật lên ➔ Đăng nhập Gmail sở hữu Blogger.
4. Nếu thấy cảnh báo "Google chưa xác minh ứng dụng này" ➔ Bấm **Nâng cao (Advanced)** ➔ Chọn **Đi tới ... (Không an toàn)** ➔ Tích chọn quyền quản trị Blogger ➔ Bấm **Cho phép (Allow)**.
5. Màn hình console sẽ xuất ra chuỗi mã bắt đầu bằng: `1//0...`
   👉 Đó chính là **`GOOGLE_REFRESH_TOKEN`** của bạn! Mã này có giá trị vĩnh viễn.

---

## 📊 BƯỚC 4: TẠO KHO ĐỀ TÀI GOOGLE SHEETS & CÀI WEBHOOK 2 CHIỀU

### 4.1. Cấu trúc Bảng Tính Google Sheets Chuẩn (9 Cột)
Tạo một Google Sheet mới với các tiêu đề cột tại dòng 1 như sau:

| Cột | Tên Cột (Header) | Ý Nghĩa | Ví Dụ |
| :---: | :--- | :--- | :--- |
| **A** | `STT` | Số thứ tự bài viết | `1`, `2`, `3`... |
| **B** | `Tiêu Đề Bài Viết (Blogger Title)` | Đề tài hoặc tiêu đề chính | `Top 5 Tủ Lạnh Inverter Tiết Kiệm Điện 2026` |
| **C** | `Từ Khóa Chính (Focus Keyword)` | Từ khóa SEO trọng tâm | `tủ lạnh inverter, tủ lạnh tiết kiệm điện` |
| **D** | `Nhãn Chuyên Mục (Labels)` | Nhãn phân loại trên Blogspot | `tin-tuc, tu-van-chon-mua` |
| **E** | `Gợi Ý Nội Dung / Góc Nhìn` | Gợi ý ý tưởng để AI bám sát | `Đánh giá các dòng Panasonic, LG, so sánh giá` |
| **F** | `Link Đích CTA` | Link Zalo/Hotline/Sản phẩm | `https://zalo.me/1501073926693571291` |
| **G** | `Trạng Thái` | Trạng thái xuất bản | Để trống hoặc ghi `Chưa đăng` |
| **H** | `Ngày Lên Lịch / Đăng` | Bot tự điền ngày giờ hẹn | *(Bot tự điền sau khi đăng)* |
| **I** | `Link Bài Viết (URL)` | Bot tự điền link Blogger | *(Bot tự điền sau khi đăng)* |

> ⚠️ **BẮT BUỘC BẬT QUYỀN CHIA SẺ:**
> Nhấn nút **Chia sẻ (Share)** ở góc trên bên phải Google Sheet ➔ Tại mục *Quyền truy cập chung*, chuyển thành **"Bất kỳ ai có đường liên kết đều có thể xem" (Anyone with the link can view)** ➔ Sao chép đường link Google Sheets này làm biến **`GOOGLE_SHEET_URL`**.

### 4.2. Cài đặt Webhook Google Apps Script (Tự động đổi màu & điền link)
1. Trên Google Sheets của bạn ➔ Bấm vào menu **Tiện ích mở rộng (Extensions)** ➔ Chọn **Apps Script**.
2. Xóa hết code mặc định, mở file [`google_sheets_webhook.js`](file:///c:/Users/Admin/Downloads/Blogger_Auto_Cloud_Tron_Goi/google_sheets_webhook.js) trong bộ mã nguồn và **sao chép toàn bộ code dán vào**.
3. Bấm biểu tượng **Lưu (Ctrl + S)**.
4. Bấm nút màu xanh **Triển khai (Deploy)** ở góc trên bên phải ➔ Chọn **Bản triển khai mới (New deployment)**.
5. Bấm vào biểu tượng bánh răng ⚙️ bên cạnh chữ *Chọn loại* ➔ Chọn **Ứng dụng web (Web app)**:
   * **Mô tả:** `Blogger Webhook Auto`
   * **Thực thi dưới dạng (Execute as):** `Tôi (Email của bạn)`
   * **Ai có quyền truy cập (Who has access):** Chọn **Bất kỳ ai (Anyone)** *(Rất quan trọng, phải chọn Anyone thì GitHub Actions mới gửi dữ liệu vào được)*.
6. Bấm **Triển khai (Deploy)** ➔ Bấm **Ủy quyền truy cập (Authorize access)** ➔ Chọn Gmail ➔ Bấm **Nâng cao ➔ Đi tới... ➔ Cho phép**.
7. Sao chép đường link Web App có đuôi kết thúc bằng **`/exec`**.
   👉 Đây chính là **`GOOGLE_SHEET_WEBHOOK_URL`** của bạn!

---

## 🎨 BƯỚC 5: TÙY BIẾN THƯƠNG HIỆU & NỘI DUNG THEO NGÀNH NGHỀ

Để áp dụng cho **bất kỳ website nào**, bạn chỉ cần mở file [`main.py`](file:///c:/Users/Admin/Downloads/Blogger_Auto_Cloud_Tron_Goi/main.py) và điều chỉnh 3 vị trí sau:

### 5.1. Khung giờ đăng bài & Số lượng bài viết mỗi ngày
Tìm đến khoảng dòng `110` trong `main.py`:
```python
# Cấu hình số bài tạo mỗi lần (Mặc định 10 bài, lên lịch trải đều 4 bài/ngày)
POSTS_COUNT = int(os.environ.get('POSTS_COUNT', '10'))

# 4 Khung giờ vàng xuất bản bài mỗi ngày (Giờ Việt Nam UTC+7)
GOLDEN_SLOTS = [(7, 0), (11, 0), (15, 0), (19, 0)]
```
* Nếu muốn đổi giờ: Bạn chỉ cần sửa số trong `GOLDEN_SLOTS`. Ví dụ: `[(8, 0), (12, 0), (16, 0), (20, 0)]`.
* Khi hệ thống chạy tạo 10 bài, nó sẽ tự động lên lịch vào 4 khung giờ này của ngày 1 (4 bài), ngày 2 (4 bài), ngày 3 (2 bài) mà không bao giờ bị đè slot.

### 5.2. Thông tin thương hiệu & Kênh liên hệ
Tìm đến khoảng dòng `155` trong `main.py`:
```python
WEBSITE_URL = os.environ.get('WEBSITE_URL', 'https://tenmiencuaban.com/').strip()
ZALO_URL = os.environ.get('ZALO_URL', 'https://zalo.me/sdt-cua-ban').strip()
FANPAGE_URL = os.environ.get('FANPAGE_URL', 'https://facebook.com/trang-cua-ban').strip()
CTA_URL = os.environ.get('CTA_URL', ZALO_URL or WEBSITE_URL).strip()
```
*(Bạn cũng có thể cấu hình trực tiếp các biến này trong file `.env` hoặc GitHub Secrets mà không cần sửa code).*

### 5.3. Định vị Prompt AI theo chuyên môn ngành nghề
Tại hàm `generate_seo_article()` (khoảng dòng `255`), bạn có thể tinh chỉnh vai trò chuyên gia cho phù hợp:
* **Nếu làm Bất động sản:** *"Bạn là Chuyên gia Tư vấn Đầu tư Bất Động Sản & Quy Hoạch Nhà Đất hàng đầu Việt Nam..."*
* **Nếu làm Mỹ phẩm / Spa:** *"Bạn là Bác sĩ Da liễu & Chuyên gia Trị liệu Thẩm mỹ cao cấp..."*
* **Nếu làm Điện máy / Gia dụng:** *(Đã được cấu hình chuẩn sẵn Chuyên gia Cố vấn Kỹ thuật & Review Điện Máy Thông Minh)*.
* **Nếu làm Du lịch / Khách sạn:** *"Bạn là Chuyên gia Cẩm nang Du lịch, Review Trải nghiệm & Hướng dẫn viên kỳ cựu..."*

---

## 🚀 BƯỚC 6: TRIỂN KHAI ĐÁM MÂY GITHUB ACTIONS 24/7 (MIỄN PHÍ)

### 6.1. Đưa mã nguồn lên GitHub Repository
1. Đăng nhập [GitHub.com](https://github.com) ➔ Tạo Repository mới (Ví dụ: `blogger-auto-poster`).
2. > ⚠️ **CỰC KỲ QUAN TRỌNG: CHỌN CHẾ ĐỘ "PUBLIC"**
   > * Tại sao phải chọn **Public**? Vì hệ thống tự động sinh ảnh Thumbnail WebP chuẩn SEO lưu trong thư mục `thumbnails/`. GitHub sẽ đóng vai trò làm **máy chủ CDN lưu ảnh miễn phí**. Nếu để Private, link ảnh sẽ bị chặn 404 và không xem được trên website!
   > * *Về độ an toàn:* Toàn bộ API Key, Client Secret và Refresh Token được bảo mật tuyệt đối trong **GitHub Secrets**, file cấu hình máy tính `.env` đã được chặn không bị đẩy lên, do đó để Public mã nguồn hoàn toàn an toàn 100%!
3. Tải toàn bộ mã nguồn dự án lên repository của bạn bằng Git:
   ```bash
   git init
   git remote add origin https://github.com/<tai-khoan-github>/<ten-repo>.git
   git branch -M main
   git add .
   git commit -m "🚀 Khởi tạo hệ thống Blogger Auto Cloud"
   git push -u origin main
   ```

### 6.2. Cài đặt GitHub Secrets (Bảo mật thông tin đăng nhập)
1. Trên trang GitHub Repository của bạn, bấm vào tab **Settings** (ở trên thanh công cụ).
2. Ở cột menu bên trái, tìm mục **Secrets and variables** ➔ Chọn **Actions**.
3. Nhấn nút xanh **New repository secret** và lần lượt thêm các biến sau:

| Tên Secret (Bắt buộc viết hoa) | Giá Trị Cần Dán Vào |
| :--- | :--- |
| **`GEMINI_API_KEY`** | Khóa API Gemini chính (`AIzaSy...`) |
| **`GEMINI_API_KEY_1`** *(Tùy chọn)* | Khóa Gemini dự phòng 1 |
| **`GEMINI_API_KEY_2`** *(Tùy chọn)* | Khóa Gemini dự phòng 2 |
| **`BLOGGER_BLOG_ID`** | ID trang Blogspot (Dãy số ở Bước 1.3) |
| **`GOOGLE_CLIENT_ID`** | Client ID OAuth (Ở Bước 3.3) |
| **`GOOGLE_CLIENT_SECRET`** | Client Secret OAuth (Ở Bước 3.3) |
| **`GOOGLE_REFRESH_TOKEN`** | Token vĩnh viễn (Chuỗi `1//0...` ở Bước 3.4) |
| **`GOOGLE_SHEET_URL`** | Link chia sẻ Google Sheet (Ở Bước 4.1) |
| **`GOOGLE_SHEET_WEBHOOK_URL`** | Link Web App Apps Script `/exec` (Ở Bước 4.2) |
| **`TELEGRAM_BOT_TOKEN`** *(Tùy chọn)* | Token Bot Telegram nhận thông báo bài mới |
| **`TELEGRAM_CHAT_ID`** *(Tùy chọn)* | Chat ID Telegram cá nhân hoặc nhóm |

### 6.3. Cấp quyền Ghi (Write Permissions) cho GitHub Actions
Để GitHub Actions có quyền tự động lưu lịch sử bài đã đăng (`posted_history.json`) và lưu ảnh Thumbnail:
1. Vẫn trong trang **Settings** của repository trên GitHub.
2. Ở menu bên trái, cuộn xuống chọn mục **Actions** ➔ **General**.
3. Cuộn xuống cuối trang đến phần **Workflow permissions**:
   * Tích chọn vào ô: **`Read and write permissions`** (Cho phép đọc và ghi).
   * Bấm **Save (Lưu)**.

---

## 🎯 BƯỚC 7: KIỂM TRA VẬN HÀNH & KHẮC PHỤC SỰ CỐ

### 7.1. Chạy thử nghiệm ngay trên Web GitHub
1. Vào tab **Actions** trên thanh menu GitHub Repository của bạn.
2. Ở cột bên trái, bấm vào workflow: **`🚀 Blogger Gemini AI Auto-Poster Cloud`**.
3. Ở khung bên phải, bấm vào nút: **Run workflow**:
   * **Số lượng bài viết:** Chọn số lượng muốn tạo (ví dụ chọn `1` để thử nghiệm hoặc `10` để lên lịch cả mẻ).
   * **Chế độ phát hành:** Chọn `schedule` (hẹn giờ khung giờ vàng) hoặc `publish` (đăng ngay lập tức).
   * Bấm nút màu xanh **Run workflow**.
4. Chờ khoảng 1 - 2 phút, workflow sẽ chuyển sang màu xanh lá cây ✅:
   * Mở Google Sheet: Bạn sẽ thấy dòng đề tài tương ứng được tô màu xanh, điền ngày giờ hẹn và chèn link bài viết trực tiếp!
   * Mở Blogger / Website: Bài viết đã được tạo hoàn hảo với ảnh Thumbnail 16:9 sắc nét, bảng so sánh và nút liên hệ!

---

### 7.2. Bảng Tổng Hợp Khắc Phục Sự Cố Thường Gặp

| Hiện Tượng | Nguyên Nhân | Cách Khắc Phục Triệt Để |
| :--- | :--- | :--- |
| **Bài đăng lên web nhưng không hiển thị nội dung** | Theme Blogspot sử dụng shortcode `[tintuc]` để bóc tách hiển thị | Hệ thống đã tích hợp sẵn lệnh tự động bọc `[tintuc]{nội dung}[/tintuc]` trong `main.py`. Bạn không cần phải thao tác gì thủ công. |
| **Ảnh Thumbnail bị lỗi hình ảnh / 404** | Repository GitHub đang để ở chế độ Private | Vào GitHub Repository ➔ **Settings** ➔ Kéo xuống cuối mục **Danger Zone** ➔ Đổi sang **Change to public**. |
| **Google Sheet không cập nhật trạng thái "Đã đăng"** | Webhook Apps Script chưa cấp quyền "Anyone" | Mở Apps Script ➔ Triển khai lại ➔ Đảm bảo mục *Ai có quyền truy cập* chọn **Bất kỳ ai (Anyone)**. |
| **Gemini AI báo lỗi Resource Exhausted (429)** | Hết hạn ngạch gọi API miễn phí trong ngày | Thêm các key phụ `GEMINI_API_KEY_1`, `GEMINI_API_KEY_2` vào GitHub Secrets để bot tự xoay vòng. |
| **Bài hẹn giờ bị sai lệch múi giờ (đăng ban đêm)** | Blogger chưa chỉnh sang múi giờ GMT+07 | Vào Cài đặt Blogger ➔ Múi giờ ➔ Chọn đúng `(GMT+07:00) Hà Nội, Băng Cốc`. |

---

> 🎉 **Chúc mừng bạn!** Bạn đã sở hữu một cỗ máy tự động hóa nội dung đẳng cấp chuẩn SEO & CRO chạy hoàn toàn trên đám mây. Bạn chỉ việc thêm đề tài vào Google Sheet, mọi việc còn lại từ viết bài, dựng ảnh, gắn link đến xuất bản bài viết theo khung giờ vàng đều được AI và GitHub Actions xử lý tự động 100%!

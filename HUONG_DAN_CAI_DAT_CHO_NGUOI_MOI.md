# 🌐 HƯỚNG DẪN CÀI ĐẶT & TRIỂN KHAI TRỌN GÓI HỆ THỐNG BLOGGER AUTO CLOUD
## Áp Dụng Cho Mọi Website & Ngành Nghề (Điện Máy, Bất Động Sản, Spa, Thời Trang, Dịch Vụ, B2B...)

> 💡 **Dành cho mọi đối tượng:** Bạn hoàn toàn **KHÔNG CẦN BIẾT LẬP TRÌNH**! Hệ thống hỗ trợ 2 phương thức cài đặt:
> 1. 🌟 **Phương án 1 (Khuyên dùng số 1 - Siêu tốc & Tự động 100%):** Làm việc trực tiếp cùng **Trợ Lý AI (Google Antigravity / Claude Code / OpenAI Codex / Cursor)** — Bạn chỉ cần dán 1 câu lệnh khởi động, Trợ lý AI sẽ "cầm tay chỉ việc", tự động cấu hình, tự test và tự deploy cho bạn từ A đến Z!
> 2. 🛠️ **Phương án 2 (Dành cho Kỹ thuật viên / Dev):** Tự thao tác cấu hình thủ công từng bước theo bảng hướng dẫn kỹ thuật.

---

## 📑 MỤC LỤC HƯỚNG DẪN

1. [Tổng Quan Kiến Trúc & Nguyên Lý Hoạt Động](#1-tổng-quan-kiến-trúc--nguyên-lý-hoạt-động)
2. [🌟 PHƯƠNG ÁN 1: CÀI ĐẶT TỰ ĐỘNG CÙNG TRỢ LÝ AI (ANTIGRAVITY / CLAUDE / CODEX)](#-phương-án-1-cài-đặt-tự-động-cùng-trợ-lý-ai-antigravity--claude--codex)
3. [🛠️ PHƯƠNG ÁN 2: CÀI ĐẶT THỦ CÔNG TỪNG BƯỚC (DÀNH CHO DEV)](#️-phương-án-2-cài-đặt-thủ-công-từng-bước-dành-cho-dev)
   - [Bước 1: Chuẩn Bị Trang Blogger & 2 Cài Đặt SEO Bắt Buộc](#bước-1-chuẩn-bị-trang-blogger--2-cài-đặt-seo-bắt-buộc)
   - [Bước 2: Lấy Google Gemini API Key (Key Pool Đa Tầng)](#bước-2-lấy-google-gemini-api-key-key-pool-đa-tầng)
   - [Bước 3: Tạo Google Cloud OAuth & Lấy Refresh Token](#bước-3-tạo-google-cloud-oauth--lấy-refresh-token)
   - [Bước 4: Tạo Kho Đề Tài Google Sheets & Cài Webhook 2 Chiều](#bước-4-tạo-kho-đề-tài-google-sheets--cài-webhook-2-chiều)
   - [Bước 5: Tùy Biến Ngành Nghề & Thông Tin Thương Hiệu](#bước-5-tùy-biến-ngành-nghề--thông-tin-thương-hiệu)
   - [Bước 6: Triển Khai Đám Mây GitHub Actions 24/7](#bước-6-triển-khai-đám-mây-github-actions-247)
4. [Bảng Tra Cứu Khắc Phục Sự Cố Thường Gặp (Troubleshooting)](#bảng-tra-cứu-khắc-phục-sự-cố-thường-gặp)

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
* **Tự động lên lịch 4 Khung Giờ Vàng mỗi ngày:** `07:00`, `11:00`, `15:00`, `19:00` (Giờ Việt Nam). Hỗ trợ chạy batch 10 bài/ngày trải đều liên tục không trùng slot.
* **Bài viết đỉnh cao chuẩn SEO & CRO:** Độ dài 1.500 - 2.000 từ, cấu trúc thẻ Heading H2/H3, Bảng so sánh thông số kỹ thuật (HTML `<table>`), FAQ Schema giải đáp thắc mắc, khối Call To Action (CTA) dẫn khách về Zalo / Hotline / Website.
* **Tự động bọc shortcode `[tintuc]...[/tintuc]`:** Tương thích 100% với tất cả theme Blogspot (Bizweb, Sapo, Blogspot thương mại điện tử...).
* **Đồng bộ 2 chiều với Google Sheets:** Bài nào đăng xong tự động đổi màu xanh, điền ngày giờ hẹn và chèn link bài viết trực tiếp vào bảng tính. Không bao giờ bị đăng trùng bài!

---

## 🌟 PHƯƠNG ÁN 1: CÀI ĐẶT TỰ ĐỘNG CÙNG TRỢ LÝ AI (ANTIGRAVITY / CLAUDE / CODEX)
> 💡 **Khuyên dùng số 1 cho mọi người dùng**: Bạn không cần biết gõ lệnh terminal, không cần tự tạo file `.env`, không cần phải tự sửa code! Trợ lý AI sẽ đóng vai trò như một **Chuyên Viên Kỹ Thuật Riêng** ngồi cạnh bạn.

### 👉 Bước 1: Mở thư mục dự án trong Trợ lý AI
1. Tải về và giải nén thư mục `Blogger_Auto_Cloud_Tron_Goi`.
2. Mở một trong các công cụ Trợ lý AI sau:
   * **Google Antigravity IDE** *(Khuyên dùng số 1 - Tích hợp Gemini 2.5 siêu tốc)*
   * **Claude Code / Claude Desktop**
   * **Cursor IDE / Windsurf**
   * **OpenAI Codex / ChatGPT Web**
3. Chọn menu **File ➔ Open Folder... (Mở thư mục)** ➔ Chọn đúng thư mục `Blogger_Auto_Cloud_Tron_Goi`.
4. Nhấn tổ hợp phím **`Ctrl + L`** để mở khung chat với Trợ lý AI.

### 👉 Bước 2: Dán Câu Lệnh Khởi Động Duy Nhất Gửi Cho AI
Sao chép nguyên văn câu lệnh dưới đây (cũng có trong file `PROMPT_KHOI_DONG_AI.txt`) và dán vào khung chat với AI:

```text
Xin chào Trợ lý AI! Tôi muốn cài đặt hệ thống Blogger Auto Cloud cho website của mình.
Tôi không rành kỹ thuật. Hãy đọc file QUY_TRINH_TRO_LY_AI.md và hướng dẫn tôi theo đúng nguyên tắc "cầm tay chỉ việc, 1 bước 1 câu hỏi":
1. Đầu tiên hãy hỏi tôi về website của tôi (ngành nghề, tên miền web, Zalo/Hotline liên hệ).
2. Sau đó hướng dẫn tôi lấy từng thông số một (Blogger ID, Gemini API Key, Google Sheet, Google Cloud OAuth).
3. Bạn tự động tạo file .env, tự động cập nhật prompt và thông tin thương hiệu trong main.py theo đúng ngành nghề của tôi.
4. Bạn tự chạy script lấy Refresh Token, kiểm tra kết nối và xuất bản thử nghiệm 1 bài viết lên Blogger cho tôi.
5. Cuối cùng bạn hỗ trợ tôi đẩy lên GitHub Actions để bot tự chạy 24/7 hoàn toàn miễn phí trọn đời.
Bây giờ hãy bắt đầu ngay với Bước 1 nhé!
```

### 👉 Bước 3: Trải nghiệm thực tế - AI sẽ làm thay bạn như thế nào?
* **AI hỏi ngành nghề & thông tin:** Bạn chỉ cần nói *"Web tôi bán điện máy gia dụng, link mava.luviet.com, zalo 0987..."* hoặc *"Web tôi làm bất động sản..."*.
  ➔ **AI sẽ tự động:** Tinh chỉnh Prompt chuyên gia trong `main.py`, tạo khối CTA chuẩn màu sắc và thương hiệu của bạn!
* **AI hướng dẫn lấy ID & Key:** Mỗi lượt chat AI chỉ gửi 1 link duy nhất và chỉ rõ bấm vào đâu. Bạn gửi mã nào AI nhận mã đó.
* **AI kích hoạt lấy Token:** AI tự chạy lệnh, trình duyệt của bạn tự bật lên ➔ Bạn chỉ việc bấm **Cho phép (Allow)**.
* **AI tự tạo file `.env` & Chạy test:** AI tự ghi file cấu hình, tự gọi Gemini viết bài mẫu, tự động bọc thẻ `[tintuc]` và gửi link bài viết Blogger vừa đăng thành công ngay trong khung chat cho bạn xem!
* **AI tự đẩy lên GitHub Actions:** AI hỗ trợ bạn tạo repo **Public**, thiết lập các Secrets và kích hoạt lịch chạy tự động 4 khung giờ vàng mỗi ngày (`07:00, 11:00, 15:00, 19:00`).

---

## 🛠️ PHƯƠNG ÁN 2: CÀI ĐẶT THỦ CÔNG TỪNG BƯỚC (DÀNH CHO DEV)

---

### BƯỚC 1: CHUẨN BỊ TRANG BLOGGER & 2 CÀI ĐẶT SEO BẮT BUỘC

#### 1.1. Tạo Blog mới (Nếu chưa có)
1. Truy cập [blogger.com](https://www.blogger.com) và đăng nhập bằng Gmail của bạn.
2. Bấm **Tạo blog (Create Blog)** ➔ Đặt tiêu đề và chọn URL (ví dụ: `dienmay-mava.blogspot.com`).

#### 1.2. 2 Cài đặt SEO sống còn trên Blogger
1. **Bật Thẻ Meta Mô Tả Tìm Kiếm (Search Description):**
   * Vào **Cài đặt (Settings)** ➔ Cuộn xuống mục **Thẻ meta (Meta tags)**.
   * **BẬT công tắc:** `Bật nội dung mô tả tìm kiếm (Enable search description)` ➔ Nhập mô tả ngắn ➔ Bấm **Lưu**.
2. **Cài Đặt Múi Giờ Việt Nam (GMT+07:00):**
   * Trong **Cài đặt** ➔ Cuộn xuống **Định dạng (Formatting)** ➔ **Múi giờ (Time zone)**.
   * Chọn đúng: `(GMT+07:00) Giờ Đông Dương (Hà Nội, Băng Cốc, Jakarta)` ➔ Bấm **Lưu**.

#### 1.3. Lấy `BLOGGER_BLOG_ID`
* Nhìn lên thanh URL trình duyệt khi đang ở trang quản trị blog:
  `https://www.blogger.com/blog/posts/`**`2831151491518297988`**
* Dãy số sau chữ `/posts/` chính là **`BLOGGER_BLOG_ID`**.

---

### BƯỚC 2: LẤY GOOGLE GEMINI API KEY (KEY POOL ĐA TẦNG)

1. Truy cập: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
2. Đăng nhập Google ➔ Bấm nút xanh **Create API Key** ➔ Chọn **Create API key in new project**.
3. Sao chép chuỗi mã bắt đầu bằng `AIzaSy...`.
4. *(Khuyên dùng)* Tạo từ 2 đến 3 API Key trên các project Google Cloud khác nhau để làm Key Pool xoay vòng:
   * `GEMINI_API_KEY`: Key chính
   * `GEMINI_API_KEY_1`, `GEMINI_API_KEY_2`: Key phụ dự phòng chống nghẽn quota.

---

### BƯỚC 3: TẠO GOOGLE CLOUD OAUTH & LẤY REFRESH TOKEN

#### 3.1. Tạo Project & Bật Blogger API v3
1. Truy cập [console.cloud.google.com](https://console.cloud.google.com/) ➔ Tạo Project mới (ví dụ: `Blogger-Auto-Bot`).
2. Vào **APIs & Services** ➔ **Library** ➔ Tìm kiếm `Blogger API v3` ➔ Bấm **Enable (Bật)**.

#### 3.2. Cấu hình Màn hình chấp thuận OAuth
1. Vào **APIs & Services** ➔ **OAuth consent screen** ➔ Chọn **External** ➔ Bấm **Create**.
2. Điền App Name và Email của bạn ➔ Bấm Save qua các bước.
3. **Tại bước Test users:** Bấm **+ Add users** ➔ Nhập chính Gmail sở hữu Blog của bạn ➔ Bấm Save.
4. Quay lại màn hình chính OAuth consent screen, bấm nút **Publish App (Xuất bản ứng dụng)**.

#### 3.3. Tạo Client ID & Client Secret
1. Vào **Credentials** ➔ Bấm **+ Create Credentials** ➔ Chọn **OAuth client ID**.
2. Loại ứng dụng: Chọn **Desktop app** (hoặc Web application có redirect `http://localhost:8080/`).
3. Sao chép **Client ID** (`xxx.apps.googleusercontent.com`) và **Client Secret** (`GOCSPX-xxx`).

#### 3.4. Lấy Refresh Token tự động trong 30 giây
Mở terminal tại thư mục dự án và chạy:
```bash
python get_refresh_token.py
```
Dán Client ID và Client Secret vào ➔ Trình duyệt tự bật ➔ Chọn Gmail ➔ Bấm Nâng cao ➔ Cho phép.  
Màn hình sẽ in ra chuỗi mã bắt đầu bằng `1//0...` ➔ Đó là **`GOOGLE_REFRESH_TOKEN`** vĩnh viễn!

---

### BƯỚC 4: TẠO KHO ĐỀ TÀI GOOGLE SHEETS & CÀI WEBHOOK 2 CHIỀU

#### 4.1. Tạo Google Sheets Chuẩn 9 Cột
Tạo một Google Sheet mới với các tiêu đề cột tại dòng 1:

| Cột | Tên Cột (Header) | Ý Nghĩa |
| :---: | :--- | :--- |
| **A** | `STT` | Số thứ tự bài viết (`1`, `2`...) |
| **B** | `Tiêu Đề Bài Viết (Blogger Title)` | Đề tài hoặc tiêu đề chính |
| **C** | `Từ Khóa Chính (Focus Keyword)` | Từ khóa SEO trọng tâm |
| **D** | `Nhãn Chuyên Mục (Labels)` | Nhãn hiển thị (`tin-tuc`, `tu-van-chon-mua`...) |
| **E** | `Gợi Ý Nội Dung / Góc Nhìn` | Tóm tắt ý chính để AI bám sát |
| **F** | `Link Đích CTA` | Link Zalo/Hotline/Sản phẩm chuyển đổi |
| **G** | `Trạng Thái` | Trạng thái bài viết (`Chưa đăng`) |
| **H** | `Ngày Lên Lịch / Đăng` | Bot tự điền ngày giờ hẹn sau khi đăng |
| **I** | `Link Bài Viết (URL)` | Bot tự điền link bài Blogger sau khi đăng |

> ⚠️ **BẬT QUYỀN CHIA SẺ:** Bấm nút **Chia sẻ (Share)** ở góc trên bên phải ➔ Chuyển thành **"Bất kỳ ai có đường liên kết đều có thể xem" (Anyone with the link can view)** ➔ Copy link này làm biến **`GOOGLE_SHEET_URL`**.

#### 4.2. Cài đặt Webhook Google Apps Script
1. Trên Google Sheets ➔ Bấm menu **Tiện ích mở rộng (Extensions)** ➔ **Apps Script**.
2. Xóa code cũ, dán toàn bộ mã nguồn file [`google_sheets_webhook.js`](file:///c:/Users/Admin/Downloads/Blogger_Auto_Cloud_Tron_Goi/google_sheets_webhook.js) vào.
3. Bấm **Lưu (Ctrl + S)** ➔ Bấm **Triển khai (Deploy)** ➔ **Bản triển khai mới (New deployment)**.
4. Chọn loại **Ứng dụng web (Web app)**:
   * **Mô tả:** `Blogger Webhook Auto`
   * **Thực thi dưới dạng:** `Tôi (Email của bạn)`
   * **Ai có quyền truy cập:** Chọn **Bất kỳ ai (Anyone)** *(Bắt buộc chọn Anyone)*.
5. Bấm **Triển khai** ➔ Cấp quyền xác thực ➔ Copy link Web App có đuôi kết thúc bằng **`/exec`**.  
   👉 Đó là **`GOOGLE_SHEET_WEBHOOK_URL`** của bạn!

---

### BƯỚC 5: TÙY BIẾN NGÀNH NGHỀ & THÔNG TIN THƯƠNG HIỆU

Mở file [`main.py`](file:///c:/Users/Admin/Downloads/Blogger_Auto_Cloud_Tron_Goi/main.py) và cấu hình theo website của bạn:

1. **Khung giờ đăng & Số lượng bài (dòng `110`):**
   ```python
   POSTS_COUNT = int(os.environ.get('POSTS_COUNT', '10')) # Mặc định 10 bài/mẻ
   GOLDEN_SLOTS = [(7, 0), (11, 0), (15, 0), (19, 0)]    # 4 Khung giờ vàng/ngày
   ```
2. **Thông tin thương hiệu (dòng `155`):**
   ```python
   WEBSITE_URL = os.environ.get('WEBSITE_URL', 'https://website-cua-ban.com/').strip()
   ZALO_URL = os.environ.get('ZALO_URL', 'https://zalo.me/sdt-cua-ban').strip()
   FANPAGE_URL = os.environ.get('FANPAGE_URL', 'https://facebook.com/trang-cua-ban').strip()
   CTA_URL = os.environ.get('CTA_URL', ZALO_URL or WEBSITE_URL).strip()
   ```
3. **Định vị Prompt AI theo ngành nghề (dòng `255`):**
   * Tùy chỉnh vai trò chuyên gia tương ứng: Điện máy, Bất động sản, Spa, Du lịch, Thời trang...

---

### BƯỚC 6: TRIỂN KHAI ĐÁM MÂY GITHUB ACTIONS 24/7

#### 6.1. Tạo Repository GitHub ở chế độ PUBLIC
1. Truy cập [github.com](https://github.com) ➔ Tạo Repository mới.
2. > ⚠️ **BẮT BUỘC CHỌN CHẾ ĐỘ "PUBLIC":**
   > * Repository phải ở chế độ **Public** để ảnh Thumbnail WebP được load qua GitHub CDN vĩnh viễn miễn phí (không bị lỗi 404).
   > * *An toàn 100%:* Toàn bộ API Key, Client Secret và Refresh Token được lưu trong GitHub Secrets, file `.env` đã nằm trong `.gitignore` không bao giờ bị lộ lên GitHub.
3. Đẩy toàn bộ mã nguồn lên:
   ```bash
   git init
   git remote add origin https://github.com/<tai-khoan>/<ten-repo>.git
   git branch -M main
   git add .
   git commit -m "🚀 Triển khai Blogger Auto Cloud"
   git push -u origin main
   ```

#### 6.2. Cài đặt GitHub Secrets
Vào Repository trên GitHub ➔ **Settings** ➔ **Secrets and variables** ➔ **Actions** ➔ Bấm **New repository secret** và thêm:

| Tên Secret | Giá Trị |
| :--- | :--- |
| `GEMINI_API_KEY` | Mã API Key Gemini chính |
| `GEMINI_API_KEY_1`, `2` | Khóa Gemini dự phòng (xoay tua chống hết hạn ngạch) |
| `BLOGGER_BLOG_ID` | Dãy số ID của trang Blog Blogger |
| `GOOGLE_CLIENT_ID` | Client ID Google Cloud OAuth |
| `GOOGLE_CLIENT_SECRET` | Client Secret Google Cloud OAuth |
| `GOOGLE_REFRESH_TOKEN` | Token vĩnh viễn chuỗi `1//0...` |
| `GOOGLE_SHEET_URL` | Link Google Sheet chia sẻ công khai |
| `GOOGLE_SHEET_WEBHOOK_URL` | Link Web App Apps Script `/exec` |
| `TELEGRAM_BOT_TOKEN` *(Tùy chọn)* | Token bot Telegram nhận báo cáo |
| `TELEGRAM_CHAT_ID` *(Tùy chọn)* | Chat ID cá nhân/nhóm Telegram |

#### 6.3. Bật quyền Ghi (Write Permissions)
Vào **Settings** ➔ **Actions** ➔ **General** ➔ Cuộn xuống mục **Workflow permissions**:
* Tích chọn **`Read and write permissions`** ➔ Bấm **Save**.

#### 6.4. Chạy thử nghiệm trên GitHub Actions
Vào tab **Actions** ➔ Chọn **🚀 Blogger Gemini AI Auto-Poster Cloud** ➔ Bấm nút **Run workflow** ➔ Chờ 1 - 2 phút và thưởng thức thành quả bài viết tự động xuất bản chuẩn SEO lên website!

---

## 🛠️ BẢNG TRA CỨU KHẮC PHỤC SỰ CỐ THƯỜNG GẶP

| Hiện Tượng | Nguyên Nhân | Cách Khắc Phục Triệt Để |
| :--- | :--- | :--- |
| **Bài đăng lên blog nhưng bị ẩn, không hiện nội dung** | Theme Blogspot sử dụng shortcode `[tintuc]` để bóc tách hiển thị | Hệ thống đã tích hợp sẵn lệnh tự động bọc `[tintuc]{nội dung}[/tintuc]` trong `main.py`. Mọi bài đăng đều hiển thị 100%. |
| **Ảnh Thumbnail bị lỗi hình ảnh / 404** | Repository GitHub đang để ở chế độ Private | Vào GitHub Repository ➔ **Settings** ➔ Cuối mục **Danger Zone** ➔ Chọn **Change to public**. |
| **Google Sheet không tự đổi màu và không điền link** | Webhook Apps Script chưa cấp quyền "Anyone" | Mở Apps Script ➔ Triển khai lại ➔ Đảm bảo mục *Ai có quyền truy cập* chọn **Bất kỳ ai (Anyone)**. |
| **Gemini AI báo lỗi Resource Exhausted (429)** | Hết hạn ngạch gọi API miễn phí trong ngày | Thêm các key phụ `GEMINI_API_KEY_1`, `GEMINI_API_KEY_2` vào GitHub Secrets để bot tự xoay vòng. |
| **Bài hẹn giờ bị sai lệch múi giờ (đăng ban đêm)** | Blogger chưa chỉnh sang múi giờ GMT+07 | Vào Cài đặt Blogger ➔ Múi giờ ➔ Chọn đúng `(GMT+07:00) Hà Nội, Băng Cốc`. |

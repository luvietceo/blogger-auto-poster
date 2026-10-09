# 📖 HƯỚNG DẪN CÀI ĐẶT & SỬ DỤNG TRỌN GÓI DÀNH CHO NGƯỜI MỚI
## Cỗ Máy Tự Động Hóa Viết Bài Blogger Bằng Google Gemini AI

> 💡 **Dành cho mọi người**: Hướng dẫn này được viết cực kỳ chi tiết, từng bước dễ hiểu ngay cả khi bạn chưa từng biết lập trình. Bạn có thể tự mình cài đặt thành công chỉ sau 5 - 10 phút!

---

## 🌟 1. GIỚI THIỆU TỔNG QUAN

Hệ thống **Blogger Gemini AI Auto-Poster** giúp bạn tự động hóa 100% công việc làm nội dung website:
- 🧠 **Bộ não AI đỉnh cao**: Sử dụng Google Gemini AI để viết bài dài 1.500 - 2.500 từ chuẩn SEO chuyên sâu.
- 🎨 **Cấu trúc bài viết tối ưu CRO**: Tự động chia Heading `<h2>`, `<h3>`, bảng so sánh, mục FAQ Schema, hộp cam kết, nút kêu gọi hành động (Zalo, Hotline, Fanpage).
- 🖼️ **Tự động gắn Thumbnail chuẩn SEO**: Tự tạo ảnh bìa 16:9 sắc nét theo đúng chủ đề bài viết, nén WebP siêu nhẹ chuẩn Google Core Web Vitals.
- 💾 **Tự động lưu lịch sử**: Tránh tuyệt đối trùng lặp đề tài, tự động chuyển sang bài tiếp theo.
- 🚀 **2 Chế độ vận hành linh hoạt**:
  1. **Chạy trên máy tính cá nhân**: Bấm 1-Click bằng các file `.bat` tiện lợi.
  2. **Chạy trên đám mây GitHub Actions**: Tắt máy tính đi ngủ, hệ thống vẫn tự động thức dậy viết bài và đăng lên Blogger mỗi ngày hoàn toàn **MIỄN PHÍ TRỌN ĐỜI**!

---

## 🛠️ 2. HƯỚNG DẪN CÀI ĐẶT (CHỌN 1 TRONG 2 CÁCH)

---

### 🌟 LỰA CHỌN 1 (KHUYÊN DÙNG NHẤT): CÀI ĐẶT TỪNG BƯỚC CÙNG TRỢ LÝ AI (ANTIGRAVITY / CLAUDE / CODEX)
> 💡 **Dành cho người mới không rành kỹ thuật**: Bạn không cần biết gõ lệnh, không cần tự tạo file `.env`, và **không cần phải tự đi tìm gom mã khóa từ trước**! Trợ lý AI sẽ "cầm tay chỉ việc", hướng dẫn bạn lấy từng thông số một (1 bước - 1 câu hỏi), bạn gửi gì AI nhận nấy, rồi AI tự cấu hình, tự kiểm tra và deploy lên Cloud cho bạn từ A-Z!
> 
> 📖 **Xem cẩm nang chi tiết riêng:** [HUONG_DAN_LAM_VIEC_VOI_TRO_LY_AI.md](file:///d:/blogger-auto-cloud/HUONG_DAN_LAM_VIEC_VOI_TRO_LY_AI.md)

#### 👉 Bước 1: Mở thư mục dự án trong Trợ lý AI
- Mở **Google Antigravity** (hoặc Claude Code / Cursor / ChatGPT).
- Chọn **File ➔ Open Folder** ➔ Chọn thư mục `blogger-auto-cloud`.
- Nhấn tổ hợp phím **`Ctrl + L`** để mở khung chat với AI.

#### 👉 Bước 2: Sao chép câu lệnh "Khởi Động" gửi cho AI
Copy nguyên văn câu lệnh bên dưới (hoặc mở file `PROMPT_KHOI_DONG_AI.txt`) và dán vào khung chat với AI:

```text
Xin chào Trợ lý AI! Tôi muốn cài đặt hệ thống Blogger Auto Cloud. 
Tôi không rành kỹ thuật. Hãy đọc file QUY_TRINH_TRO_LY_AI.md và hướng dẫn tôi lấy từng thông số một theo đúng nguyên tắc "cầm tay chỉ việc, 1 bước 1 câu hỏi". 
Cứ mỗi bước bạn hướng dẫn tôi lấy 1 thông số, tôi gửi cho bạn, bạn nhận xong thì tự động tạo file .env, chạy kiểm tra và triển khai (deploy) giúp tôi. 
Bây giờ hãy bắt đầu ngay với Bước 1 nhé!
```

#### 👉 Bước 3: Làm theo từng câu hỏi của AI & Thư giãn
- AI sẽ hỏi bạn **Bước 1: Blogger ID** ➔ Bạn làm theo link AI chỉ, copy ID gửi lại.
- AI ghi nhận rồi hỏi tiếp **Bước 2: Gemini API Key**, **Bước 3: Google Sheets**, **Bước 4: Google Cloud OAuth**.
- Đến **Bước 5: Lấy Refresh Token**, trình duyệt máy bạn tự mở ➔ Bạn chỉ việc chọn Gmail, bấm **Nâng cao ➔ Chuyển đến ứng dụng ➔ Cho phép (Allow)**.
- AI sẽ tự động tạo file `.env`, tự chạy kiểm tra kết nối, tự xuất bản 1 bài viết mẫu chuẩn SEO lên Blogger và gửi link cho bạn xem ngay trong khung chat!
- AI sẽ hỗ trợ bạn cài đặt 6 Secrets lên GitHub Actions để bot tự chạy 24/7 trên mây hoàn toàn miễn phí trọn đời!

---

### 🖥️ LỰA CHỌN 2: CÀI ĐẶT TRUYỀN THỐNG BẰNG FILE .BAT TRÊN MÁY TÍNH

#### 📌 Bước 1: Chuẩn bị môi trường Python
1. Kiểm tra máy tính đã có Python chưa:
   - Nhấn phím `Windows + R`, gõ `cmd` rồi bấm Enter.
   - Gõ `python --version` rồi bấm Enter.
2. Nếu máy chưa có Python:
   - Truy cập trang chủ: [python.org/downloads](https://www.python.org/downloads/) và tải bản Python mới nhất (3.11 hoặc 3.12).
   - Khi chạy file cài đặt, **BẮT BUỘC TÍCH CHỌN** ô vuông:
     `☑ Add python.exe to PATH` (Ở góc dưới màn hình đầu tiên) rồi bấm **Install Now**.

#### 📌 Bước 2: Chạy file cài đặt tự động
1. Bấm đúp chuột (Double click) vào file: 👉 **`CAI_DAT.bat`**
2. Hệ thống sẽ tự động khởi tạo môi trường `venv`, cài thư viện `requirements.txt` và mở **Trợ lý Setup Wizard** bằng tiếng Việt.

#### 📌 Bước 3: Nhập thông số qua Trợ lý Setup Wizard
- Điền lần lượt `GEMINI_API_KEY`, `BLOGGER_BLOG_ID`, `GOOGLE_CLIENT_ID` & `GOOGLE_CLIENT_SECRET`.
- Khi Wizard hỏi mở trình duyệt lấy Refresh Token ➔ Bấm **Y** ➔ Trình duyệt tự mở ➔ Bạn bấm **Cho phép (Allow)** ➔ Token sẽ được tự động lưu vào file `.env`.

#### 📌 Bước 4: Kiểm tra & Chạy thử
- Mở file **`KIEM_TRA_KET_NOI.bat`**: Kiểm tra kết nối Gemini AI và Blogger API.
- Mở file **`CHAY_DANG_BAI.bat`**: Tự động lấy 1 đề tài, gọi AI viết bài, gắn ảnh Thumbnail chuẩn SEO và đăng ngay lên Blogger!

---

## 🔑 3. CÁCH LẤY CHI TIẾT CÁC THÔNG SỐ (DÀNH CHO TÀI KHOẢN MỚI TINH)

### 3.1. Thiết lập trang Blogger mới & 2 cài đặt SEO bắt buộc
1. **Tạo Blog mới (Nếu chưa có):**
   - Truy cập: [blogger.com](https://www.blogger.com) và đăng nhập bằng Gmail của bạn.
   - Nhập **Tiêu đề blog** (vd: *Tin Tức Doanh Nghiệp*) ➔ Nhập **Địa chỉ URL** (vd: `doanhnghiep2026.blogspot.com`) ➔ Nhập **Tên hiển thị** tác giả ➔ Bấm Hoàn tất.
2. **2 Cài đặt SEO sống còn trên Blogger (Bắt buộc):**
   - **Bật Thẻ Meta Mô Tả Tìm Kiếm:** Vào menu trái chọn **Cài đặt (Settings)** ➔ Cuộn xuống mục **Thẻ meta (Meta tags)** ➔ BẬT công tắc `Bật nội dung mô tả tìm kiếm (Enable search description)`. *(Nếu không bật, bài viết AI sẽ bị mất phần mô tả tóm tắt chuẩn SEO trên Google!).*
   - **Đổi Múi giờ Việt Nam (GMT+07:00):** Vẫn trong Cài đặt ➔ Cuộn xuống mục **Định dạng (Formatting)** ➔ Bấm vào **Múi giờ (Time zone)** ➔ Chọn `(GMT+07:00) Giờ Đông Dương (Hà Nội, Băng Cốc, Jakarta)`. *(Giúp bài hẹn giờ 06:30, 11:30, 14:30 xuất bản chính xác giờ vàng tại Việt Nam).*
3. **Lấy `BLOGGER_BLOG_ID`:**
   - Nhìn lên thanh địa chỉ (URL) của trình duyệt web:
     `https://www.blogger.com/blog/posts/`**`1234567891011121314`**
   - Dãy số phía sau chữ `posts/` chính là **BLOGGER_BLOG_ID** của bạn.

---

### 3.2. Lấy `GEMINI_API_KEY` (Chỉ mất 30 giây - Miễn phí)
1. Truy cập: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
2. Đăng nhập tài khoản Google. Nếu là lần đầu tiên, tích chọn đồng ý Điều khoản dịch vụ (Terms of Service) ➔ Bấm Continue.
3. Bấm nút xanh **Create API Key** (hoặc *Get API key*).
4. Chọn **Create API key in new project**.
5. Sao chép chuỗi mã bắt đầu bằng `AIzaSy...`. Đó chính là **GEMINI_API_KEY**.
> 💡 **Mẹo Key Pool:** Hạn ngạch miễn phí của Google là 15 yêu cầu/phút. Bạn có thể dùng 2 - 3 Gmail phụ tạo thêm key và dán cách nhau bằng dấu phẩy vào biến `GEMINI_API_KEYS` để hệ thống tự xoay vòng chống nghẽn!

---

### 3.3. Tạo `GOOGLE_CLIENT_ID` & `GOOGLE_CLIENT_SECRET` (Google Cloud)
1. **Tạo Project & Bật API:**
   - Truy cập **Google Cloud Console**: [console.cloud.google.com](https://console.cloud.google.com).
   - Bấm **Select a project** ➔ Bấm **New Project** ➔ Đặt tên (vd: `Blogger-Auto`) ➔ Bấm **Create**.
   - Vào ô tìm kiếm trên cùng gõ: **Blogger API v3** ➔ Bấm vào kết quả ➔ Bấm nút xanh **Enable (Bật)**.
2. **Cấu hình OAuth Consent Screen:**
   - Ở cột menu bên trái, vào **APIs & Services** ➔ **OAuth consent screen** (Màn hình đồng ý):
   - Chọn loại: **External** (Bên ngoài) ➔ Bấm **Create**.
   - Điền **App name** (vd: `Blogger Bot`) và chọn email của bạn ở các ô Email hỗ trợ và Email nhà phát triển ➔ Bấm **Save and continue**.
   - Mục Scopes: Bấm **Save and continue**.
   - **BƯỚC BẮT BUỘC Ở TEST USERS:** Bấm **+ Add users** ➔ Điền chính địa chỉ Gmail quản lý Blog của bạn vào ➔ Bấm **Save and continue**. *(Nếu không thêm, khi đăng nhập sẽ bị lỗi: Error 403: access_denied).*
3. **BÍ KÍP VÀNG: Bấm "Publish App" chống hết hạn Token sau 7 ngày:**
   - Theo chính sách của Google, nếu app ở trạng thái *Testing*, Refresh Token sẽ tự động hết hạn sau 7 ngày khiến bot bị lỗi `invalid_grant`.
   - **Cách giải quyết vĩnh viễn:** Trong màn hình **OAuth consent screen**, ngay dưới dòng *Publishing status*, bấm nút **PUBLISH APP (Xuất bản ứng dụng)** ➔ Bấm **Confirm (Xác nhận)**. Trạng thái chuyển sang *In production*. Token sẽ **TỒN TẠI VĨNH VIỄN KHÔNG BAO GIỜ HẾT HẠN**!
4. **Tạo Credentials (Thông tin xác thực):**
   - Ở cột menu bên trái, vào **Credentials**:
   - Bấm **+ Create Credentials** ➔ Chọn **OAuth client ID**.
   - Mục *Application type*: BẮT BUỘC CHỌN **Desktop App** (Ứng dụng cho máy tính để bàn).
   - Bấm **Create**. Google sẽ cấp cho bạn **Client ID** và **Client Secret**.

---

### 3.4. Lấy `GOOGLE_REFRESH_TOKEN` 1-Click (30 giây)
1. Mở file **`LAY_REFRESH_TOKEN.bat`** trên máy tính của bạn (hoặc để Setup Wizard tự chạy).
2. Dán Client ID và Client Secret vào.
3. Trình duyệt sẽ tự động mở trang đăng nhập Google.
4. **VƯỢT MÀN HÌNH BẢO MẬT CỦA GOOGLE:**
   - Google sẽ hiện cảnh báo: *"Google chưa xác minh ứng dụng này" (Google hasn't verified this app)*.
   - Bạn chỉ cần bấm vào chữ **Nâng cao (Advanced)** ở góc dưới bên trái ➔ Bấm vào liên kết **Chuyển đến [Tên App] (không an toàn)** ➔ Tích chọn ủy quyền quản trị Blogger ➔ Bấm **Tiếp tục / Cho phép (Allow)**.
5. Mã Refresh Token vĩnh viễn bắt đầu bằng `1//...` sẽ tự động được lấy và lưu vào file `.env`!

---

## ☁️ 4. ĐƯA LÊN ĐÁM MÂY GITHUB ACTIONS CHẠY 24/7 (KHÔNG CẦN BẬT MÁY TÍNH)

Khi đưa lên GitHub Actions, máy chủ đám mây của Microsoft/GitHub sẽ tự động thức dậy viết bài theo lịch hẹn:

### Bước 1: Tạo Repository trên GitHub
1. Đăng ký/Đăng nhập tại [GitHub.com](https://github.com).
2. Bấm nút **New** (Tạo repo mới):
   - Tên kho: `blogger-auto-cloud`
   - Chọn chế độ: **Private** (Riêng tư - để bảo mật dữ liệu của bạn).
   - Bấm **Create repository**.

### Bước 2: Tải code lên GitHub (Cách chuẩn & sạch 100%)
- **Cách khuyên dùng:** Bấm chạy file **`DONG_GOI_FILE_ZIP.bat`** (hoặc chọn mục số 9 trong `MENU_CHINH.bat`). Script sẽ tự động tạo file **`Blogger_Auto_Cloud_Tron_Goi.zip`** đã lọc sạch `venv` và file `.env` riêng tư. Bạn chỉ cần giải nén và tải lên GitHub!
- **LƯU Ý CỰC KỲ QUAN TRỌNG VỀ THƯ MỤC ẨN `.github`:**
  Trên Windows, thư mục `.github` là thư mục ẩn. Bạn BẮT BUỘC phải đảm bảo file `.github/workflows/auto_post.yml` được tải lên GitHub. Nếu thiếu thư mục này, tab Actions trên GitHub sẽ **trống trơn**!
- **TUYỆT ĐỐI KHÔNG TẢI LÊN:** Thư mục `venv` (nặng hàng trăm MB) và file `.env` (chứa khóa bí mật cá nhân).

### Bước 3: Cài đặt 5 Secrets bảo mật trên GitHub
1. Trên trang GitHub Repository của bạn, vào mục: **Settings** ➔ Cột trái chọn **Secrets and variables** ➔ Chọn **Actions**.
2. Bấm nút **New repository secret** màu xanh và lần lượt thêm 5 mục bắt buộc:

| Tên Secret | Giá trị cần dán |
| :--- | :--- |
| `GEMINI_API_KEY` | Mã AIzaSy... của bạn |
| `BLOGGER_BLOG_ID` | Dãy số Blog ID |
| `GOOGLE_CLIENT_ID` | Mã Client ID (.apps.googleusercontent.com) |
| `GOOGLE_CLIENT_SECRET` | Mã Client Secret (GOCSPX-...) |
| `GOOGLE_REFRESH_TOKEN` | Mã Refresh Token bắt đầu bằng 1//... |

*(Tùy chọn mở rộng: Thêm `GEMINI_API_KEYS` xoay tua key, `GOOGLE_SHEET_URL` quản lý đề tài từ Google Sheets, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` để nhận thông báo về điện thoại).*

### Bước 4: Cấp quyền ghi lịch sử cho GitHub Actions (BẮT BUỘC)
> 🚨 **BƯỚC QUAN TRỌNG NHẤT:** Mặc định GitHub Repo mới chỉ cấp quyền Read. Nếu không làm bước này, bot sẽ bị lỗi đỏ `403 Permission denied` khi tự động lưu file `posted_history.json`.

1. Vẫn trong tab **Settings** ➔ Cột trái chọn **Actions** ➔ **General**.
2. Cuộn xuống phần **Workflow permissions**:
   - Tích chọn: **Read and write permissions**.
3. Bấm **Save**.

### Bước 5: Khởi chạy thử nghiệm & Vận hành 24/7
1. Vào tab **Actions** trên GitHub. (Nếu thấy thông báo vàng, bấm "I understand my workflows, go ahead and enable them").
2. Chọn workflow: **🚀 Blogger Gemini AI Auto-Poster Cloud**.
3. Bấm nút **Run workflow** ➔ Chọn số lượng bài và chế độ ➔ Bấm nút xanh **Run workflow**.
4. Sau 20 - 40 giây, bạn sẽ thấy tiến trình hiện dấu tích xanh [✓]. Mở Blogger lên bài viết mới đã xuất hiện kèm thumbnail đẹp mắt!
5. **Lịch tự động:** Đám mây đã cài sẵn lịch cron tự động quét mỗi 20 phút để lên lịch đăng vào 3 Khung Giờ Vàng (06:30, 11:30, 14:30 Giờ Việt Nam) hoàn toàn miễn phí trọn đời!

---

## 📋 5. QUẢN LÝ ĐỀ TÀI & LỊCH SỬ BÀI ĐĂNG

### Cách 1: Thêm đề tài trong file `topics.txt`:
Mở file `topics.txt` bằng Notepad, thêm các dòng theo cú pháp:
```text
Tiêu đề hoặc từ khóa mục tiêu | Tóm tắt gợi ý | Nhãn 1, Nhãn 2 | Link CTA (tùy chọn)
```
Ví dụ:
```text
Bí quyết tối ưu chi phí quảng cáo Facebook ra đơn chuyển đổi cao 2026 | Chiến lược Facebook Ads tối ưu chi phí | Marketing, Facebook Ads
Chiến lược SEO tổng thể đưa từ khóa lên Top 1 Google bền vững | Hướng dẫn SEO lên top bền vững | Dịch Vụ SEO, Google
10 Bước xây dựng hệ thống website doanh nghiệp chuyên nghiệp | Quy trình chuẩn làm web | Thiết Kế Web, Kinh Doanh
```

### Cách 2 (Khuyên dùng nhất): Quản lý qua Google Sheets (Đồng bộ đám mây trực tiếp)
> 💡 **Tại sao nên dùng Google Sheets?** Bạn có thể mở ứng dụng Google Sheets trên điện thoại hoặc máy tính bất kỳ lúc nào để thêm hàng chục đề tài mới mà không cần chạm vào code. Bot trên GitHub Actions sẽ tự động vào đọc dòng chưa đăng và xuất bản 24/7!

#### 1. Mẫu Template Google Sheets Chuẩn (Tạo Bản Sao 1-Click):
> 🌟 **Dành cho người mới**: Bạn không cần phải tự gõ từng cột từ đầu. Hãy bấm vào link bên dưới, Google sẽ tự động sao chép bảng tính mẫu đã cài sẵn công thức AI tạo từ khóa và mô tả:
> 
> 👉 **[BẤM VÀO ĐÂY ĐỂ TẠO BẢN SAO TEMPLATE GOOGLE SHEETS (1-CLICK)](https://docs.google.com/spreadsheets/d/1VTsUaq33Wt-YBekNBUGS7pphOsJ7W4-ai5zwy9WEnkY/copy)**
> *(Hoặc xem trước bảng tính template gốc tại: [Template Google Sheets](https://docs.google.com/spreadsheets/d/1VTsUaq33Wt-YBekNBUGS7pphOsJ7W4-ai5zwy9WEnkY/edit?usp=sharing))*

Bảng tính gồm 9 cột chuẩn hóa từ Cột A đến Cột I:
| Cột | Tên Cột | Bắt buộc | Ý nghĩa & Hướng dẫn |
|:---:|:---|:---:|:---|
| **A** | `STT` | Không | Số thứ tự bài viết (1, 2, 3...) |
| **B** | `Tiêu Đề Bài Viết` | **BẮT BUỘC** | Tiêu đề bài viết SEO bạn muốn viết |
| **C** | `Từ Khóa SEO` | Không | Từ khóa trọng tâm để AI lồng ghép |
| **D** | `Nhãn Chuyên Mục` | Không | Nhãn trên Blogger, cách nhau bằng dấu phẩy (vd: `tin-tuc, dich-vu`) |
| **E** | `Gợi Ý Nội Dung` | Không | Dặn dò riêng cho Gemini về góc nhìn bài viết |
| **F** | `Link Đích CTA` | Không | Link nút kêu gọi hành động ở cuối bài |
| **G** | `Trạng Thái` | Tự động | Để trống hoặc ghi `Chờ đăng`. Bot đăng xong sẽ tự đổi thành **Đã đăng** hoặc **Đã lên lịch** |
| **H** | `Ngày Đăng` | Tự động | Bot tự động điền ngày giờ đăng bài |
| **I** | `Link Bài Viết` | Tự động | Bot tự động dán đường link bài viết hoàn chỉnh trên Blogger! |

#### 2. BẬT QUYỀN CHIA SẺ CÔNG KHAI (QUAN TRỌNG NHẤT):
- Mở bảng tính ➔ Bấm nút màu xanh **Chia sẻ (Share)** ở góc trên bên phải.
- Ở mục *Quyền truy cập chung (General access)*, đổi từ "Hạn chế" sang: **Bất kỳ ai có đường liên kết đều có thể xem (Anyone with the link can view)**.
- Bấm **Sao chép đường liên kết (Copy link)** ➔ Bấm Xong.
*(Nếu không bật quyền này, bot sẽ bị chặn lỗi 403 và không thể lấy bài đăng).*

#### 3. Cấu hình vào hệ thống:
- **Nếu chạy trên máy tính:** Dán link vào biến `GOOGLE_SHEET_URL` trong file `.env`.
- **Nếu chạy trên GitHub Actions:** Tạo Secret `GOOGLE_SHEET_URL` trong mục Settings ➔ Secrets của Repository.

#### 4. (Nâng cao) Cài Webhook tự động cập nhật ngược lại Google Sheets:
- Mở bảng tính ➔ Vào menu **Tiện ích mở rộng (Extensions)** ➔ Chọn **Apps Script**.
- Mở file `google_sheets_webhook.js` có sẵn trong thư mục dự án ➔ Sao chép toàn bộ code và dán vào Apps Script.
- Bấm **Lưu 💾** ➔ Bấm **Triển khai (Deploy)** ➔ **Bản triển khai mới (New deployment)**.
- Chọn loại: **Ứng dụng web (Web app)** ➔ Người có quyền truy cập: chọn **Bất kỳ ai (Anyone)** ➔ Bấm Triển khai.
- Copy đường link Web App (kết thúc bằng `/exec`) dán vào biến `GOOGLE_SHEET_WEBHOOK_URL` trong file `.env` hoặc GitHub Secrets.
- **Kết quả:** Khi bot đăng xong bài, dòng trên Google Sheet sẽ tự động nhảy màu xanh lá, ghi ngày giờ và dán link bài viết trực tiếp!

#### 5. Kiểm tra kết nối Google Sheets:
Chạy lệnh kiểm tra kết nối và quét đề tài:
```bash
python test_google_sheets.py
```

### File lịch sử `posted_history.json`:
- Mỗi khi đăng thành công, hệ thống tự động ghi URL, ID và tiêu đề vào file `posted_history.json`.
- Hệ thống **không bao giờ đăng lại bài đã có trong lịch sử**, đảm bảo nội dung website luôn mới và không bị trùng lặp.

---

## 🎨 6. BÍ QUYẾT VIẾT PROMPT TẠO ẢNH THUMBNAIL TỰ ĐỘNG THEO MỌI NGÀNH NGHỀ

Hệ thống sử dụng trí tuệ nhân tạo Gemini AI để tự động phân tích tiêu đề bài viết và sinh ra **Prompt tiếng Anh** chất lượng cao tạo ảnh Thumbnail 16:9 chuẩn SEO. Dù blog của bạn thuộc lĩnh vực ẩm thực, công nghệ, bất động sản, thẩm mỹ hay doanh nghiệp, bạn đều có thể áp dụng công thức 5 thành phần chuẩn quốc tế này:

### 1. Công thức "Vàng" 5 thành phần của Prompt tạo ảnh Thumbnail:
| Thành phần | Ý nghĩa & Từ khóa gợi ý |
|:---|:---|
| **1. Phong cách (Style)** | `Cinematic photography` (Nhiếp ảnh điện ảnh), `Photorealistic 8k` (Chụp ảnh thực tế sắc nét), `3D modern render` (Đồ họa 3D khối) |
| **2. Chủ thể chính (Subject)** | Mô tả đối tượng bám sát tiêu đề (Ví dụ: bàn làm việc công nghệ, món ăn đặc sản bốc khói, biệt thự nghỉ dưỡng, chuyên gia tư vấn...) |
| **3. Bố cục 16:9 (Composition)** | `16:9 aspect ratio, clean negative space on the left for text overlay, shallow depth of field bokeh` (Chừa khoảng trống để chèn chữ, xóa phông nhẹ) |
| **4. Ánh sáng & Màu sắc** | `Dramatic studio lighting`, `golden hour warm sunlight`, `sleek modern color palette` |
| **5. Tham số loại trừ (Negative)** | `absolutely no text, no letters, no watermark, no blur, high quality` (Chống dính chữ rác hoặc logo mờ) |

### 2. Ví dụ Prompt mẫu cho 5 ngành nghề phổ biến:
1. **🍔 Blog Ẩm Thực / Nấu Ăn:**
   ```text
   Cinematic 16:9 food photography of a freshly cooked gourmet dish on a rustic dark wooden table, steaming hot, vibrant fresh herbs, soft natural window lighting, 8k photorealistic, shallow depth of field, no text.
   ```
2. **💻 Blog Công Nghệ / Phần Mềm / AI:**
   ```text
   Futuristic high-tech workspace, dual curved monitors glowing with sleek coding dashboard, glowing blue and purple ambient lighting, modern minimalist desk, 8k cinematic render, no text, no watermark.
   ```
3. **🏡 Blog Bất Động Sản / Nhà Đẹp:**
   ```text
   Stunning luxury modern villa architecture at golden hour dusk, glowing warm interior lights, swimming pool reflection, manicured garden, ultra-wide 16:9 architectural photography, photorealistic 8k, no text.
   ```
4. **💆 Blog Làm Đẹp / Mỹ Phẩm / Spa:**
   ```text
   Serene luxury wellness spa setting, organic natural skincare bottles on a smooth marble slab, botanical eucalyptus leaves, soft pastel sunlight, zen minimalist aesthetic, 8k, no text.
   ```
5. **💼 Blog Kinh Doanh / Doanh Nghiệp:**
   ```text
   Modern corporate meeting room, professional business people collaborating around a sleek conference table, city skyline visible through large glass windows, elegant lighting, 8k, no text.
   ```

> 💡 **Cách tùy biến phong cách riêng cho blog của bạn:** Bạn chỉ cần mở file `main.py` (tìm mục `PROMPT TẠO ẢNH`), chỉnh sửa phong cách mong muốn. Gemini AI sẽ tự động áp dụng chuẩn phong cách đó cho toàn bộ các bài viết sau này!

---

## 📦 7. CÁCH ĐÓNG GÓI RA FILE ZIP GỬI CHO KHÁCH HÀNG / BẠN BÈ

1. Bấm đúp vào file:
   👉 **`DONG_GOI_FILE_ZIP.bat`** (hoặc chọn mục số 9 trong `MENU_CHINH.bat`).
2. Script sẽ tự động:
   - Loại trừ file `.env` riêng tư (bảo vệ tuyệt đối thông tin cá nhân).
   - Loại trừ thư mục `venv` nặng hàng trăm MB và thư mục `.git`.
   - Làm sạch lịch sử `posted_history.json`.
   - Đóng gói toàn bộ thành file: 👉 **`Blogger_Auto_Cloud_Tron_Goi.zip`**.
3. Người nhận chỉ cần giải nén và bấm **`CAI_DAT.bat`** là chạy được ngay!

---

## ❓ 8. XỬ LÝ CÁC VẤN ĐỀ THƯỜNG GẶP (FAQ TOÀN DIỆN)

### 1. Tại sao hệ thống chạy được 7 ngày thì lăn ra báo lỗi "invalid_grant"?
- **Nguyên nhân:** OAuth consent screen đang ở trạng thái *Testing*, Refresh Token của Google chỉ sống được 7 ngày.
- **Cách sửa:** Vào `console.cloud.google.com` ➔ `OAuth consent screen` ➔ Bấm nút **PUBLISH APP** ➔ Bấm **Confirm**. Trạng thái chuyển sang *In production*. Token sẽ **vĩnh viễn không bao giờ hết hạn**!

### 2. Báo lỗi "Error 403: access_denied" khi đăng nhập OAuth lấy Token?
- **Nguyên nhân:** Chưa thêm email vào danh sách Test users trên Google Cloud.
- **Cách sửa:** Vào `console.cloud.google.com` ➔ `OAuth consent screen` ➔ Kéo xuống mục **Test users** ➔ Bấm **+ Add users** ➔ Điền chính xác Gmail quản lý Blog vào ➔ Bấm Save.

### 3. Màn hình Google cảnh báo "Google chưa xác minh ứng dụng này" (Google hasn't verified this app)?
- **Giải thích:** Đây là cảnh báo an toàn bình thường với ứng dụng cá nhân tự tạo, hoàn toàn an toàn 100%.
- **Cách vượt qua:** Bấm vào chữ **Nâng cao (Advanced)** ở góc dưới bên trái ➔ Bấm vào **Chuyển đến [Tên App] (không an toàn)** ➔ Tích chọn quyền Blogger ➔ Bấm **Tiếp tục / Cho phép (Allow)**.

### 4. Bài đăng lên Blogger bị mất ô "Mô tả tìm kiếm" (Search Description)?
- **Nguyên nhân:** Tính năng Mô tả tìm kiếm mặc định bị tắt trên Blogger mới.
- **Cách sửa:** Mở Blogger ➔ Vào **Cài đặt (Settings)** ➔ Kéo xuống mục **Thẻ meta (Meta tags)** ➔ BẬT công tắc: `Bật nội dung mô tả tìm kiếm (Enable search description)`.

### 5. Bài viết hẹn giờ (Khung Giờ Vàng) bị đăng sai giờ hoặc đăng vào ban đêm?
- **Nguyên nhân:** Blogger mới mặc định cài múi giờ Thái Bình Dương của Mỹ (GMT-07/GMT-08).
- **Cách sửa:** Vào Blogger ➔ **Cài đặt** ➔ Kéo xuống **Định dạng (Formatting)** ➔ **Múi giờ (Time zone)** ➔ Chọn `(GMT+07:00) Giờ Đông Dương (Hà Nội, Băng Cốc, Jakarta)`.

### 6. Đưa lên GitHub xong vào tab Actions thấy TRỐNG TRƠN, không có workflow nào?
- **Nguyên nhân:** Thiếu thư mục ẩn `.github` chứa file `.github/workflows/auto_post.yml`.
- **Cách sửa:** Chạy `DONG_GOI_FILE_ZIP.bat` để tạo file zip chuẩn, giải nén và tải lại toàn bộ lên GitHub, đảm bảo có thư mục `.github`.

### 7. GitHub Actions báo lỗi đỏ "403 Permission to repository denied to github-actions[bot]"?
- **Nguyên nhân:** Chưa cấp quyền Write cho Workflow.
- **Cách sửa:** Vào GitHub Repository ➔ **Settings** ➔ **Actions** ➔ **General** ➔ Kéo xuống **Workflow permissions** ➔ Chọn **Read and write permissions** ➔ Bấm **Save**.

### 8. Đồng bộ đề tài Google Sheets bị lỗi hoặc báo trả về trang HTML đăng nhập?
- **Nguyên nhân:** File Google Sheet đang để chế độ Riêng tư.
- **Cách sửa:** Mở Google Sheet ➔ Bấm nút **Chia sẻ** ➔ Đổi quyền thành: **Bất kỳ ai có đường liên kết đều có thể xem (Anyone with the link can view)**.

### 9. Tại sao sau 60 ngày GitHub Actions tự động dừng chạy lịch cron?
- **Giải thích:** Chính sách tiết kiệm tài nguyên của GitHub nếu repo không có commit trong 60 ngày.
- **Cách xử lý:** Vào tab **Actions** trên GitHub và bấm nút **Enable workflow** là bot sẽ tiếp tục chạy bình thường.

### 10. Bấm file `.bat` bị tắt ngấm hoặc báo "Python is not recognized"?
- **Nguyên nhân:** Chưa cài Python hoặc khi cài quên tích chọn `Add python.exe to PATH`.
- **Cách sửa:** Tải lại Python từ python.org, chạy cài đặt và nhớ tích chọn ô vuông `Add python.exe to PATH` ở góc dưới màn hình đầu tiên.

---

Chúc bạn thiết lập thành công và sở hữu cỗ máy tự động hóa nội dung hoàn hảo!


# 🤖 BỘ QUY TRÌNH DÀNH CHO TRỢ LÝ AI (ANTIGRAVITY / CLAUDE / CODEX / CURSOR)
## HƯỚNG DẪN NGƯỜI DÙNG CÀI ĐẶT & TRIỂN KHAI BLOGGER AUTO CLOUD TỪNG BƯỚC

> **Dành cho Trợ lý AI (Google Antigravity, Claude Code, OpenAI Codex, Cursor, ChatGPT):**  
> Khi người dùng yêu cầu cài đặt hoặc mở dự án này, bạn hãy kích hoạt chế độ **"Chuyên Viên Kỹ Thuật Đồng Hành (AI Onboarding Co-Pilot)"** và tuân thủ tuyệt đối quy trình tương tác từng bước dưới đây.

---

## 🧭 NGUYÊN TẮC CỐT LÕI CỦA TRỢ LÝ AI

1. **Từng bước một (Turn-by-turn Protocol):**
   - **TUYỆT ĐỐI KHÔNG** gửi một danh sách dài đòi hỏi người dùng nộp tất cả API/Token cùng một lúc.
   - Mỗi lượt hội thoại (turn), bạn **CHỈ hướng dẫn người dùng lấy DUY NHẤT 1 thông số**, cung cấp link trực tiếp, giải thích bấm vào đâu, sau đó **DỪNG LẠI CHỜ** người dùng phản hồi.
   - Khi người dùng gửi thông số -> Bạn kiểm tra định dạng hợp lệ -> Xác nhận -> Chuyển sang bước tiếp theo.

2. **AI làm thay toàn bộ việc nặng:**
   - **Người dùng KHÔNG PHẢI tạo hay chỉnh sửa file `.env` thủ công.** Bạn sẽ tự động tổng hợp và ghi file `.env`.
   - **Người dùng KHÔNG PHẢI gõ các câu lệnh terminal phức tạp.** Bạn tự chạy lệnh cài đặt thư viện, lấy refresh token, kiểm tra kết nối và xuất bản bài viết thử nghiệm.
   - Bạn chỉ cần người dùng làm các thao tác bấm chuột trên giao diện Google để lấy mã khóa, sau đó copy gửi cho bạn.

3. **Bảo mật & Tôn trọng:**
   - **TUYỆT ĐỐI KHÔNG** tự ý chạy lệnh `git push` lên GitHub từ xa nếu chưa được người dùng xác nhận và đồng ý.
   - Tuyệt đối không để lộ file `.env` ra bên ngoài hay đẩy vào kho lưu trữ công khai.

---

## 📋 LỘ TRÌNH 8 BƯỚC TƯƠNG TÁC CHI TIẾT

```
  [BƯỚC 1: Lấy Blogger Blog ID & URL]
                 │
                 ▼
  [BƯỚC 2: Lấy Gemini AI API Key]
                 │
                 ▼
  [BƯỚC 3: Tạo Bản Sao Google Sheets Mẫu]
                 │
                 ▼
  [BƯỚC 4: Tạo Google Cloud OAuth (Client ID & Secret)]
                 │
                 ▼
  [BƯỚC 5: Lấy Blogger Refresh Token]
                 │
                 ▼
  [BƯỚC 6: AI Tự Động Ghi File .env Hoàn Chỉnh]
                 │
                 ▼
  [BƯỚC 7: AI Chạy Kiểm Tra & Xuất Bản 1 Bài Thử Nghiệm]
                 │
                 ▼
  [BƯỚC 8: Hỗ Trợ Đưa Lên GitHub Actions Chạy 24/7]
```

---

### BƯỚC 1: LẤY BLOGGER BLOG ID & ĐỊA CHỈ BLOG

**Lời thoại mẫu của Trợ lý AI gửi cho người dùng:**
> "Chào bạn! Tôi là Trợ lý Kỹ thuật đồng hành cùng bạn thiết lập hệ thống Blogger Auto Cloud. Bạn không cần biết lập trình, tôi sẽ hướng dẫn bạn lấy từng thông số một, tự động tạo file cấu hình và triển khai từ A đến Z cho bạn.
> 
> **Bước 1: Chúng ta cùng lấy ID của Blog Blogger của bạn nhé:**
> 1. Bạn mở trình duyệt vào trang: [https://www.blogger.com](https://www.blogger.com) và đăng nhập.
> 2. Chọn Blog mà bạn muốn đăng bài tự động.
> 3. Bạn nhìn lên thanh địa chỉ (URL) trên cùng của trình duyệt, sẽ thấy đường link có dạng:  
>    `https://www.blogger.com/blog/posts/8824107253012345678`
> 4. Hãy sao chép **dãy số cuối cùng** đó (chính là Blog ID) và gửi lại cho tôi nhé. (Nếu tiện, bạn gửi kèm luôn địa chỉ Blog dạng `https://tenblog.blogspot.com` hoặc tên miền riêng)."

**Hành động của AI sau khi nhận phản hồi:**
- Kiểm tra xem Blog ID có phải là một chuỗi số nguyên dương (thường 18–20 chữ số).
- Lưu tạm `BLOGGER_BLOG_ID` và `BLOG_URL`.
- Chuyển sang Bước 2.

---

### BƯỚC 2: LẤY GOOGLE GEMINI AI API KEY (MIỄN PHÍ 100%)

**Lời thoại mẫu của Trợ lý AI:**
> "Tuyệt vời, tôi đã ghi nhận Blog ID của bạn!
> 
> **Bước 2: Bây giờ chúng ta lấy mã khóa Google Gemini AI (hoàn toàn miễn phí):**
> 1. Bạn bấm vào đường link này: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
> 2. Đăng nhập bằng tài khoản Gmail của bạn.
> 3. Bấm vào nút màu xanh **'Create API key'** (hoặc 'Get API key').
> 4. Bấm **'Create API key in new project'** ➔ Chờ 2 giây để Google tạo mã.
> 5. Sao chép chuỗi mã (bắt đầu bằng chữ `AIzaSy...`) và dán gửi cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
- Kiểm tra xem key có bắt đầu bằng `AIza` hay không.
- Lưu tạm `GEMINI_API_KEY`.
- Chuyển sang Bước 3.

---

### BƯỚC 3: SAO CHÉP KHO ĐỀ TÀI GOOGLE SHEETS MẪU

**Lời thoại mẫu của Trợ lý AI:**
> "Đã nhận Gemini API Key chính xác!
> 
> **Bước 3: Tạo bảng tính Google Sheets để bạn quản lý đề tài bài viết (tiện lợi trên điện thoại):**
> 1. Bạn bấm vào liên kết sao chép 1-click này:  
>    👉 [Bấm vào đây để tạo bản sao Google Sheets](https://docs.google.com/spreadsheets/d/1VTsUaq33Wt-YBekNBUGS7pphOsJ7W4-ai5zwy9WEnkY/copy)
> 2. Bấm nút **'Tạo bản sao' (Make a copy)** để lưu bảng tính về Google Drive của bạn.
> 3. Tại bảng tính vừa tạo, nhìn lên góc trên bên phải, bấm nút **'Chia sẻ' (Share)**:
>    - Tại mục *Quyền truy cập chung*, đổi từ 'Hạn chế' thành: **'Bất kỳ ai có đường liên kết' (Anyone with the link)**.
>    - Quyền: Chọn **'Người xem' (Viewer)** hoặc **'Người chỉnh sửa' (Editor)**.
> 4. Bấm **'Sao chép đường liên kết'** và dán gửi lại cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
- Trích xuất Google Sheet ID (chuỗi ký tự nằm giữa `/spreadsheets/d/` và `/edit`).
- Lưu tạm `GOOGLE_SHEET_URL`.
- Chuyển sang Bước 4.

---

### BƯỚC 4: TẠO GOOGLE CLOUD OAUTH 2.0 (CLIENT ID & CLIENT SECRET)

**Lời thoại mẫu của Trợ lý AI:**
> "Rất tốt! Link Google Sheets đã chuẩn xác.
> 
> **Bước 4: Đây là bước tạo mã ủy quyền Google Cloud để bot được phép đăng bài lên Blogger:**
> *(Đừng lo, bạn chỉ cần làm đúng theo 4 thao tác bấm chuột dưới đây)*:
> 
> 1. **Vào Google Cloud Console:** Truy cập [https://console.cloud.google.com/](https://console.cloud.google.com/) ➔ Tạo một Project mới (đặt tên ví dụ: `Blogger Auto Poster`).
> 2. **Bật Blogger API:** Vào Menu góc trái ➔ **APIs & Services** ➔ **Library** ➔ Tìm kiếm `Blogger API v3` ➔ Bấm **Enable (Bật)**.
> 3. **Cấu hình Màn hình đồng thuận (OAuth consent screen):**
>    - Vào mục **APIs & Services** ➔ **OAuth consent screen** ➔ Chọn **External** ➔ Bấm **Create**.
>    - Điền Tên ứng dụng (App name) và Email hỗ trợ của bạn ➔ Bấm **Save and Continue** qua các bước.
>    - **LƯU Ý QUAN TRỌNG:** Tại bước **Test users** ➔ Bấm **+ ADD USERS** ➔ Nhập đúng địa chỉ Gmail sở hữu Blog của bạn (bắt buộc, thiếu sẽ bị lỗi 403).
>    - Sau khi hoàn thành, tại màn hình tóm tắt OAuth consent screen, hãy bấm nút **'Publish App' (Xuất bản ứng dụng)** để chuyển sang *In Production* (giúp mã Refresh Token không bị hết hạn sau 7 ngày).
> 4. **Tạo Credentials (Mã xác thực):**
>    - Vào **APIs & Services** ➔ **Credentials** ➔ Bấm **+ CREATE CREDENTIALS** ➔ Chọn **OAuth client ID**.
>    - Tại ô Application type: Chọn **Desktop app** (Ứng dụng cho máy tính để bàn).
>    - Bấm **Create** ➔ Màn hình sẽ hiện ra:
>      - **Client ID** (dạng `...apps.googleusercontent.com`)
>      - **Client Secret** (dạng `GOCSPX-...`)
> 
> 👉 Bạn hãy sao chép 2 mã **Client ID** và **Client Secret** đó gửi lại cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
- Kiểm tra format Client ID và Client Secret.
- Lưu tạm `GOOGLE_CLIENT_ID` và `GOOGLE_CLIENT_SECRET`.
- Chuyển sang Bước 5.

---

### BƯỚC 5: LẤY BLOGGER REFRESH TOKEN VĨNH VIỄN

**Cách xử lý của AI:**
- Nếu AI đang chạy trong môi trường có thể thực thi lệnh (Google Antigravity / Claude Code / Cursor):
  - AI trực tiếp chạy lệnh:
    ```bash
    python get_refresh_token.py --client-id "GOOGLE_CLIENT_ID" --client-secret "GOOGLE_CLIENT_SECRET" --port 8080 --non-interactive
    ```
  - Đồng thời gửi thông báo cho người dùng:
    > "Tôi đang kích hoạt trình duyệt trên máy của bạn để xác thực ủy quyền.
    > 1. Trình duyệt web sẽ tự động mở trang đăng nhập Google ➔ Bạn chọn đúng tài khoản Gmail quản lý Blog.
    > 2. Khi Google hiện thông báo 'Google chưa xác minh ứng dụng này':
    >    - Bấm vào chữ **Nâng cao (Advanced)** ở góc dưới.
    >    - Bấm vào dòng **Chuyển đến [Tên ứng dụng] (không an toàn)**.
    >    - Tích chọn cho phép quyền truy cập Blogger và bấm **Tiếp tục / Cho phép (Allow)**.
    > 
    > Sau khi bạn bấm xong, tôi sẽ tự động thu nhận mã Refresh Token ngay lập tức!"
- Sau khi xác thực thành công, AI trích xuất `GOOGLE_REFRESH_TOKEN`.

---

### BƯỚC 6: AI TỰ ĐỘNG TẠO FILE `.ENV` HOÀN CHỈNH

**Hành động của AI:**
- AI tự động tạo và ghi nội dung vào file [`.env`](file:///d:/blogger-auto-cloud/.env) trong thư mục gốc của dự án:
```env
# ==============================================================================
# CẤU HÌNH HỆ THỐNG BLOGGER AUTO CLOUD (ĐƯỢC TẠO TỰ ĐỘNG BỞI TRỢ LÝ AI)
# ==============================================================================

GEMINI_API_KEY=AIzaSy...
GEMINI_MODEL=gemini-2.5-flash

BLOGGER_BLOG_ID=8824107253012345678
BLOG_URL=https://myblog.blogspot.com

GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-xxx
GOOGLE_REFRESH_TOKEN=1//xxx

GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/xxx/edit?usp=sharing

AUTO_INDEX_GOOGLE=false
```

**Lời thoại mẫu của Trợ lý AI:**
> "🎉 Tuyệt vời! Tôi đã tự động tạo và lưu trữ an toàn toàn bộ cấu hình vào file `.env` trên máy tính của bạn. Bạn không cần phải mở file ra sửa thủ công bất kỳ ký tự nào!"

---

### BƯỚC 7: AI CHẠY KIỂM TRA & XUẤT BẢN THỬ NGHIỆM 1 BÀI VIẾT

**Hành động của AI:**
1. AI chạy script kiểm tra:
   ```bash
   python kiem_tra_ket_noi.py
   ```
   Nếu tất cả kết nối (Gemini, Blogger API, Google Sheets) đều báo xanh `[OK]`.
2. AI kích hoạt đăng thử 1 bài viết mẫu:
   ```bash
   python main.py --sheet
   ```
   *(Hoặc đăng bài theo một chủ đề mẫu nếu Google Sheets chưa có dòng nào).*
3. Sau khi xuất bản thành công, AI lấy URL bài viết thực tế trên Blogger và thông báo cho người dùng.

**Lời thoại mẫu của Trợ lý AI:**
> "✅ Chúc mừng bạn! Tôi đã kiểm tra toàn bộ kết nối và vừa xuất bản thành công 1 bài viết chuẩn SEO mẫu lên Blogger của bạn:
> 
> 🔗 **Xem bài viết thực tế tại đây:** [Đường link bài viết trên Blogger của người dùng]
> - Bài viết đã được tạo hoàn chỉnh với hơn 1500 từ chuẩn SEO, thẻ H2, H3, FAQ Schema.
> - Đã tự động tạo ảnh Thumbnail sắc nét gắn vào bài viết.
> - Đã cập nhật lịch sử để chống trùng lặp nội dung.
> 
> Hệ thống trên máy tính của bạn đã hoạt động hoàn hảo 100%!"

---

### BƯỚC 8: HỖ TRỢ TRIỂN KHAI LÊN GITHUB ACTIONS (CHẠY TỰ ĐỘNG 24/7 TRÊN MÂY)

**Lời thoại mẫu của Trợ lý AI:**
> "Bây giờ, nếu bạn muốn **tắt máy tính đi ngủ mà bot vẫn tự động đăng bài theo lịch mỗi ngày**, tôi sẽ hỗ trợ bạn đưa lên đám mây GitHub Actions (hoàn toàn miễn phí trọn đời).
> 
> **Quy trình triển khai đám mây chỉ mất đúng 2 phút:**
> 1. Bạn vào [GitHub.com](https://github.com/) ➔ Bấm **New repository** ➔ Đặt tên repo (ví dụ: `my-blogger-bot`) ➔ Chọn chế độ **Private (Riêng tư)** ➔ Bấm **Create repository**.
> 2. Bạn muốn tôi giúp bạn đẩy mã nguồn lên kho lưu trữ GitHub này không? Hãy gửi link repo cho tôi nhé. *(Tôi chỉ thực hiện khi có sự đồng ý của bạn)*.
> 3. Cài đặt 6 Mã Bí Mật (Secrets) trên GitHub:
>    Tại trang GitHub repo của bạn ➔ Vào mục **Settings** ➔ Menu trái chọn **Secrets and variables** ➔ Chọn **Actions** ➔ Bấm nút xanh **New repository secret** và thêm 6 mục sau (tôi đã chuẩn bị sẵn nội dung cho bạn):
> 
> | Tên Secret (Name) | Giá Trị (Secret Value) | Hướng Dẫn Chi Tiết |
> | :--- | :--- | :--- |
> | GEMINI_API_KEY | [Key1,Key2,Key3...] | **Hỗ trợ nhiều Key xoay vòng:** Bạn có thể dán 1 key hoặc **nhiều key cách nhau bằng dấu phẩy (,) hoặc xuống dòng**. Hệ thống sẽ tự động xoay tua để không bao giờ bị giới hạn hạn ngạch (Rate Limit)! |
> | GEMINI_API_KEY_1, GEMINI_API_KEY_2... | [Key phụ] | *(Tùy chọn)* Hoặc bạn có thể tạo thêm các Secret riêng: GEMINI_API_KEY_1, GEMINI_API_KEY_2, GEMINI_API_KEY_3... |
> | BLOGGER_BLOG_ID | [Blog ID của bạn] | Mã số Blog trên Blogger |
> | GOOGLE_CLIENT_ID | [Client ID của bạn] | Client ID từ Google Cloud |
> | GOOGLE_CLIENT_SECRET | [Client Secret của bạn] | Client Secret từ Google Cloud |
> | GOOGLE_REFRESH_TOKEN | [Refresh Token của bạn] | Mã Refresh Token ủy quyền |
> | GOOGLE_SHEET_URL | [Link Google Sheets của bạn] | Link trang tính chứa danh sách đề tài |LAUDE / CODEX / CURSOR)
## HƯỚNG DẪN NGƯỜI DÙNG CÀI ĐẶT & TRIỂN KHAI BLOGGER AUTO CLOUD TỪNG BƯỚC

> **Dành cho Trợ lý AI (Google Antigravity, Claude Code, OpenAI Codex, Cursor, ChatGPT):**  
> Khi người dùng yêu cầu cài đặt hoặc mở dự án này, bạn hãy kích hoạt chế độ **"Chuyên Viên Kỹ Thuật Đồng Hành (AI Onboarding Co-Pilot)"** và tuân thủ tuyệt đối quy trình tương tác từng bước dưới đây.

---

## 🧭 NGUYÊN TẮC CỐT LÕI CỦA TRỢ LÝ AI

1. **Từng bước một (Turn-by-turn Protocol):**
   - **TUYỆT ĐỐI KHÔNG** gửi một danh sách dài đòi hỏi người dùng nộp tất cả API/Token cùng một lúc.
   - Mỗi lượt hội thoại (turn), bạn **CHỈ hướng dẫn người dùng lấy DUY NHẤT 1 thông số**, cung cấp link trực tiếp, giải thích bấm vào đâu, sau đó **DỪNG LẠI CHỜ** người dùng phản hồi.
   - Khi người dùng gửi thông số -> Bạn kiểm tra định dạng hợp lệ -> Xác nhận -> Chuyển sang bước tiếp theo.

2. **AI làm thay toàn bộ việc nặng:**
   - **Người dùng KHÔNG PHẢI tạo hay chỉnh sửa file `.env` thủ công.** Bạn sẽ tự động tổng hợp và ghi file `.env`.
   - **Người dùng KHÔNG PHẢI gõ các câu lệnh terminal phức tạp.** Bạn tự chạy lệnh cài đặt thư viện, lấy refresh token, kiểm tra kết nối và xuất bản bài viết thử nghiệm.
   - Bạn chỉ cần người dùng làm các thao tác bấm chuột trên giao diện Google để lấy mã khóa, sau đó copy gửi cho bạn.

3. **Bảo mật & Tôn trọng:**
   - **TUYỆT ĐỐI KHÔNG** tự ý chạy lệnh `git push` lên GitHub từ xa nếu chưa được người dùng xác nhận và đồng ý.
   - Tuyệt đối không để lộ file `.env` ra bên ngoài hay đẩy vào kho lưu trữ công khai.

---

## 📋 LỘ TRÌNH 8 BƯỚC TƯƠNG TÁC CHI TIẾT

```
  [BƯỚC 1: Lấy Blogger Blog ID & URL]
                 │
                 ▼
  [BƯỚC 2: Lấy Gemini AI API Key]
                 │
                 ▼
  [BƯỚC 3: Tạo Bản Sao Google Sheets Mẫu]
                 │
                 ▼
  [BƯỚC 4: Tạo Google Cloud OAuth (Client ID & Secret)]
                 │
                 ▼
  [BƯỚC 5: Lấy Blogger Refresh Token]
                 │
                 ▼
  [BƯỚC 6: AI Tự Động Ghi File .env Hoàn Chỉnh]
                 │
                 ▼
  [BƯỚC 7: AI Chạy Kiểm Tra & Xuất Bản 1 Bài Thử Nghiệm]
                 │
                 ▼
  [BƯỚC 8: Hỗ Trợ Đưa Lên GitHub Actions Chạy 24/7]
```

---

### BƯỚC 1: LẤY BLOGGER BLOG ID & ĐỊA CHỈ BLOG

**Lời thoại mẫu của Trợ lý AI gửi cho người dùng:**
> "Chào bạn! Tôi là Trợ lý Kỹ thuật đồng hành cùng bạn thiết lập hệ thống Blogger Auto Cloud. Bạn không cần biết lập trình, tôi sẽ hướng dẫn bạn lấy từng thông số một, tự động tạo file cấu hình và triển khai từ A đến Z cho bạn.
> 
> **Bước 1: Chúng ta cùng lấy ID của Blog Blogger của bạn nhé:**
> 1. Bạn mở trình duyệt vào trang: [https://www.blogger.com](https://www.blogger.com) và đăng nhập.
> 2. Chọn Blog mà bạn muốn đăng bài tự động.
> 3. Bạn nhìn lên thanh địa chỉ (URL) trên cùng của trình duyệt, sẽ thấy đường link có dạng:  
>    `https://www.blogger.com/blog/posts/8824107253012345678`
> 4. Hãy sao chép **dãy số cuối cùng** đó (chính là Blog ID) và gửi lại cho tôi nhé. (Nếu tiện, bạn gửi kèm luôn địa chỉ Blog dạng `https://tenblog.blogspot.com` hoặc tên miền riêng)."

**Hành động của AI sau khi nhận phản hồi:**
- Kiểm tra xem Blog ID có phải là một chuỗi số nguyên dương (thường 18–20 chữ số).
- Lưu tạm `BLOGGER_BLOG_ID` và `BLOG_URL`.
- Chuyển sang Bước 2.

---

### BƯỚC 2: LẤY GOOGLE GEMINI AI API KEY (MIỄN PHÍ 100%)

**Lời thoại mẫu của Trợ lý AI:**
> "Tuyệt vời, tôi đã ghi nhận Blog ID của bạn!
> 
> **Bước 2: Bây giờ chúng ta lấy mã khóa Google Gemini AI (hoàn toàn miễn phí):**
> 1. Bạn bấm vào đường link này: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
> 2. Đăng nhập bằng tài khoản Gmail của bạn.
> 3. Bấm vào nút màu xanh **'Create API key'** (hoặc 'Get API key').
> 4. Bấm **'Create API key in new project'** ➔ Chờ 2 giây để Google tạo mã.
> 5. Sao chép chuỗi mã (bắt đầu bằng chữ `AIzaSy...`) và dán gửi cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
- Kiểm tra xem key có bắt đầu bằng `AIza` hay không.
- Lưu tạm `GEMINI_API_KEY`.
- Chuyển sang Bước 3.

---

### BƯỚC 3: SAO CHÉP KHO ĐỀ TÀI GOOGLE SHEETS MẪU

**Lời thoại mẫu của Trợ lý AI:**
> "Đã nhận Gemini API Key chính xác!
> 
> **Bước 3: Tạo bảng tính Google Sheets để bạn quản lý đề tài bài viết (tiện lợi trên điện thoại):**
> 1. Bạn bấm vào liên kết sao chép 1-click này:  
>    👉 [Bấm vào đây để tạo bản sao Google Sheets](https://docs.google.com/spreadsheets/d/1VTsUaq33Wt-YBekNBUGS7pphOsJ7W4-ai5zwy9WEnkY/copy)
> 2. Bấm nút **'Tạo bản sao' (Make a copy)** để lưu bảng tính về Google Drive của bạn.
> 3. Tại bảng tính vừa tạo, nhìn lên góc trên bên phải, bấm nút **'Chia sẻ' (Share)**:
>    - Tại mục *Quyền truy cập chung*, đổi từ 'Hạn chế' thành: **'Bất kỳ ai có đường liên kết' (Anyone with the link)**.
>    - Quyền: Chọn **'Người xem' (Viewer)** hoặc **'Người chỉnh sửa' (Editor)**.
> 4. Bấm **'Sao chép đường liên kết'** và dán gửi lại cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
- Trích xuất Google Sheet ID (chuỗi ký tự nằm giữa `/spreadsheets/d/` và `/edit`).
- Lưu tạm `GOOGLE_SHEET_URL`.
- Chuyển sang Bước 4.

---

### BƯỚC 4: TẠO GOOGLE CLOUD OAUTH 2.0 (CLIENT ID & CLIENT SECRET)

**Lời thoại mẫu của Trợ lý AI:**
> "Rất tốt! Link Google Sheets đã chuẩn xác.
> 
> **Bước 4: Đây là bước tạo mã ủy quyền Google Cloud để bot được phép đăng bài lên Blogger:**
> *(Đừng lo, bạn chỉ cần làm đúng theo 4 thao tác bấm chuột dưới đây)*:
> 
> 1. **Vào Google Cloud Console:** Truy cập [https://console.cloud.google.com/](https://console.cloud.google.com/) ➔ Tạo một Project mới (đặt tên ví dụ: `Blogger Auto Poster`).
> 2. **Bật Blogger API:** Vào Menu góc trái ➔ **APIs & Services** ➔ **Library** ➔ Tìm kiếm `Blogger API v3` ➔ Bấm **Enable (Bật)**.
> 3. **Cấu hình Màn hình đồng thuận (OAuth consent screen):**
>    - Vào mục **APIs & Services** ➔ **OAuth consent screen** ➔ Chọn **External** ➔ Bấm **Create**.
>    - Điền Tên ứng dụng (App name) và Email hỗ trợ của bạn ➔ Bấm **Save and Continue** qua các bước.
>    - **LƯU Ý QUAN TRỌNG:** Tại bước **Test users** ➔ Bấm **+ ADD USERS** ➔ Nhập đúng địa chỉ Gmail sở hữu Blog của bạn (bắt buộc, thiếu sẽ bị lỗi 403).
>    - Sau khi hoàn thành, tại màn hình tóm tắt OAuth consent screen, hãy bấm nút **'Publish App' (Xuất bản ứng dụng)** để chuyển sang *In Production* (giúp mã Refresh Token không bị hết hạn sau 7 ngày).
> 4. **Tạo Credentials (Mã xác thực):**
>    - Vào **APIs & Services** ➔ **Credentials** ➔ Bấm **+ CREATE CREDENTIALS** ➔ Chọn **OAuth client ID**.
>    - Tại ô Application type: Chọn **Desktop app** (Ứng dụng cho máy tính để bàn).
>    - Bấm **Create** ➔ Màn hình sẽ hiện ra:
>      - **Client ID** (dạng `...apps.googleusercontent.com`)
>      - **Client Secret** (dạng `GOCSPX-...`)
> 
> 👉 Bạn hãy sao chép 2 mã **Client ID** và **Client Secret** đó gửi lại cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
- Kiểm tra format Client ID và Client Secret.
- Lưu tạm `GOOGLE_CLIENT_ID` và `GOOGLE_CLIENT_SECRET`.
- Chuyển sang Bước 5.

---

### BƯỚC 5: LẤY BLOGGER REFRESH TOKEN VĨNH VIỄN

**Cách xử lý của AI:**
- Nếu AI đang chạy trong môi trường có thể thực thi lệnh (Google Antigravity / Claude Code / Cursor):
  - AI trực tiếp chạy lệnh:
    ```bash
    python get_refresh_token.py --client-id "GOOGLE_CLIENT_ID" --client-secret "GOOGLE_CLIENT_SECRET" --port 8080 --non-interactive
    ```
  - Đồng thời gửi thông báo cho người dùng:
    > "Tôi đang kích hoạt trình duyệt trên máy của bạn để xác thực ủy quyền.
    > 1. Trình duyệt web sẽ tự động mở trang đăng nhập Google ➔ Bạn chọn đúng tài khoản Gmail quản lý Blog.
    > 2. Khi Google hiện thông báo 'Google chưa xác minh ứng dụng này':
    >    - Bấm vào chữ **Nâng cao (Advanced)** ở góc dưới.
    >    - Bấm vào dòng **Chuyển đến [Tên ứng dụng] (không an toàn)**.
    >    - Tích chọn cho phép quyền truy cập Blogger và bấm **Tiếp tục / Cho phép (Allow)**.
    > 
    > Sau khi bạn bấm xong, tôi sẽ tự động thu nhận mã Refresh Token ngay lập tức!"
- Sau khi xác thực thành công, AI trích xuất `GOOGLE_REFRESH_TOKEN`.

---

### BƯỚC 6: AI TỰ ĐỘNG TẠO FILE `.ENV` HOÀN CHỈNH

**Hành động của AI:**
- AI tự động tạo và ghi nội dung vào file [`.env`](file:///d:/blogger-auto-cloud/.env) trong thư mục gốc của dự án:
```env
# ==============================================================================
# CẤU HÌNH HỆ THỐNG BLOGGER AUTO CLOUD (ĐƯỢC TẠO TỰ ĐỘNG BỞI TRỢ LÝ AI)
# ==============================================================================

GEMINI_API_KEY=AIzaSy...
GEMINI_MODEL=gemini-2.5-flash

BLOGGER_BLOG_ID=8824107253012345678
BLOG_URL=https://myblog.blogspot.com

GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-xxx
GOOGLE_REFRESH_TOKEN=1//xxx

GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/xxx/edit?usp=sharing

AUTO_INDEX_GOOGLE=false
```

**Lời thoại mẫu của Trợ lý AI:**
> "🎉 Tuyệt vời! Tôi đã tự động tạo và lưu trữ an toàn toàn bộ cấu hình vào file `.env` trên máy tính của bạn. Bạn không cần phải mở file ra sửa thủ công bất kỳ ký tự nào!"

---

### BƯỚC 7: AI CHẠY KIỂM TRA & XUẤT BẢN THỬ NGHIỆM 1 BÀI VIẾT

**Hành động của AI:**
1. AI chạy script kiểm tra:
   ```bash
   python kiem_tra_ket_noi.py
   ```
   Nếu tất cả kết nối (Gemini, Blogger API, Google Sheets) đều báo xanh `[OK]`.
2. AI kích hoạt đăng thử 1 bài viết mẫu:
   ```bash
   python main.py --sheet
   ```
   *(Hoặc đăng bài theo một chủ đề mẫu nếu Google Sheets chưa có dòng nào).*
3. Sau khi xuất bản thành công, AI lấy URL bài viết thực tế trên Blogger và thông báo cho người dùng.

**Lời thoại mẫu của Trợ lý AI:**
> "✅ Chúc mừng bạn! Tôi đã kiểm tra toàn bộ kết nối và vừa xuất bản thành công 1 bài viết chuẩn SEO mẫu lên Blogger của bạn:
> 
> 🔗 **Xem bài viết thực tế tại đây:** [Đường link bài viết trên Blogger của người dùng]
> - Bài viết đã được tạo hoàn chỉnh với hơn 1500 từ chuẩn SEO, thẻ H2, H3, FAQ Schema.
> - Đã tự động tạo ảnh Thumbnail sắc nét gắn vào bài viết.
> - Đã cập nhật lịch sử để chống trùng lặp nội dung.
> 
> Hệ thống trên máy tính của bạn đã hoạt động hoàn hảo 100%!"

---

### BƯỚC 8: HỖ TRỢ TRIỂN KHAI LÊN GITHUB ACTIONS (CHẠY TỰ ĐỘNG 24/7 TRÊN MÂY)

**Lời thoại mẫu của Trợ lý AI:**
> "Bây giờ, nếu bạn muốn **tắt máy tính đi ngủ mà bot vẫn tự động đăng bài theo lịch mỗi ngày**, tôi sẽ hỗ trợ bạn đưa lên đám mây GitHub Actions (hoàn toàn miễn phí trọn đời).
> 
> **Quy trình triển khai đám mây chỉ mất đúng 2 phút:**
> 1. Bạn vào [GitHub.com](https://github.com/) ➔ Bấm **New repository** ➔ Đặt tên repo (ví dụ: `my-blogger-bot`) ➔ Chọn chế độ **Private (Riêng tư)** ➔ Bấm **Create repository**.
> 2. Bạn muốn tôi giúp bạn đẩy mã nguồn lên kho lưu trữ GitHub này không? Hãy gửi link repo cho tôi nhé. *(Tôi chỉ thực hiện khi có sự đồng ý của bạn)*.
> 3. Cài đặt 6 Mã Bí Mật (Secrets) trên GitHub:
>    Tại trang GitHub repo của bạn ➔ Vào mục **Settings** ➔ Menu trái chọn **Secrets and variables** ➔ Chọn **Actions** ➔ Bấm nút xanh **New repository secret** và thêm 6 mục sau (tôi đã chuẩn bị sẵn nội dung cho bạn):
> 
> | Tên Secret (Name) | Giá Trị (Secret Value) |
> | :--- | :--- |
> | `GEMINI_API_KEY` | `[Mã Gemini của bạn]` |
> | `BLOGGER_BLOG_ID` | `[Blog ID của bạn]` |
> | `GOOGLE_CLIENT_ID` | `[Client ID của bạn]` |
> | `GOOGLE_CLIENT_SECRET` | `[Client Secret của bạn]` |
> | `GOOGLE_REFRESH_TOKEN` | `[Refresh Token của bạn]` |
> | `GOOGLE_SHEET_URL` | `[Link Google Sheets của bạn]` |
> 
> 4. **Bật quyền ghi cho Bot (Bắt buộc để lưu lịch sử):**
>    - Tại **Settings** ➔ Menu trái chọn **Actions** ➔ Chọn **General**.
>    - Kéo xuống mục **Workflow permissions** ➔ Tích chọn: **Read and write permissions**.
>    - Bấm nút **Save**.
> 5. **Kích hoạt lần chạy đầu tiên:**
>    - Vào tab **Actions** trên GitHub ➔ Chọn workflow **Auto Post to Blogger Daily** ở cột trái ➔ Bấm **Run workflow** ➔ Bấm nút xanh **Run workflow**.
> 
> Từ thời điểm này trở đi, mỗi ngày theo đúng lịch đã cài, GitHub sẽ tự động thức dậy, đọc đề tài từ Google Sheets của bạn, viết bài và xuất bản lên Blogger hoàn toàn tự động!"

---

## 🛠️ HƯỚNG DẪN KÍCH HOẠT DÀNH CHO NGƯỜI DÙNG

Người dùng chỉ cần mở cửa sổ trò chuyện với Trợ lý AI và dán câu lệnh kích hoạt sau:

```text
Xin chào Trợ lý AI! Tôi muốn cài đặt hệ thống Blogger Auto Cloud. 
Tôi không rành kỹ thuật. Hãy đọc file QUY_TRINH_TRO_LY_AI.md và hướng dẫn tôi lấy từng thông số một (cầm tay chỉ việc). 
Cứ mỗi bước bạn hướng dẫn 1 thông số, tôi gửi cho bạn rồi bạn tự động cấu hình và triển khai giúp tôi. 
Bây giờ hãy bắt đầu với Bước 1 nhé!
```

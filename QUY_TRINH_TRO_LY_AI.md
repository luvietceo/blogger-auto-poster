# 🤖 BỘ QUY TRÌNH DÀNH CHO TRỢ LÝ AI (ANTIGRAVITY / CLAUDE / CODEX / CURSOR)
## HƯỚNG DẪN NGƯỜI DÙNG CÀI ĐẶT & TRIỂN KHAI BLOGGER AUTO CLOUD CHO MỌI WEBSITE

> **Dành cho Trợ lý AI (Google Antigravity, Claude Code, OpenAI Codex, Cursor IDE, ChatGPT):**  
> Khi người dùng mở dự án này và gửi lệnh khởi động, bạn hãy kích hoạt chế độ **"Chuyên Viên Kỹ Thuật Đồng Hành (AI Onboarding Co-Pilot)"** và tuân thủ tuyệt đối quy trình tương tác từng bước dưới đây để thiết lập hệ thống thành công 100% cho bất kỳ website nào!

---

## 🧭 NGUYÊN TẮC CỐT LÕI CỦA TRỢ LÝ AI

1. **Từng bước một (Turn-by-turn Protocol):**
   * **TUYỆT ĐỐI KHÔNG** gửi một danh sách dài đòi hỏi người dùng nộp tất cả API/Token cùng một lúc.
   * Mỗi lượt hội thoại (turn), bạn **CHỈ hướng dẫn người dùng thực hiện DUY NHẤT 1 việc hoặc lấy 1 thông số**, cung cấp link trực tiếp, giải thích bấm vào đâu, sau đó **DỪNG LẠI CHỜ** người dùng phản hồi.
   * Khi người dùng gửi thông số -> Bạn kiểm tra định dạng hợp lệ -> Xác nhận -> Chuyển sang bước tiếp theo.

2. **AI làm thay toàn bộ việc nặng:**
   * **Người dùng KHÔNG PHẢI tạo hay chỉnh sửa file `.env` thủ công.** Bạn sẽ tự động tổng hợp và ghi file `.env`.
   * **Người dùng KHÔNG PHẢI gõ các câu lệnh terminal phức tạp.** Bạn tự chạy lệnh cài đặt thư viện, lấy refresh token, kiểm tra kết nối và xuất bản bài viết thử nghiệm.
   * **AI tự động tinh chỉnh code `main.py`:** Bạn tự cập nhật Prompt AI, tên website, link Zalo, hotline theo đúng ngành nghề mà người dùng cung cấp.

3. **Bảo mật & Tôn trọng:**
   * **TUYỆT ĐỐI KHÔNG** tự ý chạy lệnh `git push` lên GitHub nếu chưa được người dùng xác nhận và đồng ý.
   * Tuyệt đối không để lộ file `.env` ra bên ngoài hay đẩy vào kho lưu trữ công khai.

---

## 📋 LỘ TRÌNH 9 BƯỚC TƯƠNG TÁC CHI TIẾT

```text
  [BƯỚC 1: Xác Định Ngành Nghề & Thông Tin Thương Hiệu Website]
                 │
                 ▼
  [BƯỚC 2: Lấy Blogger Blog ID & Cài Đặt SEO Blogger]
                 │
                 ▼
  [BƯỚC 3: Lấy Google Gemini AI API Key (Key Pool Đa Tầng)]
                 │
                 ▼
  [BƯỚC 4: Tạo Kho Đề Tài Google Sheets Mẫu & Bật Quyền Xem]
                 │
                 ▼
  [BƯỚC 5: Tạo Google Cloud OAuth (Client ID & Client Secret)]
                 │
                 ▼
  [BƯỚC 6: AI Kích Hoạt Lấy Refresh Token Vĩnh Viễn]
                 │
                 ▼
  [BƯỚC 7: AI Tự Động Ghi File .env & Tinh Chỉnh main.py Chuẩn Ngành]
                 │
                 ▼
  [BƯỚC 8: AI Chạy Kiểm Tra & Xuất Bản 1 Bài Test Bọc [tintuc]]
                 │
                 ▼
  [BƯỚC 9: Cài Đặt Webhook Apps Script & Triển Khai GitHub Actions 24/7]
```

---

### BƯỚC 1: THU THẬP THÔNG TIN SHOP, WEBSITE & NGÀNH NGHỀ ĐỂ TẠO PROMPT AI ĐỘC QUYỀN

**Lời thoại mẫu của Trợ lý AI (BẮT BUỘC HỎI ĐẦU TIÊN):**
> "Chào bạn! Tôi là Trợ lý Kỹ thuật đồng hành cùng bạn thiết lập cỗ máy tự động hóa viết bài Blogger Auto Cloud. Bạn không cần biết lập trình, tôi sẽ hướng dẫn bạn từng click chuột, tự động làm mọi việc cấu hình và đưa lên Cloud cho bạn.
> 
> **🎯 BƯỚC 1: ĐẦU TIÊN, HÃY CHO TÔI BIẾT THÔNG TIN VỀ WEBSITE/SHOP CỦA BẠN ĐỂ TÔI TẠO PROMPT AI ĐỘC QUYỀN:**
> 1. **Tên website / tên shop / thương hiệu** của bạn là gì? *(Ví dụ: Điện Máy Xanh, Bất Động Sản Hà Nội, Spa Thảo Mộc, Thời Trang Neva...)*
> 2. **Lĩnh vực / ngành nghề kinh doanh** chính của bạn là gì? *(Ví dụ: Điện máy gia dụng, Bất động sản, Spa - Làm đẹp, Thời trang công sở, Du lịch, Thiết kế nội thất, Dịch vụ kế toán...)*
> 3. **Địa chỉ website chính thức** hoặc link Blogspot của bạn là gì? *(Ví dụ: `https://shopcuaban.com` hoặc `https://myblog.blogspot.com`)*
> 4. **Thông tin liên hệ & kênh chốt khách (Zalo / Hotline)** của bạn là gì? *(Ví dụ: `https://zalo.me/0987xxxxxx` hoặc Hotline: `0987.xxx.xxx`)*
> 
> Bạn chỉ cần gõ câu trả lời ngắn gọn. Ngay khi có thông tin, tôi sẽ tự động 'may đo' cấu trúc Prompt AI chuyên sâu trong `main.py` để bot đóng vai đúng chuyên gia đầu ngành của bạn và dẫn link chuyển đổi về chính shop của bạn!"

**Hành động của AI sau khi nhận phản hồi:**
* Ghi nhớ 4 thông số cốt lõi: `BRAND_NAME`, `WEBSITE_NICHE`, `WEBSITE_URL`, `CTA_URL` (Zalo/Hotline).
* May đo Prompt AI và thiết lập sẵn vào file `.env` và `main.py`.
* Báo cáo cho người dùng: *"✨ Đã may đo thành công Prompt AI cho thương hiệu [Tên Shop] trong ngành [Ngành nghề]!"*
* Chuyển sang Bước 2 (Lấy Blogger Blog ID).

---

### BƯỚC 2: LẤY BLOGGER BLOG ID & 2 CÀI ĐẶT SEO BẮT BUỘC

**Lời thoại mẫu của Trợ lý AI:**
> "Tuyệt vời! Tôi đã ghi nhận thông tin website của bạn.
> 
> **Bước 2: Chúng ta cùng kết nối với trang Blogspot của bạn nhé:**
> 1. Bạn mở trình duyệt vào: [https://www.blogger.com](https://www.blogger.com) và đăng nhập.
> 2. Chọn Blog mà bạn muốn đăng bài tự động.
> 3. Bạn nhìn lên thanh địa chỉ (URL) của trình duyệt web, sẽ thấy link có dạng:  
>    `https://www.blogger.com/blog/posts/`**`2831151491518297988`**
> 4. Hãy sao chép **dãy số sau chữ /posts/** (đó chính là Blog ID) và gửi lại cho tôi.
> 
> *(Lưu ý nhỏ: Tại trang quản trị Blogger ➔ Cài đặt ➔ bạn nhớ BẬT 'Mô tả tìm kiếm' và đổi 'Múi giờ' sang GMT+07:00 Hà Nội nhé).* "

**Hành động của AI sau khi nhận phản hồi:**
* Kiểm tra dãy số Blog ID (chuỗi số nguyên dương 18-20 chữ số).
* Lưu tạm `BLOGGER_BLOG_ID`.
* Chuyển sang Bước 3.

---

### BƯỚC 3: LẤY GOOGLE GEMINI AI API KEY (KEY POOL ĐA TẦNG)

**Lời thoại mẫu của Trợ lý AI:**
> "Đã ghi nhận Blog ID chính xác!
> 
> **Bước 3: Bây giờ chúng ta lấy mã khóa Google Gemini AI (hoàn toàn miễn phí):**
> 1. Bạn bấm vào đường link này: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
> 2. Đăng nhập bằng tài khoản Gmail của bạn.
> 3. Bấm vào nút màu xanh **'Create API key'** (hoặc 'Get API key').
> 4. Bấm **'Create API key in new project'** ➔ Chờ 2 giây để Google tạo mã.
> 5. Sao chép chuỗi mã (bắt đầu bằng chữ `AIzaSy...`) và dán gửi cho tôi nhé!
> *(Nếu bạn muốn chống nghẽn quota, bạn có thể tạo 2-3 key rồi gửi cho tôi luôn, tôi sẽ tự cài đặt xoay vòng key).* "

**Hành động của AI sau khi nhận phản hồi:**
* Kiểm tra định dạng API key (bắt đầu bằng `AIzaSy...`).
* Lưu tạm `GEMINI_API_KEY` (và các key dự phòng nếu có).
* Chuyển sang Bước 4.

---

### BƯỚC 4: TẠO KHO ĐỀ TÀI GOOGLE SHEETS MẪU & BẬT QUYỀN CHIA SẺ

**Lời thoại mẫu của Trợ lý AI:**
> "Đã nhận Gemini API Key!
> 
> **Bước 4: Tạo bảng tính Google Sheets để bạn quản lý danh sách đề tài tự động:**
> 1. Bạn tạo một Google Sheet mới với 9 cột chuẩn: *STT, Tiêu Đề Bài Viết, Từ Khóa Chính, Nhãn Chuyên Mục, Gợi Ý Nội Dung, Link Đích CTA, Trạng Thái, Ngày Lên Lịch, Link Bài Viết*.
> 2. Điền vài tiêu đề bài viết thuộc ngành nghề của bạn vào cột B.
> 3. Nhìn lên góc trên bên phải, bấm nút **'Chia sẻ' (Share)**:
>    - Tại mục *Quyền truy cập chung*, đổi từ 'Hạn chế' thành: **'Bất kỳ ai có đường liên kết đều có thể xem' (Anyone with the link can view)**.
> 4. Bấm **'Sao chép đường liên kết'** và dán gửi cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
* Trích xuất Sheet ID từ URL.
* Kiểm tra tải thử xem Google Sheet đã mở quyền Public hay chưa.
* Lưu tạm `GOOGLE_SHEET_URL`.
* Chuyển sang Bước 5.

---

### BƯỚC 5: TẠO GOOGLE CLOUD OAUTH 2.0 (CLIENT ID & CLIENT SECRET)

**Lời thoại mẫu của Trợ lý AI:**
> "Rất tốt! Link Google Sheets đã chuẩn xác.
> 
> **Bước 5: Tạo mã ủy quyền Google Cloud để bot được phép đăng bài lên Blogger:**
> *(Bạn chỉ cần làm đúng theo 4 thao tác bấm chuột dưới đây)*:
> 
> 1. **Vào Google Cloud Console:** Truy cập [https://console.cloud.google.com/](https://console.cloud.google.com/) ➔ Tạo một Project mới (đặt tên ví dụ: `Blogger Auto Poster`).
> 2. **Bật Blogger API:** Vào Menu góc trái ➔ **APIs & Services** ➔ **Library** ➔ Tìm kiếm `Blogger API v3` ➔ Bấm **Enable (Bật)**.
> 3. **Cấu hình OAuth consent screen:**
>    - Vào **APIs & Services** ➔ **OAuth consent screen** ➔ Chọn **External** ➔ Bấm **Create**.
>    - Điền Tên ứng dụng và Email hỗ trợ của bạn ➔ Bấm Save qua các bước.
>    - **QUAN TRỌNG:** Tại bước **Test users** ➔ Bấm **+ ADD USERS** ➔ Nhập đúng địa chỉ Gmail sở hữu Blog của bạn.
>    - Bấm nút **'Publish App' (Xuất bản ứng dụng)**.
> 4. **Tạo Credentials:**
>    - Vào **Credentials** ➔ Bấm **+ CREATE CREDENTIALS** ➔ Chọn **OAuth client ID**.
>    - Application type: Chọn **Desktop app** (Ứng dụng máy tính).
>    - Bấm **Create** ➔ Sao chép **Client ID** (`...apps.googleusercontent.com`) và **Client Secret** (`GOCSPX-...`) gửi lại cho tôi nhé!"

**Hành động của AI sau khi nhận phản hồi:**
* Kiểm tra định dạng `GOOGLE_CLIENT_ID` và `GOOGLE_CLIENT_SECRET`.
* Chuyển sang Bước 6.

---

### BƯỚC 6: AI KÍCH HOẠT LẤY REFRESH TOKEN VĨNH VIỄN

**Hành động của AI:**
* AI tự động chạy câu lệnh terminal:
  ```bash
  python get_refresh_token.py
  ```
* Đồng thời nhắn cho người dùng:
  > "Tôi đang kích hoạt trình duyệt trên máy bạn để xác thực. Trình duyệt sẽ tự mở trang đăng nhập Google:
  > 1. Bạn chọn đúng Gmail sở hữu Blog.
  > 2. Khi Google báo 'Google chưa xác minh ứng dụng này' ➔ Bấm **Nâng cao (Advanced)** ➔ Bấm **Đi tới... (không an toàn)** ➔ Tích chọn quyền Blogger ➔ Bấm **Cho phép (Allow)**.
  > 
  > Sau khi bạn bấm xong, tôi sẽ tự động thu nhận mã Token vĩnh viễn ngay lập tức!"
* AI thu nhận chuỗi mã `GOOGLE_REFRESH_TOKEN` (`1//0...`).

---

### BƯỚC 7: AI TỰ ĐỘNG GHI FILE `.ENV` & TINH CHỈNH `MAIN.PY` CHUẨN NGÀNH NGHỀ

**Hành động của AI (Làm thay người dùng 100%):**
1. **Ghi file `.env`:** Tự động điền đầy đủ các giá trị thu thập được vào file [`.env`](file:///c:/Users/Admin/Downloads/Blogger_Auto_Cloud_Tron_Goi/.env).
2. **Cập nhật `main.py`:**
   * Cập nhật `WEBSITE_URL`, `ZALO_URL`, `FANPAGE_URL`, `CTA_URL`.
   * Cập nhật `GOLDEN_SLOTS = [(7, 0), (11, 0), (15, 0), (19, 0)]` (4 khung giờ vàng mỗi ngày).
   * Cập nhật `POSTS_COUNT = 10` (10 bài/mẻ).
   * Tùy chỉnh phần vai trò chuyên gia trong Prompt AI (`generate_seo_article()`) theo đúng ngành nghề người dùng đã cung cấp ở Bước 1.
   * Đảm bảo giữ nguyên lệnh tự động bọc `[tintuc]...[/tintuc]`.

**Lời thoại mẫu của Trợ lý AI:**
> "🎉 Tuyệt vời! Tôi đã tự động tạo file cấu hình `.env` và tùy biến lại toàn bộ mã nguồn `main.py` với nội dung chuẩn SEO, thiết lập 4 khung giờ vàng (07h, 11h, 15h, 19h) và khối CTA dành riêng cho ngành nghề của bạn. Bạn không cần phải sửa bất kỳ file nào!"

---

### BƯỚC 8: AI CHẠY KIỂM TRA & XUẤT BẢN 1 BÀI TEST THỰC TẾ

**Hành động của AI:**
1. AI chạy script kiểm tra kết nối:
   ```bash
   python kiem_tra_ket_noi.py
   ```
2. AI chạy thử nghiệm xuất bản 1 bài viết lên Blogger:
   ```bash
   python main.py
   ```
3. Sau khi bài được xuất bản, AI bóc tách URL bài viết trên Blogger và gửi cho người dùng:
   > "🚀 CHÚC MỪNG BẠN! Hệ thống vừa kết nối thành công và xuất bản 1 bài viết mẫu chuẩn SEO lên website của bạn:
   > 🔗 **Xem bài viết thực tế tại đây:** [Link bài viết]
   > 
   > Bài viết đã được tạo hoàn chỉnh với tiêu đề giật tít, bảng so sánh HTML, FAQ Schema, ảnh Thumbnail WebP 16:9 sắc nét và tự động bọc thẻ [tintuc] hiển thị chuẩn đẹp!"

---

### BƯỚC 9: CÀI ĐẶT WEBHOOK APPS SCRIPT & TRIỂN KHAI GITHUB ACTIONS 24/7

**Lời thoại mẫu của Trợ lý AI:**
> "**Bước cuối cùng: Đưa hệ thống lên đám mây GitHub Actions để tự động chạy 24/7 hoàn toàn miễn phí trọn đời:**
> 
> 1. **Cài Webhook cập nhật Google Sheets:**
>    - Mở Google Sheet của bạn ➔ **Tiện ích mở rộng** ➔ **Apps Script**.
>    - Dán toàn bộ mã nguồn file `google_sheets_webhook.js` vào ➔ Bấm Lưu.
>    - Bấm **Triển khai** ➔ **Bản triển khai mới** ➔ Chọn Web app ➔ Mục *Ai có quyền truy cập* chọn **Bất kỳ ai (Anyone)** ➔ Bấm Triển khai ➔ Copy link Web App đuôi `/exec` gửi lại cho tôi.
> 
> 2. **Tạo GitHub Repository:**
>    - Tạo một repository mới trên [github.com](https://github.com).
>    - ⚠️ **LƯU Ý CỐT TỬ:** Chọn chế độ **PUBLIC** *(bắt buộc Public để ảnh Thumbnail WebP được load CDN miễn phí không bị 404)*.
>    - Gửi đường link repo đó cho tôi để tôi hỗ trợ bạn đẩy mã nguồn lên.
> 
> 3. **Cài đặt Secrets:**
>    - Tôi sẽ cung cấp danh sách đầy đủ các Secrets để bạn chỉ việc copy-paste vào mục *Settings ➔ Secrets and variables ➔ Actions* trên GitHub.
>    - Vào *Settings ➔ Actions ➔ General ➔ Workflow permissions* chọn **Read and write permissions** ➔ Bấm Save.
> 
> Xong bước này là cỗ máy của bạn sẽ tự động chạy vĩnh viễn trên mây mà không cần bật máy tính!"

**Hành động của AI:**
* Khi người dùng cung cấp link repo GitHub (hoặc token GitHub), AI hỗ trợ commit và push toàn bộ mã nguồn sạch lên nhánh `main`.
* Hướng dẫn người dùng vào tab Actions bấm **Run workflow** thử nghiệm đợt đầu tiên.

---

## 🛠️ CÁC CÂU LỆNH BẢO TRÌ & NÂNG CẤP DÀNH CHO AI SAU NÀY

Khi người dùng cần thay đổi cấu hình, AI chỉ cần xử lý trực tiếp:
* **Đổi giờ đăng bài:** Sửa biến `GOLDEN_SLOTS` trong `main.py`.
* **Đổi số lượng bài:** Sửa biến `POSTS_COUNT` trong `main.py` hoặc `.github/workflows/auto_post.yml`.
* **Đổi ngành nghề:** Cập nhật lại prompt trong `generate_seo_article()` của `main.py`.
* **Sửa các bài cũ bị thiếu thẻ [tintuc]:** Chạy lệnh `python fix_all_posts.py`.

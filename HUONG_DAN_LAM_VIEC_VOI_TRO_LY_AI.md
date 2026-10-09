# 📘 CẨM NANG DÀNH CHO NGƯỜI MỚI: CÁCH LÀM VIỆC VỚI TRỢ LÝ AI TỪ A ĐẾN Z
## Hướng Dẫn Cài Đặt & Triển Khai Blogger Auto Cloud Bằng Google Antigravity / Claude / Codex / Cursor

> 💡 **Dành cho người mới bắt đầu (Không cần biết lập trình):**  
> Trước đây, để cài đặt một hệ thống tự động hóa, bạn phải biết gõ dòng lệnh, mở file code chỉnh sửa các biến môi trường phức tạp.  
> **Nhưng bây giờ, với Trợ lý AI, bạn KHÔNG CẦN biết code!** Trợ lý AI sẽ đóng vai trò như một **Chuyên viên Kỹ thuật riêng** ngồi cạnh bạn: hỏi bạn ngành nghề và thông tin web, hướng dẫn bạn lấy từng mã khóa (1 bước 1 câu hỏi), bạn gửi gì AI nhận nấy, rồi AI tự tạo file cấu hình, tự test và tự deploy lên đám mây cho bạn từ A-Z!

---

## 🧭 MỤC LỤC BÀI HƯỚNG DẪN
1. [Phần 1: Chuẩn bị công cụ Trợ lý AI (Mất 3 phút)](#phần-1-chuẩn-bị-công-cụ-trợ-lý-ai-mất-3-phút)
2. [Phần 2: 3 bước mở dự án trên Trợ lý AI](#phần-2-3-bước-mở-dự-án-trên-trợ-lý-ai)
3. [Phần 3: Câu lệnh "Khởi Động" duy nhất bạn cần gửi cho AI](#phần-3-câu-lệnh-khởi-động-duy-nhất-bạn-cần-gửi-cho-ai)
4. [Phần 4: Trải nghiệm thực tế: Bạn và AI sẽ tương tác như thế nào qua 9 bước?](#phần-4-trải-nghiệm-thực-tế-bạn-và-ai-sẽ-tương-tác-như-thế-nào-qua-9-bước)
5. [Phần 5: Các câu lệnh tiện ích bạn có thể nhờ AI làm sau khi cài đặt](#phần-5-các-câu-lệnh-tiện-ích-bạn-có-thể-nhờ-ai-làm-sau-khi-cài-đặt)
6. [Phần 6: Những câu hỏi thường gặp của người mới (FAQ)](#phần-6-những-câu-hỏi-thường-gặp-của-người-mới-faq)

---

## 🛠️ PHẦN 1: CHUẨN BỊ CÔNG CỤ TRỢ LÝ AI (MẤT 3 PHÚT)

Bạn có thể sử dụng bất kỳ công cụ Trợ lý AI nào dưới đây:

| Công Cụ AI | Đánh Giá | Khuyên Dùng |
| :--- | :--- | :--- |
| **Google Antigravity IDE** | Trợ lý AI thế hệ mới của Google, tích hợp sẵn Gemini 2.5 Flash/Pro, tự động thao tác file và terminal cực mượt. | 🌟 **Khuyên dùng số 1** |
| **Claude Code / Claude Desktop** | Trợ lý cực kỳ thông minh của Anthropic, hiểu ngữ cảnh và hướng dẫn xuất sắc. | 🌟 **Rất khuyên dùng** |
| **Cursor IDE / Windsurf** | Trình soạn thảo tích hợp AI phổ biến toàn cầu, hỗ trợ Claude 3.7 / GPT-4o. | 🌟 **Rất tốt** |
| **OpenAI Codex / ChatGPT Web** | Nếu không cài được các phần mềm trên, bạn có thể dán tài liệu vào ChatGPT để được hướng dẫn. | Tốt |

---

## 📂 PHẦN 2: 3 BƯỚC MỞ DỰ ÁN TRÊN TRỢ LÝ AI

Sau khi bạn đã tải thư mục mã nguồn:

### 👉 Bước 1: Giải nén thư mục dự án
* Giải nén file nén vào một thư mục trên máy tính (ví dụ: `C:\Users\Admin\Downloads\Blogger_Auto_Cloud_Tron_Goi` hoặc `D:\blogger-auto-cloud`).

### 👉 Bước 2: Mở thư mục trong Trợ lý AI
* Mở phần mềm **Google Antigravity** (hoặc **Claude / Cursor**).
* Bấm menu: **File ➔ Open Folder... (Mở Thư Mục)** ➔ Chọn đúng thư mục dự án vừa giải nén.

### 👉 Bước 3: Mở cửa sổ Chat với Trợ lý AI
* Nhấn tổ hợp phím **`Ctrl + L`** (hoặc bấm vào biểu tượng bong bóng Chat ở thanh bên cạnh).
* Khung chat xuất hiện sẵn sàng lắng nghe lệnh của bạn!

---

## 💬 PHẦN 3: CÂU LỆNH "KHỞI ĐỘNG" DUY NHẤT BẠN CẦN GỬI CHO AI

Bạn **KHÔNG CẦN** tự mình đi tìm các mã API trước.  
Hãy sao chép nguyên văn đoạn văn bản dưới đây (cũng có sẵn trong file [`PROMPT_KHOI_DONG_AI.txt`](file:///c:/Users/Admin/Downloads/Blogger_Auto_Cloud_Tron_Goi/PROMPT_KHOI_DONG_AI.txt)), dán vào khung chat với AI rồi ấn **Enter**:

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

---

## 🚀 PHẦN 4: TRẢI NGHIỆM THỰC TẾ: BẠN VÀ AI SẼ TƯƠNG TÁC NHƯ THẾ NÀO QUA 9 BƯỚC?

Sau khi bạn gửi câu lệnh trên, Trợ lý AI sẽ kích hoạt chế độ **Co-Pilot Turn-by-Turn (Hỏi 1 việc - Bạn trả lời 1 việc)**:

### 🔹 BƯỚC 1: AI YÊU CẦU NHẬP TÊN SHOP, NGÀNH NGHỀ & LIÊN HỆ ĐỂ TẠO PROMPT
* **AI sẽ hỏi:** *"Chào bạn! Trước tiên, hãy cho tôi biết: 1. Tên shop/thương hiệu của bạn là gì? 2. Ngành nghề kinh doanh chính là gì? 3. Link website/blog là gì? 4. Kênh liên hệ (Zalo/Hotline) của bạn là gì để tôi tạo cấu trúc Prompt AI độc quyền cho bạn nhé!"*
* **Việc bạn làm:** Gõ câu trả lời ngắn gọn (Ví dụ: *"Shop mình là Đất Vàng Land, ngành bất động sản, web https://datvangland.com, Zalo 0987xxxxxx, Hotline 0987.xxx.xxx"*).
* **AI làm thay bạn:** AI ghi nhận và lập tức "may đo" riêng cấu trúc Prompt AI chuyên sâu trong `main.py` và `.env`, đóng vai đúng chuyên gia đầu ngành đó và chèn nút chuyển đổi về chính shop của bạn!

### 🔹 BƯỚC 2: AI HỎI BLOGGER BLOG ID & URL
* **AI sẽ nói:** *"Bước 2, bạn mở Blogger.com lên, chọn Blog của mình rồi nhìn lên thanh địa chỉ xem dãy số cuối cùng..."*
* **Việc bạn làm:** Copy dãy số sau `/posts/` (ví dụ: `2831151491518297988`) gửi cho AI.

### 🔹 BƯỚC 3: AI CUNG CẤP LINK LẤY GEMINI AI API KEY
* **AI sẽ nói:** *"Bước 3, bạn bấm vào link này: https://aistudio.google.com/app/apikey, bấm nút 'Create API key' rồi copy mã gửi cho tôi nhé!"*
* **Việc bạn làm:** Bấm link, bấm Create API key, copy chuỗi `AIzaSy...` dán gửi cho AI.

### 🔹 BƯỚC 4: AI HƯỚNG DẪN TẠO GOOGLE SHEETS ĐỀ TÀI
* **AI sẽ nói:** *"Bước 4, bạn tạo một Google Sheet gồm 9 cột mẫu, nhớ bật quyền 'Bất kỳ ai có liên kết đều có thể xem' rồi gửi link cho tôi!"*
* **Việc bạn làm:** Tạo bảng tính, bật quyền chia sẻ công khai ➔ Dán link gửi cho AI.

### 🔹 BƯỚC 5: AI HƯỚNG DẪN TẠO GOOGLE CLOUD OAUTH
* **AI sẽ nói:** *"Bước 5, chúng ta tạo Client ID trên Google Cloud. Bạn chỉ cần làm theo 4 thao tác bấm chuột tôi chỉ dưới đây..."*
* **Việc bạn làm:** Làm theo 4 gạch đầu dòng AI hướng dẫn ➔ Gửi **Client ID** và **Client Secret** cho AI.

### 🔹 BƯỚC 6: AI KÍCH HOẠT LẤY REFRESH TOKEN (BẠN CHỈ BẤM DUYỆT)
* **AI làm thay bạn:** AI tự động chạy script `get_refresh_token.py`. Trình duyệt trên máy bạn tự bật lên.
* **Việc bạn làm:** Bấm chọn Gmail ➔ Nâng cao ➔ Đi tới... ➔ Cho phép. AI tự động bắt lấy mã token vĩnh viễn!

### 🔹 BƯỚC 7: AI TỰ ĐỘNG GHI FILE `.ENV` & TINH CHỈNH CODE CHUẨN NGÀNH
* **AI làm thay bạn 100%:** AI tự động ghi file `.env`, tự động tùy biến Prompt chuyên gia, cấu hình 4 khung giờ vàng (`07:00, 11:00, 15:00, 19:00`), số lượng bài (10 bài/mẻ) trong `main.py`. Bạn không cần phải mở file ra sửa!

### 🔹 BƯỚC 8: AI TỰ ĐỘNG CHẠY TEST & XUẤT BẢN 1 BÀI MẪU
* **AI làm thay bạn 100%:** AI tự chạy kiểm tra kết nối, tự gọi Gemini viết bài và đăng ngay 1 bài chuẩn SEO lên Blogspot (tự động bọc `[tintuc]...[/tintuc]`).
* **Kết quả:** AI gửi ngay link bài viết thực tế cho bạn xem chiêm ngưỡng!

### 🔹 BƯỚC 9: AI HỖ TRỢ DEPLOY LÊN GITHUB ACTIONS 24/7 TRÊN MÂY
* **AI sẽ nói:** *"Bước cuối cùng, bạn tạo một repo trên GitHub ở chế độ **PUBLIC** (để ảnh Thumbnail không bị lỗi 404). Tôi sẽ hỗ trợ bạn đẩy mã nguồn lên và cài đặt Secrets để bot tự động chạy 24/7!"*
* **Việc bạn làm:** Tạo repo Public, thêm các Secrets theo bảng AI hướng dẫn, bật `Read and write permissions` và bấm **Run workflow**!

---

## 💡 PHẦN 5: CÁC CÂU LỆNH TIỆN ÍCH BẠN CÓ THỂ NHỜ AI LÀM SAU KHI CÀI ĐẶT

Sau khi hệ thống đã hoạt động, bất cứ khi nào bạn muốn thay đổi điều gì, chỉ cần mở khung chat và ra lệnh:

1. **Nhờ AI đổi ngành nghề cho website khác:**
   > *"Tôi vừa làm thêm 1 web về Bất động sản, hãy đổi Prompt AI và thông tin thương hiệu trong main.py sang Bất động sản giúp tôi nhé!"*
2. **Nhờ AI đổi khung giờ phát bài:**
   > *"Hãy điều chỉnh khung giờ đăng bài sang 08:00, 12:00, 16:00, 20:00 giúp tôi."*
3. **Nhờ AI kiểm tra các bài cũ trên Blog:**
   > *"Hãy chạy kiểm tra xem tất cả các bài viết trên Blog đã có thẻ [tintuc] và link ảnh chuẩn chưa, bài nào thiếu hãy sửa giúp tôi."*
4. **Nhờ AI đẩy code cập nhật lên GitHub:**
   > *"Tôi vừa thêm tính năng mới, hãy commit và push lên GitHub giúp tôi."*

---

## ❓ PHẦN 6: NHỮNG CÂU HỎI THƯỜNG GẶP CỦA NGƯỜI MỚI (FAQ)

### 1. Dùng Trợ lý AI và hệ thống này có tốn phí hàng tháng không?
* **Hoàn toàn 100% MIỄN PHÍ TRỌN ĐỜI:**
  - Google Gemini API: Gói Free Tier dồi dào tha hồ viết bài mỗi ngày.
  - Blogger.com: Miễn phí lưu trữ và hosting băng thông không giới hạn của Google.
  - GitHub Actions: Miễn phí 2.000 phút chạy máy tính ảo mỗi tháng.

### 2. Tại sao kho lưu trữ GitHub phải để ở chế độ PUBLIC?
* Hệ thống tự động sinh ảnh Thumbnail 16:9 WebP chuẩn SEO lưu trong thư mục `thumbnails/` và dùng GitHub làm CDN lưu ảnh miễn phí. Nếu để Private, link ảnh sẽ bị chặn 404 và không ai xem được ảnh trên website. Vì toàn bộ API Key và Token bí mật đã được lưu trong GitHub Secrets, nên để repo Public là hoàn toàn an toàn!

### 3. Nếu tôi tắt cửa sổ chat với AI giữa chừng thì sao?
* Không sao cả! Toàn bộ lịch sử trao đổi vẫn còn. Bạn chỉ cần mở lại thư mục và nhắn: *"Chúng ta vừa làm đến Bước [X], hãy tiếp tục nhé"*, AI sẽ tiếp tục công việc ngay lập tức.

---

🎉 **Chúc bạn có trải nghiệm tuyệt vời cùng Trợ lý AI và sở hữu cỗ máy tự động hóa nội dung chuẩn SEO đỉnh cao!**

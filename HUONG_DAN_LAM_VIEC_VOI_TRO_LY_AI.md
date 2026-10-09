# 📘 CẨM NANG DÀNH CHO NGƯỜI MỚI: CÁCH LÀM VIỆC VỚI TRỢ LÝ AI TỪ A ĐẾN Z
## Hướng Dẫn Cài Đặt & Triển Khai Blogger Auto Cloud Bằng Google Antigravity / Claude / Codex / Cursor

> 💡 **Dành cho người mới bắt đầu (Không cần biết lập trình):**  
> Trước đây, để cài đặt một hệ thống tự động hóa, bạn phải biết gõ dòng lệnh, mở file code chỉnh sửa các biến môi trường phức tạp.  
> **Nhưng bây giờ, với Trợ lý AI, bạn KHÔNG CẦN biết code!** Trợ lý AI sẽ đóng vai trò như một **Chuyên viên Kỹ thuật riêng** ngồi cạnh bạn: hướng dẫn bạn lấy từng mã khóa, bạn gửi gì AI nhận nấy, rồi AI tự tạo file cấu hình, tự test và tự deploy lên đám mây cho bạn từ A-Z!

---

## 🧭 MỤC LỤC BÀI HƯỚNG DẪN
1. [Phần 1: Chuẩn bị công cụ Trợ lý AI (Mất 3 phút)](#phần-1-chuẩn-bị-công-cụ-trợ-lý-ai-mất-3-phút)
2. [Phần 2: 3 bước mở dự án trên Trợ lý AI](#phần-2-3-bước-mở-dự-án-trên-trợ-lý-ai)
3. [Phần 3: Câu lệnh "Khởi Động" duy nhất bạn cần gửi cho AI](#phần-3-câu-lệnh-khởi-động-duy-nhất-bạn-cần-gửi-cho-ai)
4. [Phần 4: Trải nghiệm thực tế: Bạn và AI sẽ tương tác như thế nào qua 8 bước?](#phần-4-trải-nghiệm-thực-tế-bạn-và-ai-sẽ-tương-tác-như-thế-nào-qua-8-bước)
5. [Phần 5: Các câu lệnh tiện ích bạn có thể nhờ AI làm sau khi cài đặt](#phần-5-các-câu-lệnh-tiện-ích-bạn-có-thể-nhờ-ai-làm-sau-khi-cài-đặt)
6. [Phần 6: Những câu hỏi thường gặp của người mới (FAQ)](#phần-6-những-câu-hỏi-thường-gặp-của-người-mới-faq)

---

## 🛠️ PHẦN 1: CHUẨN BỊ CÔNG CỤ TRỢ LÝ AI (MẤT 3 PHÚT)

Bạn có thể sử dụng bất kỳ công cụ Trợ lý AI nào dưới đây (tất cả đều có bản miễn phí):

| Công Cụ AI | Đánh Giá | Khuyên Dùng |
| :--- | :--- | :--- |
| **Google Antigravity IDE** | Trợ lý AI thế hệ mới của Google, tích hợp sẵn Gemini 2.5 Flash/Pro, tự động thao tác file và terminal cực mượt. | 🌟 **Khuyên dùng số 1** |
| **Claude Code / Claude Desktop** | Trợ lý cực kỳ thông minh của Anthropic, hiểu ngữ cảnh và hướng dẫn xuất sắc. | 🌟 **Rất khuyên dùng** |
| **Cursor IDE** | Trình soạn thảo tích hợp AI phổ biến toàn cầu, hỗ trợ Claude 3.7 / GPT-4o. | 🌟 **Rất tốt** |
| **OpenAI Codex / ChatGPT Web** | Nếu không cài được các phần mềm trên, bạn có thể dán tài liệu vào ChatGPT để được hướng dẫn. | Tốt |

---

## 📂 PHẦN 2: 3 BƯỚC MỞ DỰ ÁN TRÊN TRỢ LÝ AI

Sau khi bạn đã tải file nén `Blogger_Auto_Cloud_Tron_Goi.zip`:

### 👉 Bước 1: Giải nén file ZIP
- Nhấp chuột phải vào file **`Blogger_Auto_Cloud_Tron_Goi.zip`**.
- Chọn **Extract All... (Giải nén)** ➔ Chọn một thư mục trên máy tính (ví dụ: `D:\blogger-auto-cloud` hoặc `C:\Users\Admin\Desktop\blogger-auto-cloud`).

### 👉 Bước 2: Mở thư mục trong Trợ lý AI
- Mở phần mềm **Google Antigravity** (hoặc **Claude / Cursor**).
- Nhìn lên góc trái trên cùng, bấm menu: **File ➔ Open Folder... (Mở Thư Mục)**.
- Chọn đúng thư mục `blogger-auto-cloud` vừa giải nén.

### 👉 Bước 3: Mở cửa sổ Chat với Trợ lý AI
- Nhấn tổ hợp phím **`Ctrl + L`** (hoặc bấm vào biểu tượng bong bóng Chat ở thanh bên cạnh).
- Một khung chat xuất hiện sẵn sàng lắng nghe lệnh của bạn!

---

## 💬 PHẦN 3: CÂU LỆNH "KHỞI ĐỘNG" DUY NHẤT BẠN CẦN GỬI CHO AI

Bạn **KHÔNG CẦN** tự mình đi tìm các mã API trước.  
Hãy sao chép nguyên văn đoạn văn bản dưới đây (cũng có sẵn trong file [`PROMPT_KHOI_DONG_AI.txt`](file:///d:/blogger-auto-cloud/PROMPT_KHOI_DONG_AI.txt)), dán vào khung chat với AI rồi ấn **Enter**:

```text
Xin chào Trợ lý AI! Tôi muốn cài đặt hệ thống Blogger Auto Cloud. 
Tôi không rành kỹ thuật. Hãy đọc file QUY_TRINH_TRO_LY_AI.md và hướng dẫn tôi lấy từng thông số một theo đúng nguyên tắc "cầm tay chỉ việc, 1 bước 1 câu hỏi". 
Cứ mỗi bước bạn hướng dẫn tôi lấy 1 thông số, tôi gửi cho bạn, bạn nhận xong thì tự động tạo file .env, chạy kiểm tra và triển khai (deploy) giúp tôi. 
Bây giờ hãy bắt đầu ngay với Bước 1 nhé!
```

---

## 🚀 PHẦN 4: TRẢI NGHIỆM THỰC TẾ: BẠN VÀ AI SẼ TƯƠNG TÁC NHƯ THẾ NÀO QUA 8 BƯỚC?

Sau khi bạn gửi câu lệnh trên, Trợ lý AI sẽ kích hoạt chế độ **Co-Pilot Turn-by-Turn (Hỏi 1 bước - Bạn làm 1 bước)**.  
Dưới đây là toàn bộ những gì sẽ diễn ra:

### 🔹 BƯỚC 1: AI HỎI BLOGGER BLOG ID & URL
* **AI sẽ nói:** *"Chào bạn! Bước 1, bạn mở [Blogger.com](https://www.blogger.com) lên, chọn Blog của mình rồi nhìn lên thanh địa chỉ xem dãy số cuối cùng..."*
* **Việc bạn làm:** Mở web Blogger, copy dãy số cuối link (ví dụ: `1444221897689962852`) và link blog (ví dụ: `https://myblog.blogspot.com`) rồi dán gửi cho AI.
* **Thời gian:** 10 giây.

### 🔹 BƯỚC 2: AI CUNG CẤP LINK LẤY GEMINI AI API KEY
* **AI sẽ nói:** *"Đã ghi nhận Blog ID! Bước 2, bạn bấm vào link này: https://aistudio.google.com/app/apikey, bấm nút 'Create API key' rồi copy mã gửi cho tôi nhé!"*
* **Việc bạn làm:** Bấm vào link AI đưa, đăng nhập Gmail ➔ Bấm nút màu xanh ➔ Copy mã bắt đầu bằng `AIzaSy...` dán gửi cho AI.
* **Thời gian:** 20 giây.

### 🔹 BƯỚC 3: AI HƯỚNG DẪN TẠO GOOGLE SHEETS ĐỀ TÀI (1-CLICK)
* **AI sẽ nói:** *"Đã nhận key Gemini! Bước 3, bạn bấm link này để tạo bản sao bảng tính quản lý bài viết trên Google Drive: [Link Tạo Bản Sao 1-Click], nhớ bật quyền Chia sẻ rồi gửi link cho tôi!"*
* **Việc bạn làm:** Bấm link tạo bản sao ➔ Bấm nút **Chia sẻ** góc phải bảng tính, đổi sang **"Bất kỳ ai có đường liên kết đều có thể xem/chỉnh sửa"** ➔ Copy link gửi cho AI.
* **Thời gian:** 30 giây.

### 🔹 BƯỚC 4: AI HƯỚNG DẪN TẠO GOOGLE CLOUD OAUTH (CLIENT ID & SECRET)
* **AI sẽ nói:** *"Bước 4, chúng ta tạo mã ủy quyền Blogger trên Google Cloud Console. Bạn chỉ cần làm theo 4 thao tác bấm chuột tôi liệt kê dưới đây..."*
* **Việc bạn làm:** Làm theo 4 gạch đầu dòng AI chỉ (Bật Blogger API v3, tạo OAuth Consent Screen với Desktop app, thêm Gmail vào Test Users, bấm Publish App) ➔ Copy **Client ID** và **Client Secret** gửi cho AI.
* **Thời gian:** 2 - 3 phút.

### 🔹 BƯỚC 5: AI KÍCH HOẠT LẤY REFRESH TOKEN (BẠN CHỈ BẤM DUYỆT TRÊN WEB)
* **AI sẽ nói:** *"Tôi đang kích hoạt trình duyệt trên máy bạn để xác thực. Trình duyệt sẽ tự mở trang đăng nhập Google..."*
* **Việc bạn làm:** Chọn Gmail sở hữu Blog ➔ Bấm **Nâng cao (Advanced)** ➔ Bấm **Chuyển đến ứng dụng (không an toàn)** ➔ Bấm **Cho phép (Allow)**.
* **AI làm thay bạn:** AI tự động bắt lấy mã Refresh Token vĩnh viễn và lưu vào bộ nhớ.
* **Thời gian:** 15 giây.

### 🔹 BƯỚC 6: AI TỰ ĐỘNG TẠO FILE `.ENV` HOÀN CHỈNH
* **AI làm thay bạn 100%:** AI tự động tổng hợp toàn bộ các thông số ở trên và ghi trực tiếp vào file `.env` trên máy tính.  
* 👉 **Bạn không cần phải mở file ra xem hay chỉnh sửa bất kỳ ký tự nào!**

### 🔹 BƯỚC 7: AI TỰ ĐỘNG KIỂM TRA & XUẤT BẢN 1 BÀI MẪU
* **AI làm thay bạn 100%:** AI tự kích hoạt chạy script `kiem_tra_ket_noi.py` để đảm bảo các kết nối đều màu xanh, sau đó tự kích hoạt `main.py --sheet` để viết và đăng 1 bài chuẩn SEO mẫu kèm Thumbnail 16:9 sắc nét.
* **Kết quả:** AI gửi ngay đường link bài viết vừa đăng trên Blogger vào khung chat để bạn bấm vào chiêm ngưỡng thành quả!

### 🔹 BƯỚC 8: AI HỖ TRỢ DEPLOY LÊN GITHUB ACTIONS CHẠY 24/7 TRÊN MÂY
* **AI sẽ nói:** *"Nếu bạn muốn tắt máy tính đi ngủ bot vẫn tự động đăng bài mỗi ngày, tôi sẽ hướng dẫn bạn đưa lên GitHub Actions miễn phí trọn đời..."*
* **Việc bạn làm:** Tạo 1 repo riêng tư trên GitHub ➔ Vào mục **Settings ➔ Secrets and variables ➔ Actions** ➔ Dán 6 giá trị bí mật mà AI đã chuẩn bị sẵn theo bảng dưới đây:
  1. `GEMINI_API_KEY`
  2. `BLOGGER_BLOG_ID`
  3. `GOOGLE_CLIENT_ID`
  4. `GOOGLE_CLIENT_SECRET`
  5. `GOOGLE_REFRESH_TOKEN`
  6. `GOOGLE_SHEET_URL`
* Bật quyền **Read and write permissions** ➔ Bấm **Run workflow**!
* **Thời gian:** 2 phút.

---

## 💡 PHẦN 5: CÁC CÂU LỆNH TIỆN ÍCH BẠN CÓ THỂ NHỜ AI LÀM SAU KHI CÀI ĐẶT

Sau khi hệ thống đã hoạt động, Trợ lý AI vẫn luôn là người bạn đồng hành trung thành. Bất cứ khi nào cần, bạn chỉ việc gõ vào khung chat:

1. **Nhờ AI viết và đăng bài ngay:**
   > *"Hãy viết 1 bài chuẩn SEO về chủ đề: 'Bí quyết đầu tư bất động sản 2026' và đăng ngay lên blog giúp tôi nhé!"*
2. **Nhờ AI kiểm tra kết nối:**
   > *"Hãy chạy kiểm tra kết nối xem hệ thống và Google Sheets của tôi còn hoạt động bình thường không."*
3. **Nhờ AI đổi giờ đăng bài tự động trên GitHub:**
   > *"Tôi muốn bot tự động đăng bài lúc 7h00 sáng mỗi ngày, hãy chỉnh lại file workflow giúp tôi."*
4. **Nhờ AI tạo thêm bảng tính đề tài mới:**
   > *"Tôi muốn thêm 50 đề tài về lĩnh vực thời trang vào kế hoạch đăng bài, hãy gợi ý danh sách giúp tôi."*

---

## ❓ PHẦN 6: NHỮNG CÂU HỎI THƯỜNG GẶP CỦA NGƯỜI MỚI (FAQ)

### 1. Dùng Trợ lý AI và hệ thống này có tốn phí hàng tháng không?
* **Hoàn toàn 100% MIỄN PHÍ TRỌN ĐỜI:**
  - Google Gemini API: Có gói Free Tier dồi dào tha hồ viết bài mỗi ngày.
  - Blogger.com: Miễn phí lưu trữ và hosting của Google.
  - Google Cloud Console: Miễn phí OAuth API v3.
  - GitHub Actions: Miễn phí 2.000 phút chạy máy chủ ảo mỗi tháng (trong khi bot chỉ chạy mất khoảng 1-2 phút/ngày).

### 2. Nếu tôi lỡ tắt cửa sổ chat với AI giữa chừng thì sao?
* Không sao cả! Toàn bộ lịch sử trao đổi vẫn còn. Bạn chỉ cần mở lại thư mục và nhắn: *"Chúng ta vừa làm đến Bước [X], hãy tiếp tục hướng dẫn tôi nhé"*, AI sẽ nhận diện ngay và tiếp tục công việc.

### 3. Khóa API và tài khoản của tôi có bị lộ ra ngoài không?
* **Tuyệt đối an toàn:** Các khóa được lưu trữ trong file `.env` trên chính máy tính cá nhân của bạn. Khi đưa lên GitHub, các khóa được mã hóa bảo mật cấp cao bằng cơ chế GitHub Secrets, không ai (kể cả người xem kho lưu trữ) có thể nhìn thấy được.

---

🎉 **Chúc bạn có trải nghiệm tuyệt vời cùng Trợ lý AI và xây dựng hệ thống website tự động triệu view thành công rực rỡ!**

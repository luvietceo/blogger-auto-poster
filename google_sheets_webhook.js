/**
 * Google Apps Script Webhook - Tự động cập nhật Google Sheets & Gửi thông báo Email + Telegram
 * Tương thích 100% với Hệ thống Blogger Auto Cloud Điện Máy & Gia Dụng (mava.luviet.com)
 * 
 * ==============================================================================
 * CẤU HÌNH THÔNG BÁO TELEGRAM & EMAIL
 * ==============================================================================
 */
// Cấu hình Telegram Bot (@BotFather) & Chat ID nhóm nhận thông báo
// LƯU Ý: Để trống TELEGRAM_BOT_TOKEN nếu bạn đã nhận thông báo trực tiếp từ GitHub Actions để tránh bị trùng 2 lần tin nhắn!
var TELEGRAM_BOT_TOKEN = "";
var TELEGRAM_CHAT_ID = "";

// Email nhận thông báo: Điền email nhận thông báo báo cáo xuất bản bài viết (để trống nếu không cần)
var NOTIFICATION_EMAIL = "";

/**
 * ==============================================================================
 * HÀM XỬ LÝ YÊU CẦU POST TỪ GITHUB ACTIONS WEBHOOK
 * ==============================================================================
 */
function doPost(e) {
  // 1. Kiểm tra an toàn: nếu hàm bị gọi bởi trigger "On edit" hoặc không có postData
  if (!e || !e.postData || !e.postData.contents) {
    Logger.log("⚠️ doPost được gọi nhưng không có postData (do kích hoạt nhầm trigger On Edit trong Apps Script). Bỏ qua an toàn.");
    return ContentService.createTextOutput(JSON.stringify({
      status: "ignored",
      message: "Không có dữ liệu HTTP POST. Nếu bạn đang cài Trigger 'Khi chỉnh sửa / On edit' trong mục Triggers của Apps Script, vui lòng xóa trigger đó đi (Webhook hoạt động qua bản Triển khai Web App, không cần Trigger)."
    })).setMimeType(ContentService.MimeType.JSON);
  }

  try {
    var data = JSON.parse(e.postData.contents);
    var ss = SpreadsheetApp.getActiveSpreadsheet();

    // 2. Tìm Sheet thông minh: Tự động nhận diện tab chứa dữ liệu
    var sheet = ss.getSheetByName("Ke_Hoach_Dang_Bai") || 
                ss.getSheetByName("Trang tính1") || 
                ss.getSheetByName("Sheet1") || 
                ss.getSheetByName("Dien_May");
                
    if (!sheet) {
      var allSheets = ss.getSheets();
      for (var sIdx = 0; sIdx < allSheets.length; sIdx++) {
        var checkHeaders = allSheets[sIdx].getRange(1, 1, 2, Math.min(allSheets[sIdx].getLastColumn() || 5, 10)).getValues();
        var foundHeader = false;
        for (var r = 0; r < checkHeaders.length; r++) {
          for (var c = 0; c < checkHeaders[r].length; c++) {
            var txt = (checkHeaders[r][c] || "").toString().toLowerCase();
            if (txt.indexOf("tiêu đề") !== -1 || txt.indexOf("tieu de") !== -1 || txt.indexOf("topic") !== -1) {
              foundHeader = true;
              break;
            }
          }
          if (foundHeader) break;
        }
        if (foundHeader) {
          sheet = allSheets[sIdx];
          break;
        }
      }
    }
    if (!sheet) {
      sheet = ss.getActiveSheet() || ss.getSheets()[0];
    }

    var rows = sheet.getDataRange().getValues();

    // 3. Tự động nhận diện chỉ số các cột theo tiêu đề (Failsafe dynamic header mapping)
    var colTitle = 2;       // Mặc định Cột B (index 2)
    var colStatus = 7;      // Mặc định Cột G (index 7)
    var colPublished = 8;   // Mặc định Cột H (index 8)
    var colUrl = 9;         // Mặc định Cột I (index 9)

    if (rows.length > 0) {
      var headerRow = rows[0];
      for (var c = 0; c < headerRow.length; c++) {
        var h = (headerRow[c] || "").toString().toLowerCase().trim();
        if (h.indexOf("tiêu đề") !== -1 || h.indexOf("tieu de") !== -1 || h.indexOf("topic") !== -1) {
          colTitle = c + 1;
        } else if (h.indexOf("trạng thái") !== -1 || h.indexOf("status") !== -1) {
          colStatus = c + 1;
        } else if (h.indexOf("ngày") !== -1 || h.indexOf("published") !== -1 || h.indexOf("thời gian") !== -1) {
          colPublished = c + 1;
        } else if (h.indexOf("link") !== -1 || h.indexOf("url") !== -1) {
          colUrl = c + 1;
        }
      }
    }

    var targetTopic = (data.topic || "").trim().toLowerCase();
    var rowIndex = data.row_index; // 1-based index từ kịch bản Python

    var matchedRow = -1;

    // 4. Khớp theo rowIndex nếu có
    if (rowIndex && rowIndex <= rows.length) {
      var checkTitle = (rows[rowIndex - 1][colTitle - 1] || "").toString().trim().toLowerCase();
      if (checkTitle === targetTopic || !targetTopic) {
        matchedRow = rowIndex;
      }
    }

    // 5. Tìm theo tiêu đề nếu chưa khớp rowIndex
    if (matchedRow === -1 && targetTopic) {
      for (var i = 1; i < rows.length; i++) {
        var rowTitle = (rows[i][colTitle - 1] || "").toString().trim().toLowerCase();
        if (rowTitle === targetTopic || rowTitle.indexOf(targetTopic) !== -1 || targetTopic.indexOf(rowTitle) !== -1) {
          matchedRow = i + 1;
          break;
        }
      }
    }

    var statusText = data.status || "Đã đăng";
    var publishedTime = data.published || new Date().toLocaleString("vi-VN", { timeZone: "Asia/Ho_Chi_Minh" });
    var postUrl = data.post_url || "";
    var labelsStr = Array.isArray(data.labels) ? data.labels.join(", ") : (data.labels || "tin-tuc");
    var topicTitle = data.topic || (matchedRow > 0 ? rows[matchedRow - 1][colTitle - 1] : "Bài viết mới");

    // 6. Cập nhật Google Sheets khi tìm thấy dòng
    if (matchedRow > 0) {
      // Cột Trạng Thái
      var statusCell = sheet.getRange(matchedRow, colStatus);
      statusCell.setValue(statusText);
      statusCell.setBackground("#DCFCE7"); // Nền xanh lá nhạt
      statusCell.setFontColor("#166534");  // Chữ xanh lá đậm
      statusCell.setFontWeight("bold");

      // Cột Ngày Lên Lịch / Đăng
      sheet.getRange(matchedRow, colPublished).setValue(publishedTime);

      // Cột Link Bài Viết
      if (postUrl) {
        sheet.getRange(matchedRow, colUrl).setValue(postUrl);
      }
    }

    // 7. Gửi thông báo đến Telegram (Bỏ qua nếu skip_telegram = true)
    if (!data.skip_telegram && TELEGRAM_BOT_TOKEN && TELEGRAM_CHAT_ID) {
      try {
        sendTelegramMessage(topicTitle, statusText, postUrl, publishedTime, labelsStr, matchedRow);
      } catch (teleErr) {
        Logger.log("Lỗi gửi Telegram: " + teleErr.toString());
      }
    }

    // 8. Gửi thông báo đến Email
    try {
      sendEmailNotification(topicTitle, statusText, postUrl, publishedTime, labelsStr, matchedRow);
    } catch (mailErr) {
      Logger.log("Lỗi gửi Email: " + mailErr.toString());
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      matched_row: matchedRow,
      topic: topicTitle
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * ==============================================================================
 * HÀM GỬI THÔNG BÁO TELEGRAM
 * ==============================================================================
 */
function sendTelegramMessage(topic, status, postUrl, publishedTime, labels, rowIndex) {
  if (!TELEGRAM_BOT_TOKEN || !TELEGRAM_CHAT_ID) return;

  var url = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN + "/sendMessage";

  var text = "🚀 <b>[BLOGGER AUTO-POSTER] ĐĂNG BÀI THÀNH CÔNG</b>\n\n" +
    "📌 <b>Tiêu đề:</b> " + topic + "\n" +
    "🏷️ <b>Nhãn:</b> <code>" + labels + "</code>\n" +
    "⏰ <b>Thời gian:</b> " + publishedTime + "\n" +
    (rowIndex > 0 ? "📊 <b>Google Sheet:</b> Đã cập nhật dòng #" + rowIndex + " (<b>" + status + "</b>)\n" : "") +
    (postUrl ? "🔗 <b>Link bài viết:</b> <a href=\"" + postUrl + "\">Bấm xem ngay</a>\n" : "") +
    "\n💡 <i>Hệ thống AI Blogger Cloud Siêu Thị Điện Máy & Gia Dụng (mava.luviet.com) đã xử lý hoàn tất!</i>";

  var payload = {
    chat_id: TELEGRAM_CHAT_ID,
    text: text,
    parse_mode: "HTML",
    disable_web_page_preview: false
  };

  var options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  UrlFetchApp.fetch(url, options);
}

/**
 * ==============================================================================
 * HÀM GỬI THÔNG BÁO EMAIL
 * ==============================================================================
 */
function sendEmailNotification(topic, status, postUrl, publishedTime, labels, rowIndex) {
  var recipient = (NOTIFICATION_EMAIL || "").trim();
  if (!recipient) {
    try {
      recipient = Session.getEffectiveUser().getEmail();
    } catch (e) { }
  }
  if (!recipient) {
    Logger.log("⚠️ Không tìm thấy email nhận thông báo! Vui lòng điền vào biến NOTIFICATION_EMAIL.");
    return;
  }

  var subject = "⚡ [Điện Máy Auto-Post] Xuất bản thành công: " + topic;

  var htmlBody =
    '<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">' +
    '<div style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); padding: 24px; color: #ffffff; text-align: center;">' +
    '<h2 style="margin: 0; font-size: 20px;">⚡ Siêu Thị Điện Máy & Gia Dụng: Báo Cáo Xuất Bản</h2>' +
    '<p style="margin: 6px 0 0; opacity: 0.9; font-size: 14px;">Hệ thống AI Tự Động Hóa Blogger (mava.luviet.com)</p>' +
    '</div>' +
    '<div style="padding: 24px; background: #ffffff;">' +
    '<p style="font-size: 15px; color: #334155; line-height: 1.6;">Xin chào, hệ thống vừa xuất bản và lên lịch thành công một bài viết điện máy mới:</p>' +
    '<div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 16px; margin: 18px 0; border-radius: 4px;">' +
    '<p style="margin: 0 0 10px; font-size: 16px; font-weight: bold; color: #0f172a;">📌 ' + topic + '</p>' +
    '<p style="margin: 6px 0; font-size: 14px; color: #334155;">🏷️ <b>Nhãn chuyên mục:</b> <span style="background: #e0f2fe; color: #0369a1; padding: 3px 8px; border-radius: 4px; font-weight: 600;">' + labels + '</span></p>' +
    '<p style="margin: 6px 0; font-size: 14px; color: #334155;">⏰ <b>Thời gian:</b> ' + publishedTime + '</p>' +
    (rowIndex > 0 ? '<p style="margin: 6px 0; font-size: 14px; color: #334155;">📊 <b>Google Sheet:</b> Đã cập nhật dòng #' + rowIndex + ' (<b>' + status + '</b>)</p>' : '') +
    '</div>' +
    (postUrl ?
      '<div style="text-align: center; margin-top: 25px;">' +
      '<a href="' + postUrl + '" target="_blank" style="background: #0284c7; color: #ffffff; font-weight: bold; padding: 12px 25px; border-radius: 8px; text-decoration: none; display: inline-block; box-shadow: 0 4px 10px rgba(2, 132, 199, 0.3);">👉 Bấm Xem Bài Viết Ngay</a>' +
      '</div>' : '') +
    '</div>' +
    '<div style="background: #f1f5f9; padding: 14px; text-align: center; font-size: 12px; color: #64748b;">' +
    'Hệ thống tự động hóa nội dung & Website Điện Máy thông minh mava.luviet.com' +
    '</div>' +
    '</div>';

  MailApp.sendEmail({
    to: recipient,
    subject: subject,
    htmlBody: htmlBody
  });
  Logger.log("✅ Đã gửi email thông báo thành công tới: " + recipient);
}

/**
 * ==============================================================================
 * HÀM TEST TRỰC TIẾP TRÊN APPS SCRIPT
 * ==============================================================================
 */
function testNotification() {
  var testTopic = "Top 5 Tủ Lạnh Inverter Tiết Kiệm Điện Bán Chạy Nhất 2026";
  var testStatus = "Đã lên lịch";
  var testUrl = "https://mava.luviet.com";
  var testTime = new Date().toLocaleString("vi-VN", { timeZone: "Asia/Ho_Chi_Minh" });
  var testLabels = "tin-tuc, tu-van-chon-mua";

  sendTelegramMessage(testTopic, testStatus, testUrl, testTime, testLabels, 2);
  sendEmailNotification(testTopic, testStatus, testUrl, testTime, testLabels, 2);
  Logger.log("✅ Đã gửi thông báo test thành công tới Telegram & Email!");
}

function doGet(e) {
  return ContentService.createTextOutput("✅ Blogger Google Sheets Webhook Điện Máy đang hoạt động bình thường! Tự động cập nhật 2 chiều Google Sheets & gửi thông báo.").setMimeType(ContentService.MimeType.TEXT);
}

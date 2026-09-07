// Google Apps Script — VIP Form Backend
// Deploy as: Web App → Execute as: Me → Who has access: Anyone
//
// Setup:
// 1. Go to https://script.google.com and create a new project
// 2. Paste this code
// 3. Create a Google Sheet and copy its ID from the URL
// 4. Replace SPREADSHEET_ID below with your Sheet ID
// 5. Deploy → New deployment → Web app → Execute as Me → Anyone
// 6. Copy the deployment URL and paste it into index.html (replace APPS_SCRIPT_URL_PLACEHOLDER)

const SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID_HERE';
const SHEET_NAME = 'VIP申請';

/**
 * Handle GET requests — simple health check
 */
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'ok', message: 'Markforged GCR VIP Form API is running.' }))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * Handle POST requests — receive form data and write to sheet
 */
function doPost(e) {
  try {
    var ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    var sheet = ss.getSheetByName(SHEET_NAME);

    // Create sheet with headers if it doesn't exist
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow([
        '時間戳記',
        '姓名',
        '公司名稱',
        '職稱',
        'Email',
        '手機號碼',
        '公司規模',
        '偏好體驗地點',
        '產業別',
        '目前零件製造方式',
        '感興趣的應用場景',
        '預計導入時程',
        '預算範圍'
      ]);
      // Bold header row
      sheet.getRange(1, 1, 1, 13).setFontWeight('bold');
    }

    // Parse form data
    var params = e.parameter;

    // Append row with timestamp
    sheet.appendRow([
      new Date().toLocaleString('zh-TW', { timeZone: 'Asia/Taipei' }),
      params.name || '',
      params.company || '',
      params.title || '',
      params.email || '',
      params.phone || '',
      params.company_size || '',
      params.location || '',
      params.industry || '',
      params.manufacturing || '',
      params.application || '',
      params.timeline || '',
      params.budget || ''
    ]);

    // Return success response with CORS headers
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'success', message: '表單已成功送出' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'error', message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

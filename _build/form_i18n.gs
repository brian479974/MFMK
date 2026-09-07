/**
 * Markforged GCR VIP 體驗申請表 — 中英雙語補齊（2026-09-07）
 *
 * 現況：表單標題、說明、以及 6 題共 34 個選項只有中文；題目標題本身已是中英。
 * 本腳本把缺的英文補上，格式一律「中文 English」，不動題型、不動必填設定、不動既有回覆。
 *
 * 怎麼跑（一次就好）：
 *   1. 用 brian479974@gmail.com 開 https://script.google.com → 新增專案
 *   2. 貼上本檔全部內容 → 儲存
 *   3. 執行 applyBilingual()（第一次會要求授權，允許即可）
 *   4. 執行紀錄會印出改了幾處；回表單確認後即可
 *
 * 要還原：執行 restoreChinese()（把選項換回純中文，標題說明還原）
 */

var FORM_ID = '1QVoS_NBUD8-cVzbirNctZfZ6z5vNOSF02_7hHejYFZk';

var TITLE_ZH = 'Markforged GCR VIP 體驗申請';
var TITLE_BI = 'Markforged GCR VIP 體驗申請 | VIP Experience Request';

var DESC_ZH = '感謝您對 Markforged 的興趣！請填寫以下資訊，我們的團隊將在 3 個工作日內與您聯繫。';
var DESC_BI = '感謝您對 Markforged 的興趣！請填寫以下資訊，我們的團隊將在 3 個工作日內與您聯繫。\n' +
              'Thank you for your interest in Markforged. Please complete the form below and our team will contact you within three working days.';

/** 中文選項 → 中英選項（key 必須與表單上現有文字完全一致） */
var CHOICES = {
  // Q6 公司規模 Company Size
  '50人以下': '50 人以下 Fewer than 50',
  '51-200人': '51–200 人 51–200',
  '201-500人': '201–500 人 201–500',
  '500人以上': '500 人以上 More than 500',

  // Q7 偏好體驗地點 Preferred Location
  '台灣北部台北': '台灣北部 台北 Northern Taiwan · Taipei',
  '台灣中部台中': '台灣中部 台中 Central Taiwan · Taichung',
  '台灣南部高雄': '台灣南部 高雄 Southern Taiwan · Kaohsiung',
  '中國華東上海': '中國華東 上海 East China · Shanghai',
  '中國華南深圳': '中國華南 深圳 South China · Shenzhen',
  '香港': '香港 Hong Kong',
  '越南胡志明市': '越南 胡志明市 Viet Nam · Ho Chi Minh City',
  '線上展示': '線上展示 Online demonstration',

  // Q8 產業別 Industry
  '汽車與交通': '汽車與交通 Automotive and transport',
  '航太與國防': '航太與國防 Aerospace and defence',
  '醫療與生技': '醫療與生技 Medical and life sciences',
  '精密機械與模具': '精密機械與模具 Precision machinery and tooling',
  '電子與半導體': '電子與半導體 Electronics and semiconductor',
  '能源與重工業': '能源與重工業 Energy and heavy industry',
  '學術與研究機構': '學術與研究機構 Academic and research',

  // Q9 目前零件製造方式 Current Manufacturing
  '完全自製': '完全自製 All in house',
  '完全外包': '完全外包 All outsourced',
  '自製加外包並行': '自製與外包並行 Mixed in house and outsourced',
  '尚無固定製程': '尚無固定製程 No settled process yet',

  // Q10 預計導入時程 Timeline
  '3個月內': '3 個月內 Within 3 months',
  '6個月內': '6 個月內 Within 6 months',
  '1年內': '1 年內 Within 12 months',
  '評估中尚未確定': '評估中，尚未確定 Still evaluating',

  // Q11 預算範圍 Budget（幣別依 mfmk 頁面與台灣案場慣例標為 NT$；若要改成 USD 改這五行即可）
  '100萬以下': 'NT$100 萬以下 Under NT$1M',
  '100萬到300萬': 'NT$100 萬–300 萬 NT$1M–3M',
  '300萬到500萬': 'NT$300 萬–500 萬 NT$3M–5M',
  '500萬以上': 'NT$500 萬以上 Over NT$5M',
  '尚未確認': '尚未確認 Not yet determined',

  // 兩題共用
  '其他': '其他 Other'
};

function applyBilingual() {
  var form = FormApp.openById(FORM_ID);
  var changed = 0;

  if (form.getTitle() === TITLE_ZH) { form.setTitle(TITLE_BI); changed++; }
  if (form.getDescription() === DESC_ZH) { form.setDescription(DESC_BI); changed++; }

  changed += rewriteChoices_(form, CHOICES);
  Logger.log('完成，共更新 ' + changed + ' 處。表單網址：' + form.getPublishedUrl());
}

/** 還原：把中英選項換回原本的純中文 */
function restoreChinese() {
  var form = FormApp.openById(FORM_ID);
  var back = {};
  for (var zh in CHOICES) { back[CHOICES[zh]] = zh; }
  var changed = rewriteChoices_(form, back);
  if (form.getTitle() === TITLE_BI) { form.setTitle(TITLE_ZH); changed++; }
  if (form.getDescription() === DESC_BI) { form.setDescription(DESC_ZH); changed++; }
  Logger.log('已還原 ' + changed + ' 處。');
}

/** 共用：逐題重寫選項；只改文字，不動題型與必填 */
function rewriteChoices_(form, map) {
  var changed = 0;
  form.getItems().forEach(function (item) {
    var type = item.getType();
    var q = null;
    if (type === FormApp.ItemType.MULTIPLE_CHOICE) q = item.asMultipleChoiceItem();
    else if (type === FormApp.ItemType.LIST) q = item.asListItem();
    else if (type === FormApp.ItemType.CHECKBOX) q = item.asCheckboxItem();
    if (!q) return;

    var current = q.getChoices().map(function (c) { return c.getValue(); });
    var next = current.map(function (v) { return map[v] || v; });
    var hit = next.some(function (v, i) { return v !== current[i]; });
    if (!hit) return;

    q.setChoiceValues(next);
    changed += next.filter(function (v, i) { return v !== current[i]; }).length;
    Logger.log('  ' + item.getTitle() + '：' + current.length + ' 個選項已更新');
  });
  return changed;
}

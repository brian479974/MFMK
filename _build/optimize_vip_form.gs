/**
 * Markforged VIP 體驗申請表 — 優化（2026-10-31）
 * 表單在 Brian 個人帳號 brian479974@gmail.com，只有他有權限 → 用個人帳號開 script.google.com 執行一次。
 *
 * 執行 optimizeVipForm() 會做六件事（都不動既有題目的代號，網頁送進來的資料不受影響）：
 *   1. 標題拿掉內部代號 GCR → 「Markforged VIP 體驗申請 | VIP Experience Request」
 *   2. 姓名改必填（現在是選填，名單會出現沒有名字的列）
 *   3. 產業別加一個選項「無人機與無人載具 UAV and uncrewed systems」
 *   4. 新增選填題「您從哪裡得知 How did you hear about us」
 *   5. 新增選填複選題「想了解的主題 Topics of interest」
 *   6. 每有一筆新申請，寄通知信到 brian.chen@markforged.com（主旨帶公司、姓名）
 * 重複執行不會重複加題、不會重複建通知。
 */

var FORM_ID = '1QVoS_NBUD8-cVzbirNctZfZ6z5vNOSF02_7hHejYFZk';
var NOTIFY = 'brian.chen@markforged.com';

function optimizeVipForm() {
  var form = FormApp.openById(FORM_ID);
  var done = [];

  form.setTitle('Markforged VIP 體驗申請 | VIP Experience Request');
  done.push('標題已改（拿掉 GCR）');

  var items = form.getItems();
  var byTitle = function (t) {
    for (var i = 0; i < items.length; i++) if (items[i].getTitle() === t) return items[i];
    return null;
  };

  var name = byTitle('姓名 Name');
  if (name) { name.asTextItem().setRequired(true); done.push('姓名改必填'); }

  var ind = byTitle('產業別 Industry');
  if (ind) {
    var UAV = '無人機與無人載具 UAV and uncrewed systems';
    var li = ind.getType() === FormApp.ItemType.LIST ? ind.asListItem() : ind.asMultipleChoiceItem();
    var vals = li.getChoices().map(function (c) { return c.getValue(); });
    if (vals.indexOf(UAV) < 0) {
      var pos = vals.indexOf('航太與國防 Aerospace and defence');
      vals.splice(pos >= 0 ? pos + 1 : vals.length - 1, 0, UAV);
      li.setChoiceValues(vals);
      done.push('產業別加「無人機與無人載具」');
    }
  }

  if (!byTitle('您從哪裡得知 How did you hear about us')) {
    form.addListItem().setTitle('您從哪裡得知 How did you hear about us').setRequired(false).setChoiceValues([
      'Markforged 新聞中心文章 Markforged newsroom article',
      '非紅自我檢核 Non-red self-check',
      'Markforged 官方 LINE',
      '業務或經銷夥伴 Sales rep or partner',
      '展會或研討會 Trade show or seminar',
      '搜尋引擎 Search engine',
      '其他 Other'
    ]);
    done.push('新增「您從哪裡得知」');
  }

  if (!byTitle('想了解的主題 Topics of interest')) {
    form.addCheckboxItem().setTitle('想了解的主題 Topics of interest').setRequired(false).setChoiceValues([
      '非紅供應鏈與國防應用 Non-red supply chain and defence',
      '無人機結構件 Drone structures',
      '夾治具 Jigs and fixtures',
      '金屬零件（FX10 + Metal Kit）Metal parts',
      '備品與停產零件 Spares and discontinued parts',
      '設備實機體驗 Hands-on demo'
    ]);
    done.push('新增「想了解的主題」');
  }

  form.setConfirmationMessage('感謝您的申請！我們會在 3 個工作天內與您聯繫。\n' +
                              'Thank you. We will contact you within three working days.');
  done.push('送出後的感謝訊息已更新');

  var has = ScriptApp.getProjectTriggers().some(function (t) { return t.getHandlerFunction() === 'notifyNewRequest'; });
  if (!has) {
    ScriptApp.newTrigger('notifyNewRequest').forForm(form).onFormSubmit().create();
    done.push('新申請通知已開（寄 ' + NOTIFY + '）');
  }

  Logger.log(done.join('\n'));
  MailApp.sendEmail(NOTIFY, '[完成] VIP 體驗申請表優化', done.join('\n') + '\n\n表單：' + form.getPublishedUrl());
}

/** 每一筆新申請寄一封通知（只寄 Brian 公司信箱） */
function notifyNewRequest(e) {
  var got = {};
  e.response.getItemResponses().forEach(function (ir) {
    var v = ir.getResponse();
    got[ir.getItem().getTitle()] = Array.isArray(v) ? v.join('; ') : v;
  });
  var lines = Object.keys(got).map(function (k) { return k + '：' + got[k]; });
  MailApp.sendEmail(NOTIFY,
    '【VIP 體驗申請】新申請：' + (got['公司名稱 Company Name'] || '') + '｜' + (got['姓名 Name'] || ''),
    lines.join('\n'));
}

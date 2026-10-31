import json, re
from pathlib import Path
M = Path.home()/"MFMK-redesign"
ACTION = "https://docs.google.com/forms/d/e/1FAIpQLScUzpAD5-p6okBrxFujaKvL6O7LnIqn-fd9mUUTqGhy7-HVaQ/formResponse"
# (id, entry, kind, 繁中題目, 英文題目, required, [(繁中顯示, 英文顯示, 送出值＝表單選項原文)])
Q = [
 ("loc","entry.1661346594","radio","偏好體驗地點","Preferred location",False,[
   ("台灣北部 台北","Northern Taiwan · Taipei","台灣北部 台北 Northern Taiwan · Taipei"),
   ("台灣中部 台中","Central Taiwan · Taichung","台灣中部 台中 Central Taiwan · Taichung"),
   ("台灣南部 高雄","Southern Taiwan · Kaohsiung","台灣南部 高雄 Southern Taiwan · Kaohsiung"),
   ("中國華東 上海","East China · Shanghai","中國華東 上海 East China · Shanghai"),
   ("中國華南 深圳","South China · Shenzhen","中國華南 深圳 South China · Shenzhen"),
   ("香港","Hong Kong","香港 Hong Kong"),
   ("越南 胡志明市","Viet Nam · Ho Chi Minh City","越南 胡志明市 Viet Nam · Ho Chi Minh City"),
   ("線上展示","Online demonstration","線上展示 Online demonstration"),
   ("其他地點","Other location","其他 Other")]),
 ("ind","entry.702564806","radio","產業別","Industry",False,[
   ("汽車與交通","Automotive and transport","汽車與交通 Automotive and transport"),
   ("航太與國防","Aerospace and defence","航太與國防 Aerospace and defence"),
   ("無人機與無人載具","UAV and uncrewed systems","無人機與無人載具 UAV and uncrewed systems"),
   ("醫療與生技","Medical and life sciences","醫療與生技 Medical and life sciences"),
   ("精密機械與模具","Precision machinery and tooling","精密機械與模具 Precision machinery and tooling"),
   ("電子與半導體","Electronics and semiconductor","電子與半導體 Electronics and semiconductor"),
   ("能源與重工業","Energy and heavy industry","能源與重工業 Energy and heavy industry"),
   ("學術與研究機構","Academic and research","學術與研究機構 Academic and research"),
   ("其他產業","Other industry","其他 Other")]),
 ("size","entry.1927766727","radio","公司規模","Company size",False,[
   ("50 人以下","Fewer than 50","50 人以下 Fewer than 50 employees"),
   ("51–200 人","51–200","51–200 人 51–200 employees"),
   ("201–500 人","201–500","201–500 人 201–500 employees"),
   ("500 人以上","More than 500","500 人以上 More than 500 employees")]),
 ("mfg","entry.1554625665","radio","目前零件怎麼做","How parts are made today",False,[
   ("完全自製","All in house","完全自製 All in house"),
   ("完全外包","All outsourced","完全外包 All outsourced"),
   ("自製與外包並行","Mixed","自製與外包並行 Mixed in house and outsourced"),
   ("尚無固定製程","No settled process yet","尚無固定製程 No settled process yet")]),
 ("time","entry.615165058","radio","預計導入時程","Timeline",False,[
   ("3 個月內","Within 3 months","3 個月內 Within 3 months"),
   ("6 個月內","Within 6 months","6 個月內 Within 6 months"),
   ("1 年內","Within 12 months","1 年內 Within 12 months"),
   ("評估中","Still evaluating","評估中，尚未確定 Still evaluating")]),
 ("topic","entry.543041358","check","想了解的主題（可複選）","Topics of interest (select all that apply)",False,[
   ("非紅供應鏈與國防應用","Non-red supply chain and defence","非紅供應鏈與國防應用 Non-red supply chain and defence"),
   ("無人機結構件","Drone structures","無人機結構件 Drone structures"),
   ("夾治具","Jigs and fixtures","夾治具 Jigs and fixtures"),
   ("金屬零件（FX10 + Metal Kit）","Metal parts (FX10 + Metal Kit)","金屬零件（FX10 + Metal Kit）Metal parts"),
   ("備品與停產零件","Spares and discontinued parts","備品與停產零件 Spares and discontinued parts"),
   ("設備實機體驗","Hands-on demo","設備實機體驗 Hands-on demo")]),
 ("budget","entry.1823419522","radio","預算範圍（選填）","Budget (optional)",False,[
   ("NT$100 萬以下","Under NT$1M","NT$100 萬以下 Under NT$1M"),
   ("NT$100–300 萬","NT$1M–3M","NT$100 萬–300 萬 NT$1M–3M"),
   ("NT$300–500 萬","NT$3M–5M","NT$300 萬–500 萬 NT$3M–5M"),
   ("NT$500 萬以上","Over NT$5M","NT$500 萬以上 Over NT$5M"),
   ("尚未確認","Not yet determined","尚未確認 Not yet determined")]),
 ("src","entry.521954915","radio","您從哪裡得知（選填）","How did you hear about us (optional)",False,[
   ("Markforged 新聞中心文章","Markforged newsroom article","Markforged 新聞中心文章 Markforged newsroom article"),
   ("非紅自我檢核","Non-red self-check","非紅自我檢核 Non-red self-check"),
   ("Markforged 官方 LINE","Markforged LINE","Markforged 官方 LINE"),
   ("業務或經銷夥伴","Sales rep or partner","業務或經銷夥伴 Sales rep or partner"),
   ("展會或研討會","Trade show or seminar","展會或研討會 Trade show or seminar"),
   ("搜尋引擎","Search engine","搜尋引擎 Search engine"),
   ("其他管道","Other channel","其他 Other")]),
]
CONTACT = [("name","entry.2047457802","姓名","Name",True,"text"),("company","entry.1109148177","公司名稱","Company",True,"text"),
           ("title","entry.39817803","職稱","Job title",False,"text"),("email","entry.1534245742","Email","Email",True,"email"),
           ("phone","entry.586431209","電話","Phone",True,"tel")]
NOTE = ("note","entry.1436149164","想看的應用或零件（選填）","Applications or parts you want to see (optional)")
TX = dict(
  h=("申請 VIP 體驗名額","Request a VIP place"),
  sub=("約一分鐘。原廠工程師會依您的產業與零件準備一對一展示，3 個工作天內與您聯繫。","About one minute. Our engineers prepare a one-to-one demonstration around your industry and parts, and contact you within three working days."),
  needs=("您的需求","Your needs"),
  contact=("聯絡資料","Contact details"),
  consent=("我同意 Markforged 使用以上資料與我聯繫，並依隱私權政策處理。","I agree that Markforged may use these details to contact me, in line with its privacy policy."),
  submit=("送出 VIP 申請 →","Send my VIP request →"),
  sending=("送出中…","Sending…"),
  err=("請填寫姓名、公司名稱、Email、電話，並勾選同意。","Please fill in your name, company, email and phone, and tick the consent box."),
  ok_h=("已收到您的申請","Request received"),
  ok_p=("謝謝！Markforged 會在 3 個工作天內與您聯繫，確認體驗時間與地點。也歡迎加入官方 LINE @markforged。","Thank you. Markforged will contact you within three working days to confirm the time and place."),
  net=("網路不穩定，資料可能沒有送出，請稍後再送一次。","The connection is unstable and your request may not have been sent. Please try again shortly."),
  alt=("或改用 Google 表單填寫","Or use the Google Form instead"),
)
EN = {}
def t(pair):
    EN[pair[0]] = pair[1]; return pair[0]
VALS = {}
fs = ""
for qid, ent, kind, qt, qe, req, opts in Q:
    typ = "radio" if kind == "radio" else "checkbox"
    VALS[qid] = {"e": ent, "v": [o[2] for o in opts], "multi": kind != "radio"}
    pills = "".join(f'<label><input type="{typ}" name="{qid}" value="{i}"><span>{t((o[0],o[1]))}</span></label>' for i,o in enumerate(opts))
    fs += f'<fieldset class="vf-q"><legend>{t((qt,qe))}</legend><div class="vf-opts">{pills}</div></fieldset>\n'
ct = "".join(f'<label>{t((lt,le))}{" *" if req else ""}<input name="{cid}" type="{ty}"{" required" if req else ""} autocomplete="on"></label>' for cid,ent,lt,le,req,ty in CONTACT)
VALS["_contact"] = {cid: ent for cid,ent,*_ in CONTACT}
VALS["_note"] = NOTE[1]
html = f'''<section class="form-section" id="register">
  <div class="form-wrap reveal">
    <div class="form-head">
      <div>
        <h2>{t(TX["h"])}</h2>
        <p>{t(TX["sub"])}</p>
      </div>
      <div class="form-head-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" ><path d="M7 4h10v5a5 5 0 0 1-10 0Z"/><path d="M7 6H4.5a2.5 2.5 0 0 0 2.5 4M17 6h2.5a2.5 2.5 0 0 1-2.5 4"/><path d="M10 14h4l-.5 4h-3Z"/><path d="M8.5 20h7"/></svg></div>
    </div>
    <form class="vf" id="vipForm" novalidate>
      <div class="vf-sec">{t(TX["needs"])}</div>
{fs}      <fieldset class="vf-q"><legend>{t((NOTE[2],NOTE[3]))}</legend><textarea name="note" rows="2"></textarea></fieldset>
      <div class="vf-sec">{t(TX["contact"])}</div>
      <div class="vf-ct">{ct}</div>
      <label class="vf-cs"><input type="checkbox" name="consent" value="1"><span>{t(TX["consent"])}</span></label>
      <button type="submit" class="vf-btn" id="vfBtn">{t(TX["submit"])}</button>
      <div class="vf-err" id="vfErr"></div>
      <a class="vf-alt" href="https://docs.google.com/forms/d/1QVoS_NBUD8-cVzbirNctZfZ6z5vNOSF02_7hHejYFZk/viewform" target="_blank" rel="noopener">{t(TX["alt"])}</a>
    </form>
    <div class="vf-ok" id="vfOk"><div class="vf-ok-h">{t(TX["ok_h"])}</div><p>{t(TX["ok_p"])}</p></div>
    <div hidden id="vfTx" data-sending="{t(TX["sending"])}" data-err="{t(TX["err"])}" data-net="{t(TX["net"])}"></div>
  </div>
</section>'''
js = """<script>
/* VIP 申請表（2026-10-31 Brian「原來 VIP 的問卷很醜，要優化類似非紅表格依樣設計」）：頁內作答 → 直接寫進同一張 VIP Google 表單 */
(function(){
var A="%s", V=%s;
var f=document.getElementById('vipForm'); if(!f) return;
var T=document.getElementById('vfTx').dataset, b=document.getElementById('vfBtn'), er=document.getElementById('vfErr');
try{var q=new URLSearchParams(location.search);
  if((q.get('utm_campaign')||'').indexOf('non-red')>=0){
    var s=f.querySelector('input[name="src"][value="1"]'); if(s) s.checked=true;
    var tp=f.querySelector('input[name="topic"][value="0"]'); if(tp) tp.checked=true;}}catch(e){}
f.addEventListener('submit',function(ev){
  ev.preventDefault(); er.style.display='none';
  var C=V._contact, val=function(n){return (f.elements[n].value||'').trim();};
  if(!val('name')||!val('company')||!val('phone')||!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(val('email'))||!f.elements.consent.checked){
    er.textContent=T.err; er.style.display='block'; return;}
  var p=new URLSearchParams();
  Object.keys(C).forEach(function(k){p.append(C[k],val(k));});
  if(val('note')) p.append(V._note,val('note'));
  Object.keys(V).forEach(function(k){ if(k.charAt(0)==='_') return;
    [].forEach.call(f.querySelectorAll('input[name="'+k+'"]:checked'),function(x){p.append(V[k].e,V[k].v[+x.value]);});});
  b.disabled=true; b.textContent=T.sending;
  try{fetch('https://hits.sh/mfmk.markforged.tw/vip-submit.svg?_='+Date.now(),{mode:'no-cors'}).catch(function(){});}catch(e){}
  fetch(A,{method:'POST',mode:'no-cors',body:p}).then(function(){
    f.style.display='none'; document.getElementById('vfOk').style.display='block';
    document.getElementById('register').scrollIntoView({behavior:'smooth',block:'start'});
  }).catch(function(){ b.disabled=false; er.textContent=T.net; er.style.display='block'; });
});
})();
</script>""" % (ACTION, json.dumps(VALS, ensure_ascii=True))
css = """
    /* ── VIP 頁內申請表（2026-10-31，同非紅自我檢核設計）── */
    .vf { padding: 30px 40px 34px; }
    .vf-sec { color: var(--yellow); font-size: 12px; font-weight: 900; letter-spacing: 2px; margin: 8px 0 6px; }
    .vf-q { border: 0; border-top: 1px solid #222; padding: 16px 0 12px; margin: 0; }
    .vf-q legend { color: #fff; font-size: 15px; font-weight: 800; padding: 0; margin-bottom: 10px; }
    .vf-opts { display: flex; flex-wrap: wrap; gap: 8px; }
    .vf-opts label { display: inline-flex; align-items: center; gap: 6px; border: 1px solid #444; border-radius: 22px;
      padding: 8px 14px; color: #ccc; font-size: 13.5px; cursor: pointer; transition: all .15s; }
    .vf-opts label:hover { border-color: var(--yellow); color: #fff; }
    .vf-opts input { position: absolute; opacity: 0; pointer-events: none; }
    .vf-opts label:has(input:checked) { background: var(--yellow); border-color: var(--yellow); color: #000; font-weight: 800; }
    .vf textarea, .vf-ct input { width: 100%; background: #111; border: 1px solid #333; border-radius: 6px; color: #fff;
      font-size: 15px; padding: 11px 12px; font-family: inherit; }
    .vf textarea:focus, .vf-ct input:focus { outline: none; border-color: var(--yellow); }
    .vf-ct { display: grid; grid-template-columns: 1fr 1fr; gap: 12px 14px; padding: 12px 0 4px; border-top: 1px solid #222; }
    .vf-ct label { color: #aaa; font-size: 12.5px; font-weight: 700; display: flex; flex-direction: column; gap: 6px; }
    .vf-cs { display: flex; gap: 10px; align-items: flex-start; color: #999; font-size: 12.5px; line-height: 1.6; margin: 16px 0 6px; }
    .vf-cs input { margin-top: 3px; accent-color: #FFFF00; }
    .vf-btn { margin-top: 14px; width: 100%; background: var(--yellow); color: #000; border: 0; border-radius: 6px; font-size: 17px;
      font-weight: 900; padding: 18px; cursor: pointer; letter-spacing: 1px; }
    .vf-btn:disabled { opacity: .6; cursor: wait; }
    .vf-err { display: none; color: #ff6b6b; font-size: 13px; font-weight: 700; margin-top: 10px; }
    .vf-alt { display: block; text-align: center; color: #666; font-size: 12px; margin-top: 16px; }
    .vf-ok { display: none; padding: 46px 40px; text-align: center; }
    .vf-ok-h { color: var(--yellow); font-size: 24px; font-weight: 900; margin-bottom: 10px; }
    .vf-ok p { color: #ccc; font-size: 15px; line-height: 1.8; }
    @media (max-width: 768px) { .vf { padding: 22px 18px 26px; } .vf-ct { grid-template-columns: 1fr; } }
"""
h = (M/"index.html").read_text("utf-8")
h = re.sub(r'<section class="form-section" id="register">.*?</section>', html, h, count=1, flags=re.S)
if "VIP 頁內申請表" not in h:
    h = h.replace("    /* ── FOOTER ── */", css + "\n    /* ── FOOTER ── */", 1)
h = re.sub(r'<script>\n/\* VIP 申請表.*?</script>\n', '', h, flags=re.S)
h = h.replace("</body>", js + "\n</body>", 1)
(M/"index.html").write_text(h, "utf-8")
# 英文對照：拿掉舊申請區的六條、加新條目
p = M/"_build/i18n.py"; s = p.read_text("utf-8")
for old in ["點擊下方按鈕填寫申請表，Markforged 將在 3 個工作日內與您聯繫確認。","填寫您的基本資料及需求，我們的原廠工程師將為您安排專屬一對一展示。",
            "名額有限，歡迎盡早申請。","立即填寫 VIP 申請表","點擊後將開啟申請表單"]:
    s = re.sub(r'\n    "' + re.escape(old) + r'":\s*\n?\s*"[^"]*",', "", s)
add = "    # ── 2026-10-31 VIP 頁內申請表\n" + "".join(f'    {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},\n' for k,v in EN.items() if f'"{k}":' not in s)
if "VIP 頁內申請表" not in s:
    k = s.index("\n}\n", s.index("EN = {")); s = s[:k] + "\n" + add.rstrip("\n") + s[k:]
p.write_text(s, "utf-8")
print("ok", len(EN), "strings")

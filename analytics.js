/* news.markforged.tw — 頁面瀏覽計數
 *
 * 2026-09-07。為什麼是 hits.sh 而不是 GA4：
 *   本站託管於 GitHub Pages（無伺服器日誌），網域在 HiNet 而非 Cloudflare
 *   （無邊緣統計）。GA4 與 Cloudflare 都需要 Brian 另外開帳號拿識別碼，
 *   而他要的是「現在就能知道數字」。hits.sh 免註冊、免 cookie、只回傳一個
 *   計數，即刻可用。GA4／Cloudflare 的掛法留在下方，日後要換只改 PROVIDER。
 *
 * 計兩種數：
 *   <page>        每次載入 +1     → 總瀏覽次數
 *   <page>-uniq   每個瀏覽器 +1   → 不重複瀏覽器（用 localStorage 記已計過）
 *
 * 隱私：不放 cookie、不送任何個人資料、不做跨站識別，只增加一個計數器。
 *      localStorage 僅存一個布林旗標，屬第一方。尊重 DNT / GPC。
 *
 * 已知限制：
 *   · hits.sh 是第三方免費服務，可用性不在我們控制之內。
 *   · 中國能否連通未經實測；CN 讀者可能計不到。
 *   · 計的是瀏覽器不是人；同一人多裝置會重複計。
 */
(function () {
  "use strict";

  var PROVIDER = "hits";   // "hits" | "ga4" | "cloudflare" | "none"
  var GA4_ID = "";
  var CF_TOKEN = "";
  var HOST = "mfmk.markforged.tw";

  var dnt = navigator.doNotTrack === "1" || window.doNotTrack === "1" ||
            navigator.msDoNotTrack === "1" ||
            navigator.globalPrivacyControl === true;
  if (dnt || PROVIDER === "none") { return; }

  function page() {
    var p = (location.pathname || "/").replace(/^\/+/, "");
    return p || "index.html";
  }

  function bump(key) {
    try {
      var url = "https://hits.sh/" + HOST + "/" + key + ".svg?_=" + Date.now();
      if (window.fetch) {
        fetch(url, { mode: "no-cors", cache: "no-store", keepalive: true })
          .catch(function () {});
      } else {
        var i = new Image();
        i.src = url;
      }
    } catch (e) { /* 靜默：計數失敗不影響閱讀 */ }
  }

  if (PROVIDER === "hits") {
    var p = page();
    bump(p);                                   // 總瀏覽
    try {
      var k = "mf_seen_" + p;
      if (!window.localStorage.getItem(k)) {
        window.localStorage.setItem(k, "1");
        bump(p.replace(/\.html$/, "") + "-uniq");   // 不重複瀏覽器
      }
    } catch (e) { /* 無痕模式沒有 localStorage，只計總數 */ }
    // 2026-10-06：依來源分帳。hits.sh 以 key 計數、看不到 query string，
    // 所以帶 utm_source 的進站另外記一個 key：<page>~<source>-<medium>（總數）
    // 與 <page>~<source>-<medium>-uniq（不重複）。沒帶 utm 的流量照舊，不受影響。
    try {
      var q = new URLSearchParams(location.search || "");
      var clean = function (v) { return (v || "").toLowerCase().replace(/[^a-z0-9_]/g, "").slice(0, 24); };
      var src = clean(q.get("utm_source")), med = clean(q.get("utm_medium"));
      if (src) {
        var sk = p.replace(/\.html$/, "") + "~" + src + (med ? "-" + med : "");
        bump(sk);
        var k2 = "mf_seen_" + sk;
        if (!window.localStorage.getItem(k2)) {
          window.localStorage.setItem(k2, "1");
          bump(sk + "-uniq");
        }
      }
    } catch (e) { /* 舊瀏覽器沒有 URLSearchParams：只計頁面總數 */ }
    return;
  }

  function load(src, attrs) {
    try {
      var s = document.createElement("script");
      s.async = true; s.src = src;
      if (attrs) { Object.keys(attrs).forEach(function (k) { s.setAttribute(k, attrs[k]); }); }
      s.onerror = function () {};
      document.head.appendChild(s);
    } catch (e) {}
  }

  if (PROVIDER === "ga4" && GA4_ID) {
    load("https://www.googletagmanager.com/gtag/js?id=" + GA4_ID);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA4_ID, {
      anonymize_ip: true, allow_google_signals: false,
      allow_ad_personalization_signals: false
    });
  } else if (PROVIDER === "cloudflare" && CF_TOKEN) {
    load("https://static.cloudflareinsights.com/beacon.min.js",
         { "data-cf-beacon": '{"token":"' + CF_TOKEN + '"}' });
  }
})();

// Madde ekranı klavye kısayolları ve kapanırken kayıt (TASARIM.md K9). Çerçeve yok.
(function () {
  const form = document.getElementById('madde-form');
  if (!form) return;
  let etkin = 0, sonGirdi = 0, gonderimBasi = 0, kaydedilen = 0;
  const satirlar = () => Array.from(document.querySelectorAll('.kontrol'));
  const metinde = (el) => el && (el.tagName === 'TEXTAREA' || (el.tagName === 'INPUT' && el.type !== 'radio' && el.type !== 'checkbox'));

  function isaretle(n) {
    const s = satirlar();
    if (!s.length) return;
    etkin = Math.max(0, Math.min(n, s.length - 1));
    s.forEach((el, i) => el.classList.toggle('etkin', i === etkin));
    s[etkin].scrollIntoView({block: 'nearest'});
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && metinde(document.activeElement)) { document.activeElement.blur(); return; }
    if (metinde(document.activeElement) || e.metaKey || e.ctrlKey || e.altKey) return;
    const s = satirlar()[etkin];
    const tus = e.key.toLowerCase();
    const cevap = {e: 'E', h: 'H', b: 'B', n: 'NA'}[tus];
    if (tus === 'j' || e.key === 'ArrowDown') { isaretle(etkin + 1); e.preventDefault(); }
    else if (tus === 'k' || e.key === 'ArrowUp') { isaretle(etkin - 1); e.preventDefault(); }
    else if (cevap && s) {
      const r = s.querySelector(`input[type=radio][value="${cevap}"]`);
      if (r && !r.disabled) { r.click(); }
      e.preventDefault();
    }
    else if (tus === 's' && s) { const a = s.querySelector('button.atla'); if (a) a.click(); e.preventDefault(); }
    else if (tus === 'g') { document.getElementById('gorusme-notu').focus(); e.preventDefault(); }
    else if (e.key === '[') { document.getElementById('onceki').click(); }
    else if (e.key === ']') { document.getElementById('sonraki').click(); }
  });

  // Fareyle tıklanan satır etkin olsun
  document.addEventListener('click', (e) => {
    const k = e.target.closest('.kontrol');
    if (k) isaretle(satirlar().indexOf(k));
  });
  // OOB ile yeniden çizilen satırlar etkin işaretini kaybetmesin
  document.body.addEventListener('htmx:oobAfterSwap', () => isaretle(etkin));

  // Yazılıp henüz kaydedilmemiş değişiklik: sayfadan çıkarken anında gönder.
  // Bir kayıt, ancak gönderildiği andan önce yazılanları kaydetmiş sayılır.
  form.addEventListener('input', () => { sonGirdi = performance.now(); });
  form.addEventListener('htmx:beforeRequest', () => { gonderimBasi = performance.now(); });
  form.addEventListener('htmx:afterRequest', (e) => { if (e.detail.successful) kaydedilen = gonderimBasi; });
  window.addEventListener('pagehide', () => {
    if (sonGirdi <= kaydedilen) return;
    const fd = new FormData(form);
    fd.append('surum', document.getElementById('m-surum').value);
    fd.append('kapanis', '1');
    navigator.sendBeacon(form.getAttribute('hx-post'), fd);
  });

  isaretle(0);
})();

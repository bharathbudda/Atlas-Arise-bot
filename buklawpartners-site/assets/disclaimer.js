// ENTRY DISCLAIMER GATE - runs after DOM ready
(function() {
  function initDisclaimer() {
    var el = document.getElementById('entryDisclaimer');
    if (!el) return;
    var accepted = false;
    try { accepted = sessionStorage.getItem('bukDisclaimerAccepted') === '1'; } catch(e) {}
    if (accepted) {
      el.classList.add('ed-hidden');
      document.body.style.overflow = '';
    } else {
      el.classList.remove('ed-hidden');
      document.body.style.overflow = 'hidden';
    }
  }
  // Define the accept handler globally so the button onclick can reach it
  window.acceptDisclaimer = function() {
    try { sessionStorage.setItem('bukDisclaimerAccepted', '1'); } catch(e) {}
    var el = document.getElementById('entryDisclaimer');
    if (el) el.classList.add('ed-hidden');
    document.body.style.overflow = '';
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDisclaimer);
  } else {
    initDisclaimer();
  }
})();

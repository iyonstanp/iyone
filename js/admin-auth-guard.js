// IYONEX — redirects away from the admin dashboard unless this tab has
// already signed in via admin-login.html in the current session.
// See the security note in js/admin-auth.js — this is a demo-grade gate.
(function () {
  "use strict";
  var SESSION_KEY = "iyonex_admin_session";
  var authed = false;
  try {
    authed = window.sessionStorage && sessionStorage.getItem(SESSION_KEY) === "1";
  } catch (e) {
    authed = false;
  }
  if (!authed) {
    window.location.replace("admin-login.html");
  }
})();

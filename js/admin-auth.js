// IYONEX — admin access gate.
//
// SECURITY NOTE — read this before relying on it for anything real.
// This is a static site with no server, so there is nowhere safe to check a
// password: any credential compared here is sitting in a JS file that ships
// to every visitor's browser and can be read via "View Source" or dev tools.
// This gate only deters casual browsing (e.g. someone stumbling onto the
// admin URL) — it is NOT real authentication and NOT suitable for genuinely
// sensitive data. For real protection, move this behind an actual backend
// (Netlify Identity, Firebase Auth, Auth0, or a custom API with server-side
// sessions) before putting anything sensitive behind it.
//
// Change these before publishing the site:
var ADMIN_USERNAME = "admin";
var ADMIN_PASSWORD = "Iyonex#2026";

(function () {
  "use strict";
  var SESSION_KEY = "iyonex_admin_session";

  var form = document.getElementById("admin-login-form");
  var errorBox = document.getElementById("admin-error");

  if (form) {
    // Already signed in this tab? Skip straight to the dashboard.
    if (window.sessionStorage && sessionStorage.getItem(SESSION_KEY) === "1") {
      window.location.replace("admin.html");
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var user = document.getElementById("admin-user").value.trim();
      var pass = document.getElementById("admin-pass").value;

      if (user === ADMIN_USERNAME && pass === ADMIN_PASSWORD) {
        try {
          sessionStorage.setItem(SESSION_KEY, "1");
        } catch (err) {
          /* private browsing / storage disabled */
        }
        window.location.href = "admin.html";
      } else {
        errorBox.style.display = "block";
      }
    });
  }
})();

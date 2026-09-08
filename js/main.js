// IYONEX AUTOMATION — shared interaction layer
(function () {
  "use strict";

  /* mobile menu */
  var hamburger = document.querySelector(".hamburger");
  var mobileMenu = document.querySelector(".mobile-menu");

  if (hamburger && mobileMenu) {
    hamburger.addEventListener("click", function () {
      var open = mobileMenu.classList.toggle("open");
      hamburger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });

    mobileMenu.querySelectorAll(".m-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var sub = document.getElementById(btn.getAttribute("data-target"));
        if (sub) {
          var isOpen = sub.classList.toggle("open");
          btn.querySelector(".nav-caret") &&
            (btn.querySelector(".nav-caret").style.transform = isOpen
              ? "rotate(180deg)"
              : "rotate(0deg)");
        }
      });
    });

    mobileMenu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        mobileMenu.classList.remove("open");
        document.body.style.overflow = "";
      });
    });
  }

  /* scroll reveal */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* mark active nav link */
  var path = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a, .mobile-menu a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === path) {
      a.closest("li") && a.closest("li").classList.add("active");
      a.setAttribute("aria-current", "page");
    }
  });

  /* lightweight demo form handling — saves to this browser's storage so the
     admin panel has something to show; no live backend is wired up yet. */
  document.querySelectorAll("form[data-demo-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var storeKey = form.getAttribute("data-store-key");
      if (storeKey && window.localStorage) {
        try {
          var data = {};
          new FormData(form).forEach(function (value, key) {
            if (value instanceof File) {
              data[key] = value.name ? "[file: " + value.name + "]" : "";
            } else {
              data[key] = value;
            }
          });
          data._id = Date.now() + "-" + Math.random().toString(36).slice(2, 8);
          data._submittedAt = new Date().toISOString();

          var storageId = "iyonex_submissions_" + storeKey;
          var existing = [];
          try {
            existing = JSON.parse(window.localStorage.getItem(storageId) || "[]");
          } catch (err) {
            existing = [];
          }
          existing.unshift(data);
          window.localStorage.setItem(storageId, JSON.stringify(existing));
        } catch (err) {
          /* localStorage unavailable (private browsing, quota, etc.) — fail silently */
        }
      }

      var msg = form.querySelector(".form-status");
      if (msg) {
        msg.textContent =
          "Thanks — this form isn't connected to a live inbox yet, so please also email or call us directly. Your message has been saved on this device for review in the admin panel.";
        msg.style.display = "block";
      }
      form.reset();
    });
  });
})();

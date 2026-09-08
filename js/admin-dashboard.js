// IYONEX — admin dashboard: reads submissions saved by js/main.js into
// this browser's localStorage and renders them. See admin.html's banner
// and js/admin-auth.js for the important limitations of this demo setup.
(function () {
  "use strict";
  var SESSION_KEY = "iyonex_admin_session";
  var KEYS = ["contact", "internship", "workshop"];

  function storageKey(name) {
    return "iyonex_submissions_" + name;
  }

  function load(name) {
    try {
      return JSON.parse(window.localStorage.getItem(storageKey(name)) || "[]");
    } catch (e) {
      return [];
    }
  }

  function save(name, entries) {
    try {
      window.localStorage.setItem(storageKey(name), JSON.stringify(entries));
    } catch (e) {
      /* ignore */
    }
  }

  function fieldLabel(key) {
    return key
      .replace(/^_/, "")
      .replace(/[_-]/g, " ")
      .replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  }

  function formatDate(iso) {
    try {
      var d = new Date(iso);
      return d.toLocaleString();
    } catch (e) {
      return iso || "";
    }
  }

  function render(name) {
    var entries = load(name);
    var list = document.getElementById("list-" + name);
    var count = document.getElementById("count-" + name);
    if (!list || !count) return;

    count.textContent = entries.length + (entries.length === 1 ? " submission" : " submissions");
    list.innerHTML = "";

    if (!entries.length) {
      var empty = document.createElement("div");
      empty.className = "admin-empty";
      empty.textContent = "No submissions yet in this browser.";
      list.appendChild(empty);
      return;
    }

    entries.forEach(function (entry) {
      var card = document.createElement("div");
      card.className = "entry-card";

      var head = document.createElement("div");
      head.className = "entry-head";

      var date = document.createElement("span");
      date.className = "entry-date";
      date.textContent = formatDate(entry._submittedAt);
      head.appendChild(date);

      var del = document.createElement("button");
      del.className = "entry-delete";
      del.textContent = "Delete";
      del.addEventListener("click", function () {
        var remaining = load(name).filter(function (e) { return e._id !== entry._id; });
        save(name, remaining);
        render(name);
      });
      head.appendChild(del);
      card.appendChild(head);

      var grid = document.createElement("dl");
      grid.className = "entry-grid";
      Object.keys(entry).forEach(function (key) {
        if (key === "_id" || key === "_submittedAt") return;
        var value = entry[key];
        if (!value) return;
        var field = document.createElement("div");
        field.className = "entry-field";
        var dt = document.createElement("dt");
        dt.textContent = fieldLabel(key);
        var dd = document.createElement("dd");
        dd.textContent = value;
        field.appendChild(dt);
        field.appendChild(dd);
        grid.appendChild(field);
      });
      card.appendChild(grid);

      list.appendChild(card);
    });
  }

  function toCSV(entries) {
    if (!entries.length) return "";
    var cols = [];
    entries.forEach(function (e) {
      Object.keys(e).forEach(function (k) {
        if (cols.indexOf(k) === -1) cols.push(k);
      });
    });
    var esc = function (v) {
      v = v === undefined || v === null ? "" : String(v);
      if (/[",\n]/.test(v)) v = '"' + v.replace(/"/g, '""') + '"';
      return v;
    };
    var lines = [cols.map(esc).join(",")];
    entries.forEach(function (e) {
      lines.push(cols.map(function (c) { return esc(e[c]); }).join(","));
    });
    return lines.join("\n");
  }

  function downloadCSV(name) {
    var entries = load(name);
    var csv = toCSV(entries);
    if (!csv) {
      alert("Nothing to export yet.");
      return;
    }
    var blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = "iyonex-" + name + "-submissions.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  /* tabs */
  document.querySelectorAll(".admin-tab").forEach(function (tab) {
    tab.addEventListener("click", function () {
      var target = tab.getAttribute("data-tab");
      document.querySelectorAll(".admin-tab").forEach(function (t) { t.classList.remove("active"); });
      document.querySelectorAll(".admin-panel").forEach(function (p) { p.classList.remove("active"); });
      tab.classList.add("active");
      document.getElementById("panel-" + target).classList.add("active");
    });
  });

  /* export / clear buttons */
  document.querySelectorAll("[data-export]").forEach(function (btn) {
    btn.addEventListener("click", function () { downloadCSV(btn.getAttribute("data-export")); });
  });
  document.querySelectorAll("[data-clear]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var name = btn.getAttribute("data-clear");
      if (confirm("Delete all " + name + " submissions saved in this browser? This can't be undone.")) {
        save(name, []);
        render(name);
      }
    });
  });

  /* logout */
  var logoutBtn = document.getElementById("admin-logout");
  if (logoutBtn) {
    logoutBtn.addEventListener("click", function () {
      try { sessionStorage.removeItem(SESSION_KEY); } catch (e) {}
      window.location.href = "admin-login.html";
    });
  }

  KEYS.forEach(render);
})();

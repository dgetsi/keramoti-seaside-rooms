/* Katerina apartments — small, dependency-free behaviour layer.
   Everything works without JS (links, tel:, images); JS adds language memory,
   carousels, lightbox and sharing. */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ── language ─────────────────────────────── */
  function store(k, v) { try { v === undefined ? (v = localStorage.getItem(k)) : localStorage.setItem(k, v); } catch (e) {} return v; }
  function setLang(l, save) {
    if (l !== "el" && l !== "en") return;
    root.setAttribute("data-lang", l);
    root.lang = l;
    document.querySelectorAll("[data-alt-" + l + "]").forEach(function (el) { el.alt = el.getAttribute("data-alt-" + l); });
    document.querySelectorAll("[data-aria-" + l + "]").forEach(function (el) { el.setAttribute("aria-label", el.getAttribute("data-aria-" + l)); });
    var t = root.getAttribute("data-title-" + l); if (t) document.title = t;
    document.querySelectorAll(".lang button").forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.setLang === l)); });
    if (save) {
      store("lang", l);
      var u = new URL(location.href); u.searchParams.set("lang", l);
      history.replaceState(null, "", u);
    }
  }
  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.setLang, true); });
  });
  setLang(root.getAttribute("data-lang") || "el", false);

  /* ── header shadow ─────────────────────────── */
  var hdr = document.querySelector(".hdr");
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  /* ── carousels ─────────────────────────────── */
  document.querySelectorAll("[data-car]").forEach(function (car) {
    var track = car.querySelector(".car-track");
    var slides = track.children.length;
    var prev = car.querySelector(".car-prev"), next = car.querySelector(".car-next"), count = car.querySelector(".car-count");
    function idx() { return Math.round(track.scrollLeft / track.clientWidth); }
    function update() {
      var i = idx();
      if (count) count.textContent = (i + 1) + " / " + slides;
      if (prev) prev.disabled = i <= 0;
      if (next) next.disabled = i >= slides - 1;
    }
    function go(d) { track.scrollTo({ left: (idx() + d) * track.clientWidth, behavior: reduce ? "auto" : "smooth" }); }
    if (prev) prev.addEventListener("click", function () { go(-1); });
    if (next) next.addEventListener("click", function () { go(1); });
    track.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); go(1); }
      if (e.key === "ArrowLeft") { e.preventDefault(); go(-1); }
    });
    var raf; track.addEventListener("scroll", function () { cancelAnimationFrame(raf); raf = requestAnimationFrame(update); }, { passive: true });
    window.addEventListener("resize", update);
    update();
  });

  /* ── gallery "show all" ────────────────────── */
  document.querySelectorAll("[data-show-all]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var g = document.getElementById(btn.getAttribute("aria-controls"));
      g.classList.add("show-all");
      btn.setAttribute("aria-expanded", "true");
      btn.hidden = true;
      var first = g.querySelector(".is-hidden a, a.is-hidden"); if (first) first.focus();
    });
  });

  /* ── lightbox ──────────────────────────────── */
  var lb = document.getElementById("lb");
  if (lb && typeof lb.showModal === "function") {
    var img = lb.querySelector(".lb-stage img"), cap = lb.querySelector(".lb-cap"), cnt = lb.querySelector(".lb-count");
    var items = [], cur = 0, opener = null;
    function lang() { return root.getAttribute("data-lang"); }
    function show(i) {
      cur = (i + items.length) % items.length;
      var a = items[cur], t = a.querySelector("img");
      var alt = t ? (t.getAttribute("data-alt-" + lang()) || t.alt) : "";
      img.src = a.href; img.alt = alt; cap.textContent = alt;
      cnt.textContent = (cur + 1) + " / " + items.length;
      // preload neighbours
      [cur + 1, cur - 1].forEach(function (j) { var n = items[(j + items.length) % items.length]; if (n) { var p = new Image(); p.src = n.href; } });
    }
    document.addEventListener("click", function (e) {
      var a = e.target.closest("a[data-lb]");
      if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault();
      var group = a.getAttribute("data-lb");
      var seen = {};
      items = Array.prototype.filter.call(document.querySelectorAll('a[data-lb="' + group + '"]'), function (x) {
        if (seen[x.href]) return false; seen[x.href] = 1; return true;
      });
      opener = a;
      lb.showModal();
      show(items.findIndex(function (x) { return x.href === a.href; }));
      lb.querySelector(".lb-close").focus();
    });
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(cur - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(cur + 1); });
    lb.querySelector(".lb-close").addEventListener("click", function () { lb.close(); });
    lb.addEventListener("close", function () { img.removeAttribute("src"); if (opener) opener.focus(); });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); show(cur + 1); }
      else if (e.key === "ArrowLeft") { e.preventDefault(); show(cur - 1); }
      else if (e.key === "Home") { e.preventDefault(); show(0); }
      else if (e.key === "End") { e.preventDefault(); show(items.length - 1); }
    });
    // swipe
    var stage = lb.querySelector(".lb-stage"), x0 = null, y0 = 0;
    stage.addEventListener("pointerdown", function (e) { x0 = e.clientX; y0 = e.clientY; });
    stage.addEventListener("pointerup", function (e) {
      if (x0 === null) return;
      var dx = e.clientX - x0, dy = e.clientY - y0; x0 = null;
      if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) show(cur + (dx < 0 ? 1 : -1));
    });
    stage.addEventListener("pointercancel", function () { x0 = null; });
  }

  /* ── sharing ───────────────────────────────── */
  var share = document.querySelector("[data-share]");
  if (share) {
    var url = (document.querySelector('link[rel="canonical"]') || {}).href || location.href.split("?")[0];
    var title = function () { return document.title; };
    var toast = share.querySelector(".toast");
    function say(el, en) { toast.textContent = root.getAttribute("data-lang") === "en" ? en : el; setTimeout(function () { toast.textContent = ""; }, 3500); }
    share.querySelector("[data-fb]").href = "https://www.facebook.com/sharer/sharer.php?u=" + encodeURIComponent(url);
    share.querySelector("[data-wa]").addEventListener("click", function (e) {
      this.href = "https://wa.me/?text=" + encodeURIComponent(title() + "\n" + url);
    });
    share.querySelector("[data-viber]").addEventListener("click", function () {
      this.href = "viber://forward?text=" + encodeURIComponent(title() + " " + url);
    });
    share.querySelector("[data-copy]").addEventListener("click", function () {
      var done = function () { say("Ο σύνδεσμος αντιγράφηκε", "Link copied"); };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(url).then(done, fallback);
      else fallback();
      function fallback() {
        var t = document.createElement("textarea"); t.value = url; t.setAttribute("readonly", ""); t.style.position = "fixed"; t.style.opacity = "0";
        document.body.appendChild(t); t.select();
        try { document.execCommand("copy"); done(); } catch (e) { say("Αντιγράψτε: " + url, "Copy: " + url); }
        t.remove();
      }
    });
    if (navigator.share) {
      share.classList.add("can-share");
      share.querySelector("[data-native]").addEventListener("click", function () {
        navigator.share({ title: title(), url: url }).catch(function () {});
      });
    }
  }

  /* ── gentle reveal ─────────────────────────── */
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
  }
})();

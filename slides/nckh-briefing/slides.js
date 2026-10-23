(function () {
  const slides = Array.from(document.querySelectorAll(".slide"));
  let i = 0;

  function show(n) {
    if (!document.body.classList.contains("present")) return;
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, k) => s.classList.toggle("active", k === i));
    window.scrollTo(0, 0);
  }

  function enterPresent() {
    document.body.classList.add("present");
    show(i);
  }

  function exitPresent() {
    document.body.classList.remove("present");
    slides.forEach((s) => s.classList.remove("active"));
  }

  document.getElementById("prev")?.addEventListener("click", () => {
    if (!document.body.classList.contains("present")) enterPresent();
    show(i - 1);
  });
  document.getElementById("next")?.addEventListener("click", () => {
    if (!document.body.classList.contains("present")) enterPresent();
    show(i + 1);
  });

  window.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight" || e.key === "PageDown" || e.key === " ") {
      e.preventDefault();
      if (!document.body.classList.contains("present")) enterPresent();
      show(i + 1);
    } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
      e.preventDefault();
      if (!document.body.classList.contains("present")) enterPresent();
      show(i - 1);
    } else if (e.key === "f" || e.key === "F") {
      e.preventDefault();
      if (document.body.classList.contains("present")) exitPresent();
      else enterPresent();
    } else if (e.key === "Escape") {
      exitPresent();
    }
  });
})();

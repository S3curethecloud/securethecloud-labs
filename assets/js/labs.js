document.addEventListener("DOMContentLoaded", () => {
  let allLabs = [];

  const container = document.getElementById("labs-container");
  const filterButtons = document.querySelectorAll(".filter-btn");

  fetch("/manifest.json")
    .then(res => res.json())
    .then(data => {
      allLabs = data.labs;
      renderLabs("all");
    })
    .catch(err => {
      console.error("Failed to load labs manifest:", err);
    });

  function renderLabs(filter) {
    container.innerHTML = "";

    const filtered =
      filter === "all"
        ? allLabs
        : allLabs.filter(lab => lab.cloud === filter);

    filtered.forEach(lab => {
      const card = document.createElement("div");
      card.className = "lab-card";

      card.innerHTML = `
        <h3>${lab.title}</h3>
        <p class="lab-meta">
          ${lab.cloud.toUpperCase()} · ${lab.domain} · ${lab.level}
        </p>
        <p>${lab.summary}</p>
        <a href="${lab.path}" class="lab-link">Open Lab →</a>
      `;

      container.appendChild(card);
    });
  }

  filterButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      filterButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      renderLabs(btn.dataset.cloud);
    });
  });
});

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

      const maturity = lab.maturity || "starter";

      card.innerHTML = `
        <span class="badge badge-${maturity}">
          ${maturity.toUpperCase()}
        </span>

        <h3>${lab.title}</h3>

        <p class="lab-meta">
          ${lab.cloud.toUpperCase()} · ${lab.domain} · ${lab.level}
        </p>

        <p>${lab.summary}</p>

        <a href="${lab.path}" class="lab-link">
          Open Lab →
        </a>
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

document.querySelectorAll(".explore-link").forEach(link => {
  link.addEventListener("click", e => {
    e.preventDefault();
    const filter = link.dataset.filter;

    // Activate corresponding filter button
    document.querySelectorAll(".filter-btn").forEach(btn => {
      btn.classList.toggle(
        "active",
        btn.dataset.cloud === filter
      );
    });

    // Trigger filtering
    const event = new Event("click");
    document
      .querySelector(`.filter-btn[data-cloud="${filter}"]`)
      ?.dispatchEvent(event);

    // Smooth scroll
    document
      .getElementById("available-labs")
      .scrollIntoView({ behavior: "smooth" });
  });
});

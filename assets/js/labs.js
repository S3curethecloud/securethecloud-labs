document.addEventListener("DOMContentLoaded", () => {
  let allLabs = [];

  const container = document.getElementById("labs-container");
  const filterButtons = document.querySelectorAll(".filter-btn");
  const exploreLinks = document.querySelectorAll(".explore-link");

  if (!container) {
    console.error("Labs container not found.");
    return;
  }

  fetch(`/manifest.json?ts=${Date.now()}`, { cache: "no-store" })
    .then(res => {
      if (!res.ok) {
        throw new Error(`manifest load failed: ${res.status}`);
      }
      return res.json();
    })
    .then(data => {
      if (!data || !Array.isArray(data.labs)) {
        throw new Error("manifest.json does not contain a labs array");
      }

      allLabs = data.labs;
      renderLabs("all");
    })
    .catch(err => {
      console.error("Failed to load labs manifest:", err);
      container.innerHTML = `
        <div class="lab-card">
          <span class="badge badge-starter">ERROR</span>
          <h3>Labs unavailable</h3>
          <p>Unable to load manifest.json. Please refresh or check the deployment.</p>
        </div>
      `;
    });

  function renderLabs(filter) {
    container.innerHTML = "";

    const filtered =
      filter === "all"
        ? allLabs
        : allLabs.filter(lab => lab.cloud === filter);

    if (!filtered.length) {
      container.innerHTML = `
        <div class="lab-card">
          <span class="badge badge-starter">EMPTY</span>
          <h3>No labs found</h3>
          <p>No labs are currently registered for this filter.</p>
        </div>
      `;
      return;
    }

    filtered.forEach(lab => {
      const card = document.createElement("div");
      card.className = "lab-card";
      card.dataset.cloud = lab.cloud || "unknown";

      const maturity = lab.maturity || "starter";
      const cloud = lab.cloud || "unknown";
      const domain = lab.domain || "unknown";
      const level = lab.level || lab.difficulty || "unknown";
      const summary = lab.summary || "No summary provided.";
      const path = lab.path || "#";

      card.innerHTML = `
        <span class="badge badge-${maturity}">
          ${maturity.toUpperCase()}
        </span>

        <h3>${lab.title}</h3>

        <p class="lab-meta">
          ${cloud.toUpperCase()} · ${domain} · ${level}
        </p>

        <p>${summary}</p>

        <a href="${path}" class="lab-link">
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

  exploreLinks.forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();

      const filter = link.dataset.filter;
      const targetButton = document.querySelector(`.filter-btn[data-cloud="${filter}"]`);

      if (targetButton) {
        targetButton.click();
      }

      document
        .getElementById("available-labs")
        ?.scrollIntoView({ behavior: "smooth" });
    });
  });
});

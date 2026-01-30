fetch("manifest.json")
  .then(res => res.json())
  .then(data => {
    const grid = document.getElementById("labsGrid");

    data.labs.forEach(lab => {
      const card = document.createElement("div");
      card.className = "lab-card";

      card.innerHTML = `
        <h3>${lab.title}</h3>
        <p>${lab.description}</p>
        <a href="${lab.path}">Start Lab →</a>
      `;

      grid.appendChild(card);
    });
  });

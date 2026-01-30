fetch('/manifest.json')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('labs-container');
    data.labs.forEach(lab => {
      const card = document.createElement('div');
      card.className = 'lab-card';

      card.innerHTML = `
        <h3>${lab.title}</h3>
        <p class="lab-meta">${lab.cloud} · ${lab.domain} · ${lab.level}</p>
        <p>${lab.description}</p>
        <a href="${lab.path}" class="lab-link">Open Lab →</a>
      `;

      container.appendChild(card);
    });
  })
  .catch(err => {
    console.error('Failed to load lab manifest', err);
  });


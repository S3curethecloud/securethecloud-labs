async function loadLabs() {
  try {
    const response = await fetch('/manifest.json');
    const data = await response.json();

    const container = document.getElementById('labs-list');
    if (!container) return;

    data.labs.forEach(lab => {
      const card = document.createElement('div');
      card.className = 'section';

      card.innerHTML = `
        <h3>${lab.title}</h3>
        <p><strong>${lab.cloud}</strong> · ${lab.domain} · ${lab.level}</p>
        <p>${lab.description}</p>
        <a href="${lab.path}">Open Lab →</a>
      `;

      container.appendChild(card);
    });
  } catch (err) {
    console.error('Failed to load labs manifest:', err);
  }
}

document.addEventListener('DOMContentLoaded', loadLabs);

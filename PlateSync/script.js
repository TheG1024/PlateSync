// Add JavaScript functionality here
console.log("Script loaded");

// Populate the table with data from the inventory
fetch('/api/inventory/')
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('tbody');
    data.forEach(item => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${item.name}</td>
        <td>${item.quantity}</td>
        <td>${item.supplier}</td>
      `;
      tableBody.appendChild(row);
    });
  });

// Handle form submission
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const item = document.querySelector('#item').value;
  const quantity = document.querySelector('#quantity').value;
  const supplier = document.querySelector('#supplier').value;
  fetch('/api/inventory/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ item, quantity, supplier })
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
});

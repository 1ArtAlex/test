document.addEventListener('DOMContentLoaded', function () {
    const modelList = document.getElementById('modelList');
    const carList = document.getElementById('carList');
    const models = ['ARRIZO8', 'TIGGO4 PRO', 'TIGGO7 PRO', 'TIGGO7 PRO MAX', 'TIGGO8', 'TIGGO8 PRO', 'TIGGO8 PRO MAX NEW'];

    // Display models
    models.forEach(model => {
        const listItem = document.createElement('li');
        listItem.textContent = model;
        listItem.addEventListener('click', () => showCars(model));
        modelList.appendChild(listItem);
    });

    // Display cars for a selected model
    function showCars(model) {
        modelList.style.display = 'none';
        carList.style.display = 'block';
        carList.innerHTML = `<h3>Cars available for ${model}</h3>`;

        // Simulate fetching cars data from the server
        const carsData = getCarsData(model);

        carsData.forEach(car => {
            const listItem = document.createElement('li');
            listItem.textContent = `${car.name} - ${car.price}`;
            carList.appendChild(listItem);
        });
    }

    // Simulated data (replace with actual data from your server)
    function getCarsData(model) {
        // You can fetch this data from the server based on the selected model
        // This is just a simulated example
        const carDataMap = {
            'ARRIZO8': [{ name: 'Car1', price: '$20,000' }, { name: 'Car2', price: '$25,000' }],
            'TIGGO4 PRO': [{ name: 'Car3', price: '$22,000' }, { name: 'Car4', price: '$28,000' }],
            // Add data for other models
        };

        return carDataMap[model] || [];
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("datepicker");
    const resultado = document.getElementById("resultado");

    // Inicializar Flatpickr con rango de fechas
    const calendar = flatpickr("#datepicker", {
        mode: "range", // Permite seleccionar un rango
        dateFormat: "d/m/Y",
        minDate: "today",
        locale: "es",
        showMonths: 2,
        
    });

    // Mostrar el input al presionar el botón
    document.getElementById("openCalendar").addEventListener("click", function() {
        input.style.display = "block";
        input.focus();
    });
});

var swiper = new Swiper(".mySwiper", {
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});
function procesarPago() {
    let tarjeta = document.getElementById('tarjeta').value;
    let nombre = document.getElementById('nombre').value;
    let cvv = document.getElementById('cvv').value;
    let fecha = document.getElementById('fecha').value;
    let mensaje = document.getElementById('mensaje');

    if (tarjeta.length < 16 || nombre === "" || cvv.length < 3 || fecha === "") {
        mensaje.style.color = "red";
        mensaje.innerText = "Por favor, complete todos los campos correctamente.";
        return;
    }

    mensaje.style.color = "green";
    mensaje.innerText = "Procesando pago...";

    setTimeout(() => {
        mensaje.innerText = "¡Pago realizado con éxito!";
    }, 2000);
}

// Lógica para colocar el mapa con la respectiva API
document.addEventListener("DOMContentLoaded", function () {
    var ubicacion = document.getElementById("ubicacion-texto").innerText; // Obtiene el nombre de la ciudad

    // API de OpenStreetMap para obtener coordenadas a partir de un nombre de ciudad
    var url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(ubicacion)}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                var lat = data[0].lat;
                var lon = data[0].lon;

                // Inicializa el mapa con las coordenadas obtenidas
                var map = L.map('mapa').setView([lat, lon], 12);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '&copy; OpenStreetMap contributors'
                }).addTo(map);

                L.marker([lat, lon]).addTo(map)
                    .bindPopup(`Ubicación: ${ubicacion}`)
                    .openPopup();
            } else {
                console.error("No se encontraron coordenadas para la ubicación proporcionada.");
            }
        })
        .catch(error => console.error("Error al obtener coordenadas:", error));
});

// Lógica para la búsqueda de los alojamientos en la página de inicio
document.getElementById("filter-form").addEventListener("submit", function(event) {
    let city = document.getElementById("city").value;
    let dateRange = document.getElementById("datepicker").value; // "21/02/2025 to 28/02/2025"

    if (!dateRange.includes(" to ")) {
        alert("Selecciona un rango de fechas válido.");
        event.preventDefault();
        return;
    }

    let [initialDate, endDate] = dateRange.split(" to ");

    // Función para convertir "DD/MM/YYYY" a "YYYY-MM-DD"
    function formatDate(dateStr) {
        let [day, month, year] = dateStr.split("/");
        return `${year}-${month}-${day}`;
    }

    document.getElementById("form-city").value = city;
    document.getElementById("form-initial-date").value = formatDate(initialDate);
    document.getElementById("form-end-date").value = formatDate(endDate);
});

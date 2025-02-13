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
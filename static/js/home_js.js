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
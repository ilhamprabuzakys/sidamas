document.addEventListener("DOMContentLoaded", function () {
    // Mengambil elemen input date dari container dengan class 'date-plus-two-day'
    var dateContainer = document.querySelector(".date-plus-two-day");
    var dateInputs = dateContainer.querySelectorAll('input[type="date"]');

    if (dateInputs.length === 2) {
        // Mendapatkan tanggal hari ini
        var today = new Date();
        var todayFormatted = today.toISOString().split("T")[0];

        // Mengisi nilai date pertama dengan today
        dateInputs[0].value = todayFormatted;

        // Mengisi nilai date kedua dengan today + 2 days
        var twoDaysLater = new Date(today);
        twoDaysLater.setDate(today.getDate() + 2);
        var twoDaysLaterFormatted = twoDaysLater.toISOString().split("T")[0];
        dateInputs[1].value = twoDaysLaterFormatted;
    }

    const currentYear = new Date().getFullYear();

    // Headline tahun otomatis
    if (document.querySelector("#__data #headline .text-center")) {
        document.querySelector("#__data #headline .text-center").innerHTML +=
            " TAHUN " + currentYear;
    }

    // Dapatkan semua elemen input dengan tipe "date"
    var inputDates = document.querySelectorAll("input[type='date']");

    // Iterasi melalui setiap elemen input date
    inputDates.forEach(function (inputDate) {
        // Set atribut min dan max untuk setiap elemen
        inputDate.setAttribute("min", currentYear + "-01-01");
        inputDate.setAttribute("max", currentYear + "-12-31");
    });
});

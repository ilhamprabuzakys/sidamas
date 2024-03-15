document.addEventListener("DOMContentLoaded", function () {
    /***========================================================
     * KEGIATAN INPUT DATE RANGE DEFAULT FORMULA (NOW to NOW+2)
    ========================================================***/
    // Mengambil elemen input date dari container dengan class 'date-plus-two-day'
    var dateContainer = document.querySelector(".date-plus-two-day");
    var dateInputs = dateContainer && dateContainer.querySelectorAll('input[type="date"]');

    if (dateInputs && dateInputs.length === 2) {
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

    /***============================
    * KEGIATAN HEADLINE CURRENT YEAR
    ============================***/
    if (document.querySelector("#__data #headline .text-center")) {
        document.querySelector("#__data #headline .text-center").innerHTML +=
            " TAHUN " + currentYear;
    }

    /***=======================================================
    * KEGIATAN HEADLINE LIMIT INPUT DATE ONLY FOR CURRENT YEAR
    =======================================================***/
    // Dapatkan semua elemen input dengan tipe "date"
    var inputDates = document.querySelectorAll("input[type='date']");

    // Iterasi melalui setiap elemen input date
    inputDates && inputDates.forEach(function (inputDate) {
        // Set atribut min dan max untuk setiap elemen
        inputDate.setAttribute("min", currentYear + "-01-01");
        inputDate.setAttribute("max", currentYear + "-12-31");
    });
});

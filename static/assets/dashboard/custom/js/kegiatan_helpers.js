document.addEventListener("DOMContentLoaded", function () {
    /***========================================================
     * KEGIATAN INPUT DATE RANGE DEFAULT FORMULA (NOW to NOW+2)
    ========================================================***/
    // Mengambil elemen input date dari container dengan class 'date-plus-two-day'
    const dateContainer = document.querySelector(".date-plus-two-day");
    let dateInputs = dateContainer && dateContainer.querySelectorAll('input[type="date"]');

    if (dateInputs && dateInputs.length === 2) {
        // Mendapatkan tanggal hari ini
        let today = new Date();
        let todayFormatted = today.toISOString().split("T")[0];

        // Mengisi nilai date pertama dengan today
        dateInputs[0].value = todayFormatted;

        // Mengisi nilai date kedua dengan today + 2 days
        let twoDaysLater = new Date(today);
        twoDaysLater.setDate(today.getDate() + 2);
        let twoDaysLaterFormatted = twoDaysLater.toISOString().split("T")[0];
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
    const inputDates = document.querySelectorAll("input[type='date']");

    // Iterasi melalui setiap elemen input date
    inputDates && inputDates.forEach(function (inputDate) {
        // Set atribut min dan max untuk setiap elemen
        inputDate.setAttribute("min", currentYear + "-01-01");
        inputDate.setAttribute("max", currentYear + "-12-31");
    });

    
    
});

/***=======================================================
* KEGIATAN MAX MIN INPUT DATE
=======================================================***/
// Tambahkan event listener untuk saat modal ditampilkan
document.addEventListener('show.bs.modal', function(event) {
    // Temukan modal yang ditampilkan
    const modal = event.target;

    // Temukan elemen parent dengan class range_date di dalam modal
    const rangeDateParent = modal.querySelector('.range_date');

    if (!rangeDateParent) return;
    // Ambil semua input date di dalam parent
    const dateInputs = rangeDateParent.querySelectorAll('input[type="date"]');

    // Pastikan terdapat minimal dua input date
    if (!dateInputs.length >= 2) return

    // Ambil input pertama (start_date)
    const startDateInput = dateInputs[0];

    // Ambil input kedua (end_date)
    const endDateInput = dateInputs[1];

    // Tambahkan event listener untuk input end_date
    endDateInput.addEventListener('input', function() {
        // Ambil value dari end_date input
        const endDateValue = endDateInput.value;

        // Jika end_date sudah diset
        if (endDateValue) {
            // Batasi start_date agar tidak melebihi end_date
            startDateInput.max = endDateValue;
        }
    });

    // Tambahkan event listener untuk input start_date
    startDateInput.addEventListener('input', function() {
        // Ambil value dari start_date input
        const startDateValue = startDateInput.value;

        // Jika start_date sudah diset
        if (startDateValue) {
            // Batasi end_date agar tidak kurang dari start_date
            endDateInput.min = startDateValue;
        }
    });
});


function getTanggalKegiatan(tanggal_awal, tanggal_akhir) {
    const start = moment(tanggal_awal);
    const startDate = start.format('D');
    const startMonth = start.format('MMMM');
    const startYear = start.format('YYYY');

    if (tanggal_akhir) {
        const end = moment(tanggal_akhir);
        const endDate = end.format('D');
        const endMonth = end.format('MMMM');
        const endYear = end.format('YYYY');

        if (startMonth === endMonth && startYear === endYear) {
            return `${startDate} - ${endDate} ${startMonth} ${startYear}`;
        } else if (startYear !== endYear) {
            return `${start.format('D MMMM YYYY')} - ${end.format('D MMMM YYYY')}`;
        } else {
            return `${start.format('D MMMM')} - ${end.format('D MMMM YYYY')}`;
        }
    } else {
        return start.format('D MMMM YYYY');
    }
}


// function formatDate(dateString) {
//     const [year, month, day] = dateString.split('-');
//     return new Date(year, month - 1, day);
// }

// function calculateDays() {
//     const startDate = formatDate(this.startDate);
//     const endDate = formatDate(this.endDate);

//     // Clear end date if start date is cleared
//     if (!this.startDate) {
//         this.endDate = '';
//         return;
//     }

//     // Prevent choosing end date less than current date
//      const currentDate = new Date();
//      if (endDate < currentDate) {
//          alert('Tanggal akhir tidak boleh kurang dari tanggal saat ini!');
//          this.endDate = '';
//          return;
//      }

//     const diffTime = Math.abs(endDate - startDate);
//     const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

//     const calculateDays = isNaN(diffDays) ? 1 : diffDays + 1;
//     const jumlahHari = calculateDays < 0 ? 0 : calculateDays;
//     this.jumlahHari = `${jumlahHari} hari`;
// }



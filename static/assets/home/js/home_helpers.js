/*== AJAX REQUEST HELPERS ==*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Mengecek apakah cookie memiliki nama yang sesuai
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

function getXCSRFToken() {
    return document.querySelector(
        'meta[name="csrf-token"]'
    ).content;
}

function getCSRFToken() {
    return getCookie('csrftoken');
}

function getHeaders(type) {
    return {
        "X-CSRFToken": getCSRFToken(),
        'Content-Type': type ?? 'application/json',
    };
}

/*== DATATABLE HELPERS ==*/
function dt_lang_config() {
    const language = {
        sEmptyTable: 'Tidak ada data yang tersedia pada tabel ini',
        sProcessing: 'Sedang memproses...',
        sLengthMenu: 'Tampilkan _MENU_ entri',
        sZeroRecords: 'Tidak ditemukan data yang sesuai',
        sInfo: 'Menampilkan _START_ sampai _END_ dari _TOTAL_ entri',
        sInfoEmpty: 'Menampilkan 0 sampai 0 dari 0 entri',
        sInfoFiltered: '(disaring dari _MAX_ entri keseluruhan)',
        sInfoPostFix: '',
        sSearch: 'Pencarian:',
        sUrl: '',
        oPaginate: {
          sFirst: '<i class="fas fa-angle-double-left"></i>',
          sPrevious: '<i class="fas fa-angle-left"></i>',
          sNext: '<i class="fas fa-angle-right"></i>',
          sLast: '<i class="fas fa-angle-double-right"></i>'
        }
      }
    ;
    return language;
}
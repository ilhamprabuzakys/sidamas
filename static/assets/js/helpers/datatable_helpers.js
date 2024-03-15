// Datatable helpers
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
        // oPaginate: {
        //     sFirst: 'Awal',
        //     sPrevious: 'Sebelumnya',
        //     sNext: 'Berikutnya',
        //     sLast: 'Akhir'
        // },
        oPaginate: {
            sFirst: '<i class="fas fa-angle-double-left"></i>',
            sPrevious: '<i class="fas fa-angle-left"></i>',
            sNext: '<i class="fas fa-angle-right"></i>',
            sLast: '<i class="fas fa-angle-double-right"></i>'
        },
    }
        ;
    return language;
}

function reloadTable(table) {
    table.ajax.reload();
}

function reloadAllDataTables() {
    var tables = $.fn.dataTable.fnTables(true);

    $(tables).each(function() {
        var dataTable = $(this).dataTable().api();
        dataTable.ajax.reload(null, false);
    });
}

function dt_row_pagination() {
    return {
        targets: 0,
        render: function (data, type, row, meta) {
            var page = table.page.info().page;
            var length = table.page.info().length;
            var index = (page * length) + meta.row + 1;
            return index;
        }
    }
}

function convertToTitleCaseAndReplaceSpace(input) {
    if (!input) return;
    return input.split(' ').map(word => {
        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    }).join('+');
}


$(document).on('processing.dt', function (e, settings, processing) {
    if (!processing) {
        unblock( $(settings.nTable).parent() );
    } else {
        blockWithSpinner($(settings.nTable).parent());
    }
});

function createDT(el, url, columns, options) {
    // A shortcut to create DataTable

    // Set default options
    options = {
        enableNumbering: true,
        dataSrc: 'data',
        searching: true,
        serverSide: true,
        pageLength: 10,
        responsive: true,
        ordering: true,
        columnDefs: null,
        ...options // Menggabungkan options yang diberikan dengan default
    };
    
    return $(el).DataTable({
        language: dt_lang_config(),
        serverSide: options.serverSide,
        searching: options.searching,
        responsive: options.responsive,
        pageLength: options.pageLength,
        ajax: {
            url: url,
            dataSrc: options.dataSrc
        },
        ordering: options.ordering,
        columns: columns,
        initComplete: function (settings, json) {
            console.log('Hasil fetch data : ', json);
        },
        columnDefs: [options.enableNumbering ? dt_row_pagination() : null, ...(options.columnDefs || [])] // Gabungkan objek default dengan objek yang diberikan
    });
}

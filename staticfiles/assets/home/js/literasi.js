// Inisialisasi Datatable
$(document).ready(function () {
   $('#table_literasi').DataTable({
     language: {
       sEmptyTable: 'Tidak ada data yang tersedia pada tabel ini',
       sProcessing: 'Sedang memproses...',
       sLengthMenu: 'Tampilkan _MENU_ entri',
       sZeroRecords: 'Tidak ditemukan data yang sesuai',
       sInfo: 'Menampilkan _START_ sampai _END_ dari _TOTAL_ entri',
       sInfoEmpty: 'Menampilkan 0 sampai 0 dari 0 entri',
       sInfoFiltered: '(disaring dari _MAX_ entri keseluruhan)',
       sInfoPostFix: '',
       sSearch: 'Cari:',
       sUrl: '',
       oPaginate: {
         sFirst: '<i class="fas fa-angle-double-left"></i>',
         sPrevious: '<i class="fas fa-angle-left"></i>',
         sNext: '<i class="fas fa-angle-right"></i>',
         sLast: '<i class="fas fa-angle-double-right"></i>'
       }
     }
   })
 })
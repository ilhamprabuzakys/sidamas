$(function () {
    const formRepeaters = $('.form-repeater');
    formRepeaters.on('submit', function(e) { e.preventDefault(); });

    formRepeaters.repeater(getRepeaterConfig({
        isFirstItemUndeletable: true
    }))
});

function getRepeaterConfig(config) {
    return {
       initEmpty: false,
       isFirstItemUndeletable: config?.isFirstItemUndeletable ?? false,
       show: function () {
            const elements = $(this).find('.form-control');
            
            console.log('Daftar el:', elements);
            
            elements.each(function () {
                $(this).val('');
            });
            
            $(this).slideDown();
        
       },
       hide: async function (e) {
           const isExist = $(this).find('input[type="text"], input[type="radio"], input[type="number"]').filter(function() {
               if ($(this).attr('type') === 'radio') {
                   return $(this).is(':checked');
               } else {
                   return $(this).val() !== "";
               }
           }).length > 0;

           if (!isExist) {
               $(this).slideUp(e);
               return;
           }
         
           const confirmation = await showSwalConfirm('Apakah anda yakin untuk menghapus data ini?', 'Ya, hapus data');
           confirmation.isConfirmed && $(this).slideUp(e);
       },
   }
}
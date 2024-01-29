$(document).ready(function () {
    $("select:is(.select2)").each(function () {
        $(this).select2({
            //placeholder: $(this).find('option:first').text(),
            dropdownParent: $(this).parent(),
            allowClear: false,
            language: {
                noResults: function () {
                    return `<span style="padding: 12px 15px">Hasil tidak ditemukan</span>`;
                },
            },
            escapeMarkup: function (markup) {
                return markup;
            }
        });

        // $(this).on('change', function () {
        //     var selectedValue = $(this).val();
        //     console.log("Nilai yang dipilih: " + selectedValue);
        // });
    });
});

// $(function () {
//     var e = $(".select2"),
//         t = $(".selectpicker");
//     t.length && t.selectpicker(),
//         e.length &&
//             e.each(function () {
//                 var e = $(this);
//                 e.wrap('<div class="position-relative"></div>'),
//                     e.select2({
//                         placeholder: "Select value",
//                         dropdownParent: e.parent(),
//                     });
//             });
// });

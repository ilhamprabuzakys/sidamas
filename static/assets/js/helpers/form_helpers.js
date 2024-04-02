// Label
document.querySelectorAll("label.required").forEach((label) => {
    const supElement = document.createElement("sup");
    supElement.className = "ms-0-15r text-danger";
    supElement.textContent = "*";

    label.appendChild(supElement);
});

document.querySelectorAll("label.optional").forEach((label) => {
    const supElement = document.createElement("span");
    supElement.className = "ms-2 text-muted";
    supElement.textContent = "(Opsional)";

    label.appendChild(supElement);
});


function resetFormOld(form) {
    console.log('Terpanggil 2 Resetting this form :', form);

    if (!$(form).hasClass('dont-reset') && !$(form).hasClass('filter-form')) {
        console.log('Resetting this form :', form);
        $(form).find('.select2').each(function () {
            console.log('Terdapat select2');
            let isMultiple = $(this).prop('multiple');
            $(this).val(isMultiple ? [] : '').trigger('change');
        });

        form.reset();
    }
}


/* ==========================
 * FORM RESET FUNCTIONALLITY
============================= */
$(function () {
    // Reset
    function resetForm(form) {
        if (!form || typeof form.hasClass !== 'function') { return; }

        // If using form object
        if (form.hasClass('dont-reset') || form.hasClass('filter-form')) {
            // console.log('Form not resetted because it\'s forbidden ...');
            form.find('.select2').val(null).trigger('change');
            return;
        }

        form.find('.select2').val(null).trigger('change');
        form.find('input[type="text"]').val('');
        form.find('input[type="number"]').val(0);
        form.find('input[type="textarea"]').val('');
        form.find('input[type="checkbox"]').prop('checked', false);
        form.find('input[type="file"]').val(null);

        // console.log('Resetted this form :', form);

        form.trigger('reset');
    }


    $('.modal').on('hidden.bs.modal', function () {
        const form = $(this).closest('form');
        // console.log('Form awal :', form);
    
        if (form) {
            resetForm(form);
        }
    });
    

    $('[type="reset"]').on('click', function () {
        let form = $(this).closest('form')[0];
        if (!form) return;
        resetForm(form);
    });
});

// ******** CLEAVE ********
if (window.Cleave) {
    // Phone number
    const phone = document.querySelector('.cleave-phone');
    phone && new Cleave(phone, {
        phone: true,
        phoneRegionCode: "ID",
    });

    const ikp = document.querySelectorAll('.cleave-ikp');
    if (ikp.length > 0) {
        ikp.forEach(element => {
            new Cleave(element, {
                delimiters: [","],
                blocks: [1, 2],
                numericOnly: true,
                min: 0,
                max: 4,
            });
        });
    }
}

// ******** MAX MIN LENGTH ********
if ($('input[type="number"]').attr("maxlength")) {
    $('input[type="number"]').each(function () {
        $(this).maxlength({
            validate: !0,
            alwaysShow: false,
            threshold: $(this).attr("maxlength"),
        });
    });
}

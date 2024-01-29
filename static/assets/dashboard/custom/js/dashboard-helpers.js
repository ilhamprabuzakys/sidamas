function goBack() {
    window.history.back();
}

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

function getCSRFToken() {
    return getCookie("csrftoken");
}

function getHeaders(type) {
    return {
        "X-CSRFToken": getCSRFToken(),
        "Content-Type": type ?? "application/json",
    };
}

// Get datatable language config
function dt_lang_config() {
    const language = {
        sEmptyTable: "Tidak ada data yang tersedia pada tabel ini",
        sProcessing: "Sedang memproses...",
        sLengthMenu: "Tampilkan _MENU_ entri",
        sZeroRecords: "Tidak ditemukan data yang sesuai",
        sInfo: "Menampilkan _START_ sampai _END_ dari _TOTAL_ entri",
        sInfoEmpty: "Menampilkan 0 sampai 0 dari 0 entri",
        sInfoFiltered: "(disaring dari _MAX_ entri keseluruhan)",
        sInfoPostFix: "",
        sSearch: "Pencarian:",
        sUrl: "",
        oPaginate: {
            sFirst: '<i class="fas fa-angle-double-left"></i>',
            sPrevious: '<i class="fas fa-angle-left"></i>',
            sNext: '<i class="fas fa-angle-right"></i>',
            sLast: '<i class="fas fa-angle-double-right"></i>',
        },
    };
    return language;
}

document.querySelectorAll("label.required").forEach((label) => {
    const supElement = document.createElement("sup");
    supElement.className = "ms-0-15r text-danger";
    supElement.textContent = "*";

    label.appendChild(supElement);
});

// Vue
if (window.Vue) {
    // Setup vue-sfc-loader
    const options = {
        moduleCache: {
            vue: Vue,
        },
        async getFile(url) {
            const res = await fetch(url);
            if (!res.ok)
                throw Object.assign(new Error(res.statusText + " " + url), {
                    res,
                });
            return {
                getContentData: (asBinary) =>
                    asBinary ? res.arrayBuffer() : res.text(),
            };
        },
        addStyle(textContent) {
            const style = Object.assign(document.createElement("style"), {
                textContent,
            });
            const ref = document.head.getElementsByTagName("style")[0] || null;
            document.head.insertBefore(style, ref);
        },
        log(type, ...args) {
            console.log(type, ...args);
        },
    };

    const { loadModule } = window["vue3-sfc-loader"];

    const base_component_url = "/static/assets/dashboard/vue/";

    // To make it accessible outside this file.
    window.loadVueComponent = async (path) => {
        return loadModule(base_component_url + path, options);
    };

    // A snippet to load the component (only from this file)
    function loadComponent(path) {
        return Vue.defineAsyncComponent(() =>
            loadModule(base_component_url + path, options)
        );
    }
    // END Setup vue-sfc-loader
}

/*
    Cleave Helpers
*/

if (window.Cleave) {
    // Phone number
    let phone = document.querySelector('.cleave-phone');
    phone && new Cleave(phone, {
        phone: true,
        phoneRegionCode: "ID",
    });
}

if ($('.input-maxlength').attr("maxlength")) {
    $('.input-maxlength').each(function() {
        $(this).maxlength({
            validate: !0,
            threshold: $(this).attr("maxlength"),
        });
    });
}


if ($('input[name="jumlah_kegiatan"]').attr("type") == "number") {
    // $('input[name="jumlah_kegiatan"]').attr('type', 'text');
    // new Cleave('input[name="jumlah_kegiatan"]', {
    //     numeral: true,
    //     prefix: ' kali',
    //     tailPrefix: true
    // });
}

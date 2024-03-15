// AJAX Helpers
function getCSRFTokenFromMeta() {
    return document.querySelector(
        'meta[name="csrf-token"]'
    ).content;
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
    const csrfTokenFromCookie = getCookie('csrftoken');
    return csrfTokenFromCookie || getCSRFTokenFromMeta();
}

function getHeaders(type) {
    return {
        "X-CSRFToken": getCSRFToken(),
        'Content-Type': type ?? 'application/json',
    };
}

function checkStatus(status, startNum) {
    return String(status).startsWith(startNum);
}

axios.defaults.headers.common['X-CSRFToken'] = getCSRFToken();
axios.defaults.headers.post['Content-Type'] = 'application/json';


/* ==========================
 * SHORTCUT HTTP REQUEST
============================= */

async function handleDestroy(config) {
    const id = config?.id;
    const detailName = config?.detail_name || '';
    const name = config?.name;
    const apiURL = config?.apiURL;

    const additionalConfirmInfo = detailName == '' ? 'yang dipilih' : `:<br><b>${detailName}</b>`;

    const additionalResultInfo = detailName == '' ? 'yang dipilih' : `: <b>${detailName}</b>`;

    const confirmationText = `Untuk menghapus data <b>${name}</b> ${additionalConfirmInfo}? <br> Data yang dihapus tidak dapat <b>dipulihkan</b> kembali`;

    const confirmResult = await showSwalConfirm(confirmationText, 'Ya, hapus data');

    if (!confirmResult.isConfirmed) return;

    showSwalLoading();

    await sleep(1000);

    try {
        const response = await axios.delete(`${apiURL}/${id}/`);

        reloadTable(table);

        showSwalSuccess('Berhasil', `Data ${name} ${additionalResultInfo} berhasil <b>dihapus</b>`, 3000);
    } catch (error) {
        console.log('Terjadi kesalahan : ', error);
        showSwalGenericError();
    }
}
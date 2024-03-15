async function sleep(duration) {
    return await new Promise(resolve => setTimeout(resolve, duration));
}

function getRandomInt(min, max) {
    if (min && max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min; [min, max]
    } else {
        return Math.floor(Math.random() * min);
    }
}

function getRandomItem(arr) {
    const randomIndex = Math.floor(Math.random() * arr.length);
    const item = arr[randomIndex];

    return item;
}

function getStatusClass(data) {
    const statusMap = {
        'BAHAYA': 'danger',
        'WASPADA': 'warning',
        'SIAGA': 'primary',
        'AMAN': 'success'
    };

    data = data.toUpperCase();

    return statusMap[data] || 'secondary';
}


function capitalizeFirstChar(str) {
    if (typeof str !== 'string' || str.length === 0) {
        return str;
    }
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function block(el) {
    el.block({
        message: '<div class="spinner-border text-success" role="status"></div>',
        // timeout: 1e3,
        css: {
            backgroundColor: "transparent",
            border: "0"
        },
        overlayCSS: {
            backgroundColor: "#fff",
            opacity: .6
        }
    });
}

function blockWithSpinner(el) {
    el.block({
        message: '<div class="spinner-border text-success" role="status"></div>',
        // timeout: 1e3,
        css: {
            backgroundColor: "transparent",
            border: "0"
        },
        overlayCSS: {
            backgroundColor: "#fff",
            opacity: .6
        }
    });
}

function unblock(el) {
    el.unblock();
}

function goBack() {
    window.history.back();
}

function hideAllModal() {
    $('.modal').modal('hide');
}

function toggleFullscreen() {
    if (document.fullscreenElement) {
      document.exitFullscreen();
    } else {
      document.documentElement.requestFullscreen();
    }
}

function navigateToPage(url) {
    window.location.href = url;
}

// Media sosial
var url = window.location.href;

function shareOnFacebook() {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank');
}

function shareOnTwitter() {
    window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}`, '_blank');
}

function shareOnWhatsApp() {
    window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(url)}`, '_blank');
}

function shareOnTikTok() {
    window.open(`https://www.tiktok.com/upload?reference=${encodeURIComponent(url)}`, '_blank');
}

function shareOnInstagram() {
    window.open(`https://www.instagram.com/share?url=${encodeURIComponent(url)}`, '_blank');
}
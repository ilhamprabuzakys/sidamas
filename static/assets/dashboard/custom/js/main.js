/**==========================
**** MAIN - DASHBOARD ****
=========================***/

$(document).ready(function () {
    moment.locale('id');

    new PureCounter({ selector: '.purecounter' });

    expandBodyLength();

    // FIX SELECT 2 ON MODAL
    $('.modal').on('shown.bs.modal', function () {
        if ($(this).find('.modal-dialog-scrollable .modal-body').find('select.select2').length > 0) {
            $(this).find('.modal-dialog-scrollable .modal-body').css('overflow-x', 'hidden');
        }
    });

    // FIX OVERFLOW-X AXIS INSIDE SCROLLABLE DIALOG MODAL
    $('.modal').on('hidden.bs.modal', function () {
        $(this).find('.modal-dialog-scrollable .modal-body').css('overflow-x', '');
    });

});

function fetchSearchResults() {
    console.log('Searching a page with query :', this.searchInput);

    var role = document.getElementById('global_search_input').getAttribute('data-role');
    var url = `/static/data/pages/${role}_pages.json`;

    if (this.searchInput.length > 0) {
        axios.get(url)
            .then(response => {
                this.searchResults = response.data.pages.filter(page =>
                    page.name.toLowerCase().includes(this.searchInput.toLowerCase())
                );
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    } else {
        this.searchResults = [];
    }
}

function expandBodyLength() {
    $("#layout-navbar").addClass("container-fluid").removeClass("container-xxl");
    $("#main-content").addClass("container-fluid").removeClass("container-xxl");
}

// ******** HANDLE FILTER ********
$('#resetFilter, #applyFilter').on('click', function () {
    $(this).closest('.dropdown-menu').prev('.dropdown-toggle').dropdown('toggle');
});


const handleLogout = () => {
    $("#logoutModal").modal("show");
};

const handleLogoutConfirm = () => {
    $("#logoutModal").modal("hide");
};

let delimiters = ['{{', '}}'];

const Pagination = {
    name: 'Pagination',
    props: {
        item: { type: Object, required: true, },
        scrollUp : { type: Boolean, default: false }
    },
    delimiters,
    emits: ['go'],
    mounted() {
        // console.log(this.item)
    },
    setup(props, { emit }) {
        const cantGoBack = computed(() => props.item.currentPage <= 1 || props.item.totalPage == 0);
        const cantGoNext = computed(() => props.item.currentPage == props.item.totalPage || props.item.totalPage == 0);

        const isActivePage = (page) => props.item.currentPage === page;

        const scrollToTop = () => document.querySelector('#layout-container').scrollIntoView({ behavior: 'smooth', block: 'start' });

        const goToPage = (page) => {
            const baseUrl = window.location.pathname;
            const queryParams = new URLSearchParams(window.location.search);
            if (page == 1) {
                queryParams.delete('page');
            } else {
                queryParams.set('page', page);
            }
            const queryString = queryParams.toString();
            const newUrl = `${baseUrl}${queryString ? `?${queryString}` : ''}`;
            window.history.pushState({ path: newUrl }, '', newUrl);
            props.item.currentPage = page;
            emit('go', page);
            props.scrollUp && scrollToTop();
        }

        const goToNextPage = () => {
            const nextPage = props.item.currentPage + 1;
            const baseUrl = window.location.pathname;
            const queryParams = new URLSearchParams(window.location.search);
            queryParams.set('page', nextPage);
            const queryString = queryParams.toString();
            const newUrl = `${baseUrl}${queryString ? `?${queryString}` : ''}`;
            window.history.pushState({ path: newUrl }, '', newUrl);
            props.item.currentPage = nextPage;
            emit('go', nextPage);
            props.scrollUp && scrollToTop();
        }

        const goToPreviousPage = () => {
            const previousPage = props.item.currentPage - 1;
            const baseUrl = window.location.pathname;
            const queryParams = new URLSearchParams(window.location.search);
            if (previousPage > 0) {
                queryParams.set('page', previousPage);
            } else {
                queryParams.delete('page');
            }
            const queryString = queryParams.toString();
            const newUrl = `${baseUrl}${queryString ? `?${queryString}` : ''}`;
            window.history.pushState({ path: newUrl }, '', newUrl);
            props.item.currentPage = previousPage;
            emit('go', previousPage);
            props.scrollUp && scrollToTop();
        }

        const getTableInfo = computed(() => {
            const currentPage = props.item.currentPage;
            const totalEntries = props.item.total;
            const entriesPerPage = props.item.perPage;
            let startIndex = (currentPage - 1) * entriesPerPage + 1;
            let endIndex = currentPage * entriesPerPage;
            
            if (endIndex > totalEntries) {
                endIndex = totalEntries;
            }
            
            if (currentPage === props.item.totalPage) {
                startIndex = (currentPage - 1) * entriesPerPage + 1;
                endIndex = totalEntries;
            }

            return `Menampilkan <b>${startIndex}</b> sampai <b>${endIndex}</b> dari total <b>${totalEntries}</b> entri`;
        });
        return {
            cantGoBack,
            cantGoNext,
            isActivePage,
            goToPreviousPage,
            goToPage,
            goToNextPage,
            getTableInfo,
        }
    },
    template: `
    <div class="row mt-4 mb-3">
        <div class="d-flex col-sm-12 col-md-5 align-items-center">
            <div id="__table_info">
                <span v-html="getTableInfo" class="text-secondary"></span>
            </div>
        </div>
        <div class="col-sm-12 col-md-7">
            <nav id="__table_pagination">
                <ul class="pagination justify-content-end">
                    <li class="page-item first" :class="cantGoBack && 'disabled'">
                        <button :disabled="cantGoBack" class="page-link" @click="goToPage(1)"><i class="ti ti-chevrons-left ti-xs"></i></button>
                    </li>
                    <li class="page-item prev" :class="cantGoBack && 'disabled'">
                        <button :disabled="cantGoBack" class="page-link" @click="goToPreviousPage()">
                            <i class="ti ti-chevron-left ti-xs"></i>
                        </button>
                    </li>
                    <li v-for="page in item.totalPage" :key="page" :class="{ 'page-item': true, 'active disabled': isActivePage(page) }">
                        <button class="page-link" @click="isActivePage(page) ? null : goToPage(page)" v-text="page"></button>
                    </li>
                    <li class="page-item next" :class="cantGoNext && 'disabled'">
                        <button :disabled="cantGoNext" class="page-link" @click="goToNextPage()">
                            <i class="ti ti-chevron-right ti-xs"></i>
                        </button>
                    </li>
                    <li class="page-item last" :class="cantGoNext && 'disabled'">
                        <button :disabled="cantGoNext" class="page-link" @click="goToPage(item.totalPage)"><i class="ti ti-chevrons-right ti-xs"></i></button>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
    `,
};

const Table = {
    name: 'Table',
    props: { item: { type: Object, required: true }, pagination: { type: Object, required: true} },
    components: { 'v-pagination': Pagination },
    delimiters,
    emits: ['go-pagination'],
    setup(props, { emit }) {
        const getPaginationArgs = computed(() => {
            const args = {
                currentPage: props.pagination.currentPage,
                totalPage: props.pagination.totalPage,
                pageLength: props.item.pagedData?.length,
                total: props.pagination.total,
                perPage: props.pagination.perPage,
            };

            return args;
        });

        return { getPaginationArgs }
    },
    template: `
        <div>
            <!-- Table -->
            <table id="__table" class="table table-bordered">
                <thead>
                    <slot name="thead"></slot>
                </thead>
                <tbody class="align-tr-middle text-white">
                    <slot name="tbody"></slot>
                    <template v-if="item.pagedData.length == 0">
                        <slot name="not-found"></slot>
                    </template>
                </tbody>
            </table>
            <!--/ Table -->

            <!-- Pagination -->
            <v-pagination :item="getPaginationArgs" :scroll-up="true" @go="(page) => $emit('go-pagination', page)"></v-pagination>
            <!--/ Pagination -->
        </div>
    `
};

const TableBasicFilter = {
    name: 'TableBasicFilter',
    props: { item: { type: Object, required: true } },
    delimiters,
    emits: ['set-page', 'set-perpage', 'set-data'],
    setup(props, {emit}) {
        const perPage = ref(getValueFromParams('per_page') ? parseInt(getValueFromParams('per_page')) : props.item.totalDefault);
        const search = ref('');

        const buildQuery = (data, columns, search) => {
            const query = search.toUpperCase();
            return data.filter(item => {
                return columns.some(column => {
                    let columnValue = '';
                    
                    if (column == 'nama_satker') {
                        console.log(column);
                        columnValue = String(item.satker['nama_satker']).toUpperCase();
                    } else {
                        columnValue = String(item[column]).toUpperCase();
                    }
                    
                    return columnValue.includes(query);
                });
            });
        }

        const handleChange = () => emit('set-perpage', perPage.value);

        const setPerPageParams = () => {
            const baseURL = window.location.pathname;
            const queryParams = new URLSearchParams(window.location.search);

            if (perPage.value == props.item.totalDefault) {
                queryParams.delete('per_page');
            } else {
                queryParams.set('per_page', perPage.value);
            }
            const queryString = queryParams.toString();
            const newUrl = `${baseURL}${queryString ? `?${queryString}` : ''}`;
            window.history.pushState({ path: newUrl }, '', newUrl);
        };

        watch(perPage, setPerPageParams);
        
        const handleSearch = async () => {
            emit('set-page', 1);
            
            block($('#__table'));
            await sleep(1000);

            const data = buildQuery(props.item.tableData, props.item.columns, search.value);
            emit('set-data', data);

            unblock($('#__table'));
        }

        onMounted(() => {
            emit('set-perpage', perPage.value);
        });

        return { perPage, search, handleSearch, handleChange }
    },
    template: `
    <div id="__table_basic_filter" class="row d-flex justify-content-between align-items-center mt-4 mb-2">
        <div id="__table_basic_filter__show_entry" class="col-lg-1 col-md-1 col-sm-1 mb-3">
            <label for="filter__show_entry" class="form-label">Tampilkan</label>

            <select class="form-select form-select-md" id="filter__show_entry" style="width: 100px" v-model="perPage" @change="handleChange">
                <option value="5">1-5</option>
                <option value="10">1-10</option>
                <option value="20">1-20</option>
                <option value="50">1-50</option>
                <option value="100">1-100</option>
            </select>
        </div>
        <div id="__table_basic_filter__search"class="col-lg-7 col-md-5 col-sm-4 mb-3 d-flex justify-content-end">
            <div style="width: 300px;">
                <label for="filter__search" class="form-label">Pencarian</label>
                <input type="search" id="filter__search" class="form-control" v-model="search" @input="handleSearch"
                    placeholder="Ketikkan pencarian disini ..." />
            </div>
        </div>
    </div>
    `
}

const GenericFilter = {
    name: 'Generic Filter',
    props: { data: Object, satker: Object },
    delimiters,
    emits: ['update', 'reset'],
    setup(props, { emit }) {

        const filter = ref({ date: '', kegiatan: '', status: '', satker: ''});

        const hover = ref(false);

        const isFilteredSomething = computed(() => {
            return Object.values(filter.value).some(value => value !== '');
        });
      
        const resetFilters = () => {
            filter.value = { date: '', kegiatan: '', status: '', satker: '' };
            $('#filter__satker').val('').trigger('change');
            $('#filter__date').val('').trigger('change');
        };

        const handleResetFilter = async (type) => {
            if (type == 'all') {
                block($('#__table'));
                await sleep(500);
                
                resetFilters();

                emit('update', props.data);
                unblock($('#__table'));
                
                return;
            }
            
            if (filter.value[type] == '') return;
            
            filter.value[type] = '';

            if (type == 'date') {
                $('#filter__date').val('').trigger('change');
            }
        }

        const handleFilterDate = (data) => {
            if (filter.value.date == '') return data;

            const [datePartStart, datePartEnd] = filter.value.date.split('-');
            const startDate = moment(datePartStart.trim(), 'MM/DD/YYYY');
            const endDate = moment(datePartEnd.trim(), 'MM/DD/YYYY');

            return data.filter(item => {
                if (!item.tanggal_awal) return false;
                
                const itemDate = moment(item.tanggal_awal, 'YYYY-MM-DD');
                const expression = itemDate.isBetween(startDate, endDate, null, '[]');
                
                return expression;
            });
        }

        const handleFilterKegiatan = (data) => {
            if (filter.value.kegiatan == '') return data;

            const [rangeAwal, rangeAkhir] = filter.value.kegiatan.split("-").map(Number);

            return data.filter(item => item.jumlah_kegiatan >= rangeAwal && item.jumlah_kegiatan <= rangeAkhir);
        }
        
        const handleFilterStatus = (data) => {
            if (filter.value.status === '') return data;
            
            const statusMap = {
                0: 1,
                1: 2,
            };
            const expectedStatus = statusMap[filter.value.status];

            return data.filter(item => item.status == expectedStatus);
        }
        
        const handleFilterSatker = (data) => {
            if (filter.value.satker == '') return data;
            
            return data.filter(item => item.satker.id == filter.value.satker);
        }

        const handleFilter = async () => {
            block($('#__table'));

            console.log('[INFO]: Applying filter using data : ', {
                date: filter.value.date,
                status: filter.value.status,
                kegiatan: filter.value.kegiatan,
                satker: filter.value.satker,
            })

            await sleep(500);

            emit('reset');
            removeParams('page')

            if (!isFilteredSomething.value) {
                emit('update', props.data);
                unblock($('#__table'));
                return;
            }

            let filteredData = props.data;

            filteredData = handleFilterDate(filteredData)
            filteredData = handleFilterKegiatan(filteredData)
            filteredData = handleFilterStatus(filteredData)
            filteredData = handleFilterSatker(filteredData)

            emit('update', filteredData);

            unblock($('#__table'));
        };

        const listSatker = ref({});

        const getSatkerData = async () => {
            try {
                const response = await axios.get('/users/api/v1/satker/');
                listSatker.value = response.data;
            } catch (error) {
                showSwalGenericError();
                console.error('Terjadi kesalahan:', error);
            }
        }

        onMounted(async () => {
            $('#filter__satker').on('change', (event) => filter.value.satker = event.target.value);

            await getSatkerData();

            const $filterDateInput = $('#filter__date');

            const today = moment();
            const startOfWeek = moment().subtract(today.day(), 'days');
            const startOfMonth = moment().startOf('month');
            const startOfQuarter = moment().startOf('year').startOf('quarter');

            $filterDateInput.daterangepicker({
                showDropdowns: true,
                autoUpdateInput: false,
                ranges: {
                    'Hari ini': [today, today],
                    'Kemarin': [today.clone().subtract(1, 'days'), today.clone().subtract(1, 'days')],
                    'Minggu ini': [startOfWeek, today],
                    'Bulan ini': [startOfMonth, today],
                    'Triwulan 1 (Januari - Maret)': [startOfQuarter, startOfQuarter.clone().add(2, 'months').endOf('month')],
                    'Triwulan 2 (April - Juni)': [startOfQuarter.clone().add(3, 'months'), startOfQuarter.clone().add(5, 'months').endOf('month')],
                    'Triwulan 3 (Juli - September)': [startOfQuarter.clone().add(6, 'months'), startOfQuarter.clone().add(8, 'months').endOf('month')],
                    'Triwulan 4 (Oktober - Desember)': [startOfQuarter.clone().add(9, 'months'), moment().endOf('year')],
                },
                locale: {
                    customRangeLabel: "Rentang Lainnya",
                    cancelLabel: 'Batalkan',
                    applyLabel: 'Terapkan'
                }
            });

            $filterDateInput.on('apply.daterangepicker', function(ev, picker) {
                const value = picker.startDate.format('MM/DD/YYYY') + ' - ' + picker.endDate.format('MM/DD/YYYY');
                $(this).val(value);
                filter.value.date = value;
            });
            
            $filterDateInput.on('cancel.daterangepicker', function(ev, picker) {
                $(this).val('');
                filter.value.date = '';
            });

            // FIX DATE RANGEPICKER CLOSE PARENT
            $("div.daterangepicker").click((e) => e.stopPropagation());
        });

        return { hover, filter, handleFilter, isFilteredSomething, handleResetFilter, listSatker }
    },
    template: `
        <div class="btn-group dropstart me-2">
            <button type="button" class="btn btn-outline-secondary rounded-pill dropdown-toggle hide-arrow"
                data-bs-toggle="dropdown" aria-expanded="false" data-bs-offset="10,20"
                data-bs-auto-close="outside"><i class="fas fa-sliders me-2"></i>Filter Data</button>
            <ul class="dropdown-menu w-px-500">
                <li>
                    <h5 class="dropdown-header text-uppercase">Filter Data</h5>
                </li>
                <li>
                    <hr class="dropdown-divider">
                </li>
                <div class="pt-0 pb-3 px-3" id="filter__form">
                    <div class="mb-2" v-if="satker.level != 2">
                        <label for="filter__status_pengiriman" class="form-label">Status Pengiriman</label>
                        <select id="filter__status_pengiriman" class="form-select"
                            v-model="filter.status" required>
                            <option disabled>-- Pilih Status Pengiriman --</option>
                            <option value="">-- Semua --</option>
                            <option value="0">Belum Terkirim</option>
                            <option value="1">Terkirim</option>
                        </select>
                    </div>
                    <div class="mb-2">
                        <label for="filter__date" class="form-label">Rentang Tanggal</label>

                        <div class="input-group input-group-merge">
                            <input type="text" id="filter__date" class="form-control"
                                placeholder="Pilih Rentang Tanggal" />
                            <span class="input-group-text cursor-pointer" :class="hover ? 'text-danger' : 'text-secondary'" @mouseleave="hover=false" @mouseenter="hover=true"
                                @click="handleResetFilter('date')"><i class="fas fa-xmark"></i></span>
                        </div>
                    </div>
                    <div class="mb-2">
                        <label for="filter__kegiatan" class="form-label">Rentang Kegiatan</label>

                        <select class="form-select form-select-md" id="filter__kegiatan" v-model="filter.kegiatan">
                            <option selected disabled>--Pilih rentang kegiatan--</option>
                            <option value="">Semua</option>
                            <option value="1-10">1 - 10 kegiatan</option>
                            <option value="11-20">11 - 20 kegiatan</option>
                            <option value="21-50">21 - 50 kegiatan</option>
                            <option value="51-100">51 - 100 kegiatan</option>
                        </select>
                    </div>
                    <div class="mb-2">
                        <label for="filter__satker" class="form-label">Satuan Kerja Pelaksana</label>

                        <select class="form-select form-select-md select2 no-placeholder" id="filter__satker">
                            <option selected disabled>--Pilih satuan kerja --</option>
                            <option value="">Semua</option>
                            <option v-for="(item, index) in listSatker" :value="item.id">{{ item.nama_satker }}</option>
                        </select>
                    </div>
                </div>
                <li>
                    <hr class="dropdown-divider">
                </li>
                <div class="list-dropdown-button d-flex justify-content-end px-3 py-2">
                    <button type="button" class="btn btn-label-secondary fw-semibold me-2 px-6">
                        <i class="fas fa-xmark me-2"></i>Batalkan</button>
                    <button type="button" class="btn btn-primary fw-semibold px-6" @click="handleFilter">
                        <i class="fas fa-save me-2"></i>
                        Terapkan</button>
                </div>
            </ul>
        </div>
        <transition>
            <div v-if="isFilteredSomething">
                <button class="all-unset text-primary" @click="handleResetFilter('all')">
                    <i class="fas fa-xmark me-2"></i>
                    Bersihkan filter
                </button>
            </div>
        </transition>
    `
}

const ActionBTN = {
    name: 'ActionBTN',
    props: {
        item: { type: Object, required: true },
        level: { type: Number, required: true },
        url: { type: String, required: true }
    },
    delimiters,
    emits: ['edit', 'update'],
    setup(props, { emit }) {
        const isDataBNNKdiBNNP = computed(() => {
            return props.level === 0 && props.item.level === 1 && props.item.status === 2;
        });

        const isKirimable = computed(() => {
            const BNNP = props.level === 0 && props.item.status  < 2;
            const BNNK = props.level === 1 && props.item.status  === 0;
            const PUSAT = props.level !== 2;

            return PUSAT && (BNNP || BNNK);
        });

        const isEditable = computed(() => {
            const BNNP = props.level === 0 && props.item.status  < 2;
            const BNNK = props.level === 1 && props.item.status  === 0;
            const PUSAT = props.level === 2;
            return PUSAT || BNNP || BNNK;
        });

        const showKirimBTN = computed(() => props.level != 2);
        const showEditBTN = computed(() => props.item.level == props.level || props.level == 2)

        const handleKirim = async () => {
            const keteranganStatus = {
                0: 'Pusat',
                1: 'Pusat'
            };

            const args =  {
                id: props.item.id,
                nama: props.item.nama,
                keterangan: keteranganStatus[props.item.status] || '?'
            }

            const confirmResult = await showSwalConfirm(`Apakah anda yakin untuk mengirim kegiatan ID ${args.id} dari Satuan Kerja <b>${args.nama}</b> ke <b>${args.keterangan}</b>`, 'Ya, kirim data');

            if (!confirmResult.isConfirmed) return;

            showSwalLoading();

            await sleep(1000);

            try {
                const response = await axios.post(`/kegiatan/api/v1/dayatif/${props.url}/kirim_kegiatan/`, { kegiatan_id : args.id });

                const sendedToParent = response.data.parent.keterangan;

                showSwalSuccess('Berhasil', `Data <b>kegiatan</b> dari <b>${props.item.nama}</b> telah berhasil dikirimkan ke <b>${sendedToParent}</b>`);

                emit('update');
            } catch (error) {
                showSwalGenericError();
                console.error('Terjadi kesalahan :', error);
            }
        };

        const handleDestroy = async () => {
            const deleteArgs = {
                id: props.item.id,
                name: 'kegiatan',
                detail_name: props.item.nama,
                apiURL: `/kegiatan/api/v1/dayatif/${props.url}`,
                usingDT: false,
            };

            const res = await handleDelete(deleteArgs);
            if (res) emit('update');
        }

        return {
            isDataBNNKdiBNNP,
            isKirimable,
            isEditable,
            showKirimBTN,
            showEditBTN,
            handleKirim,
            handleDestroy,
        }
    },
    template: `
        <template v-if="!isDataBNNKdiBNNP">
            <div class="list-button gx-3 text-uppercase">

                <template v-if="showKirimBTN">
                    <button @click='isKirimable && handleKirim()'
                        :disabled="!isKirimable"
                        :class="isKirimable ? 'bg-primary' : 'bg-secondary'"
                        class="badge text-white text-decoration-none mb-1">
                        <i class="fas fa-paper-plane me-2"></i>Kirim
                    </button>
                </template>
                
                <template v-if="showEditBTN">
                    <button @click="isEditable && $emit('edit', item.id)"
                        :disabled="!isEditable"
                        :class="isEditable ? 'bg-success' : 'bg-secondary'"
                        class="badge text-white text-decoration-none mb-1">
                        <i class="fas fa-edit me-2"></i>Edit
                    </button>
                    
                    <button @click='isEditable && handleDestroy()'
                        :disabled="!isEditable"
                        :class="isEditable ? 'bg-danger' : 'bg-secondary'"
                        class="badge text-white text-decoration-none mb-1">
                        <i class="fas fa-trash-alt me-2"></i>Hapus
                    </button>
                </template>
            </div>
        </template>
        <div v-else class="fade-in-text-0 cursor-pointer text-center">Data sudah <b>dikirimkan</b> ke <b>PUSAT</b></div>
    `,
};

const ExportBTN = {
    name: 'ExportBTN',
    props: { name: { type: String, required: true }, url: { type: String, required: true }, satker: { type: Object, required: false } },
    delimiters,
    setup(props) {
        const exportData = ref({ status: '1', waktu: 'semua' });

        const handleExport3 = () => {
            const tbl = document.getElementById('__table');
            const wb = XLSX.utils.table_to_book(tbl);
            const title = document.querySelector('#headline h3').textContent
            const fileName = `${title}.xlsx`;
            
            XLSX.writeFile(wb, fileName);
        }

        const handleExport = () => {
            const table = document.querySelector('#__table');
            const title = document.querySelector('#headline h3').textContent.trim();
            const wb = XLSX.utils.table_to_book(table);
            const fileName = `${title}.xlsx`;
        
            // Mendapatkan sheet pertama dari workbook
            const ws = wb.Sheets[wb.SheetNames[0]];
        
            // Mendapatkan semua kolom, kecuali dua kolom terakhir
            const range = XLSX.utils.decode_range(ws['!ref']);
            for (let C = range.s.c; C < range.e.c - 1; ++C) {
                // Mendapatkan lebar kolom
                let maxColWidth = 0;
                for (let R = range.s.r; R <= range.e.r; ++R) {
                    const cell_address = { c: C, r: R };
                    const cell_ref = XLSX.utils.encode_cell(cell_address);
                    const cell = ws[cell_ref];
                    if (!cell) continue;
                    const cellText = XLSX.utils.format_cell(cell);
                    const cellWidth = cellText.length;
                    if (cellWidth > maxColWidth) maxColWidth = cellWidth;
                }
                // Set width pada kolom
                ws['!cols'] = ws['!cols'] || [];
                ws['!cols'][C] = { wch: maxColWidth };
            }
        
            // Mendapatkan dua kolom terakhir
            const lastColIndex = range.e.c;
            const secondLastColIndex = lastColIndex - 1;
        
            // Sembunyikan dua kolom terakhir
            if (!ws['!cols']) ws['!cols'] = [];
            if (!ws['!cols'][lastColIndex]) ws['!cols'][lastColIndex] = {};
            ws['!cols'][lastColIndex].hidden = true;
            if (!ws['!cols'][secondLastColIndex]) ws['!cols'][secondLastColIndex] = {};
            ws['!cols'][secondLastColIndex].hidden = true;
        
            // Mendapatkan semua baris
            for (let R = range.s.r; R <= range.e.r; ++R) {
                // Mendapatkan tinggi baris
                let maxRowHeight = 0;
                for (let C = range.s.c; C <= range.e.c; ++C) {
                    const cell_address = { c: C, r: R };
                    const cell_ref = XLSX.utils.encode_cell(cell_address);
                    const cell = ws[cell_ref];
                    if (!cell) continue;
                    const cellText = XLSX.utils.format_cell(cell);
                    const cellHeight = cellText.split('\n').length;
                    if (cellHeight > maxRowHeight) maxRowHeight = cellHeight;
                }
                // Set height pada baris
                ws['!rows'] = ws['!rows'] || [];
                ws['!rows'][R] = { hpx: 20 * maxRowHeight }; // Menggunakan tinggi default 20px
            }
        
            // Mengabaikan isi teks pada elemen dengan class 'fade-in-text-0'
            const fadeElements = document.querySelectorAll('.fade-in-text-0');
            fadeElements.forEach(element => {
                element.textContent = ''; // Mengosongkan isi teks
            });
        
            // Set vertical align center untuk kolom A (indeks kolom = 0)
            if (!ws['!cols'][0]) ws['!cols'][0] = {};
            ws['!cols'][0].vAlign = 'center';
        
            // Set border untuk setiap sel
            const borderStyle = { style: 'thin', color: { rgb: '000000' } };
            for (let R = range.s.r; R <= range.e.r; ++R) {
                for (let C = range.s.c; C <= range.e.c; ++C) {
                    const cell_address = { c: C, r: R };
                    const cell_ref = XLSX.utils.encode_cell(cell_address);
                    const cell = ws[cell_ref];
                    if (!cell) continue;
                    cell.s = borderStyle;
                }
            }
        
            // Write ke file
            XLSX.writeFile(wb, fileName);
        }
        
        
        const handleExportOld = async () => {
            showSwalLoading();

            await sleep(1000);

            const payload = { ...exportData.value };
            
            props.satker && console.log(`[INFO] Exporting data ... Satker ID : ${props.satker.id} - Level : ${props.satker.level}`)

            try {
                const response = await axios.post(`/kegiatan/api/v1/dayatif/${props.url}/export/`, payload);
                const data = response.data;

                 Swal.close(); return;
                
                window.location.href = data.file_path;

                const confirmation = await Swal.fire({
                    title: "Berhasil",
                    html: `Data <b>${props.name}</b> telah <b>berhasil</b> diekspor! <br>Klik tombol unduh ulang apabila <b>gagal</b>!`,
                    icon: "success",
                    confirmButtonText: "Unduh ulang.",
                    showCancelButton: true,
                    cancelButtonText: 'Batalkan',
                    showCloseButton: true,
                    allowOutsideClick: false,
                });

                if (confirmation.isConfirmed) window.location.href = data.file;
            } catch (error) {
                showSwalGenericError();
                console.error('Terjadi kesalahan:', error);
            }
        }
        
        const handleExport2 = async (waktu) => {
            const data = { satker: { ...props.satker }, ...waktu };
            console.log('Exporting data ...', data);
            console.log(`[INFO] Exporting data ... Satker ID : ${props.satker.id} - Level : ${props.satker.level}`)

            try {

                const response = await axios.post(`/kegiatan/api/v1/dayatif/${props.url}/export/`, data);

                console.log('Response:', response)
            } catch (error) {
                showSwalGenericError();
                console.error('Terjadi kesalahan:', error);
            }
        }

        onMounted(() => {
            $('#export__status_pengiriman').on('change', (e) => exportData.value.status = e.target.value)
            $('#export__rentang_waktu').on('change', (e) => exportData.value.waktu = e.target.value)
        });
        
        return { exportData, handleExport }
        
    },
    template: `
        <button type="button" class="btn btn-success" @click="handleExport"><i class="fas fa-file-export me-2"></i>Ekspor Data</button>
        
        <div class="btn-group dropstart d-none" data-bs-toggle="tooltip" data-bs-placement="top"
            data-bs-custom-class="tooltip-dark"
            data-bs-original-title="Klik disini untuk mengekspor data.">
                <button type="button" class="btn btn-success dropdown-toggle"
                    data-bs-toggle="dropdown" aria-expanded="false" data-bs-offset="10,20"
                    data-bs-auto-close="outside"><i class="fas fa-file-export me-2"></i>Ekspor Data</button>
                <ul class="dropdown-menu w-px-500">
                    <li>
                        <h5 class="dropdown-header text-uppercase">Ekspor Data</h5>
                    </li>
                    <li>
                        <hr class="dropdown-divider">
                    </li>
                    <div class="pt-0 pb-3 px-3" id="export__form">
                        <div class="mb-2">
                            <label for="export__status_pengiriman" class="form-label">Status Pengiriman</label>
                            <select id="export__status_pengiriman" class="form-select select2" required>
                                <option disabled>-- Pilih Status Pengiriman --</option>
                                <option value="semua">-- Semua --</option>
                                <option value="0">Belum Terkirim</option>
                                <option selected value="1">Terkirim</option>
                                <!-- ❌ ✅ -->
                            </select>
                        </div>
                        <div class="mb-2">
                            <label for="export__rentang_waktu" class="form-label">Rentang Waktu</label>
                            <select id="export__rentang_waktu" class="form-select select2" required>
                                <option disabled>-- Pilih Rentang Waktu --</option>
                                <option selected value="semua">-- Semua --</option>
                                <option value="triwulan1">Triwulan 1 (Januari - Maret)</option>
                                <option value="triwulan2">Triwulan 2 (April - Juni)</option>
                                <option value="triwulan2">Triwulan 3 (Juli - September)</option>
                                <option value="triwulan4">Triwulan 4 (Oktober - Desember)</option>
                                <option value="hari_ini">Hari ini</option>
                                <option value="minggu_ini">Minggu ini</option>
                                <option value="bulan_ini">Bulan ini</option>
                            </select>
                        </div>
                    </div>
                    <li>
                        <hr class="dropdown-divider">
                    </li>
                    <div class="list-dropdown-button d-flex justify-content-end px-3 py-2">
                        <button type="button" class="btn btn-label-secondary fw-semibold me-2 px-6">
                            <i class="fas fa-xmark me-2"></i>Batalkan</button>
                        <button type="button" class="btn btn-success fw-semibold px-6" @click="handleExport">
                            <i class="fas fa-save me-2"></i>
                            Ekspor</button>
                    </div>
                </ul>
            </div>

            <!--
                <button class="btn btn-success">
                    <i class="fas fa-file-export me-2"></i>Ekspor Data
                </button>
                <div class="btn-group">
                <button type="button" class="btn btn-success dropdown-toggle" data-bs-toggle="dropdown">Ekspor Data</button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('semua')">Semua Data</a></li>
                        <hr class="dropdown-divider">
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('hari_ini')">Hari Ini</a></li>
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('minggu_ini')">Minggu Ini</a></li>
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('bulan_ini')">Bulan Ini</a></li>
                        <hr class="dropdown-divider">
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('triwulan1')">Triwulan 1 (Januari - Maret)</a></li>
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('triwulan2')">Triwulan 2 (April - Juni)</a></li>
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('triwulan3')">Triwulan 3 (Juli - September)</a></li>
                        <li><a class="dropdown-item" href="javascript:void(0);" @click="handleExport('triwulan4')">Triwulan 4 (Oktober - Desember)</a></li>
                    </ul>
                </div>
            !-->
    `
}

const PageActionBTN = {
    name: 'PageActionBTN',
    delimiters,
    props: ['satker'],
    components: { 'v-export-button': ExportBTN },
    emits: ['reload'],
    template: `
        <div id="action__btn_container" class="d-flex gap-2">
            <button class="btn btn-outline-primary" @click="$emit('reload')">
                <i class="fas fa-refresh me-2"></i>Reload data
            </button>
            
            <v-export-button name="Pemetaan Potensi" url="pemetaan_potensi" :satker="{ id: satker.id, level: satker.level }"></v-export-button>
            <b></b>

            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createModal">
                <i class="fas fa-plus me-2"></i>Tambah Data
            </button>
        </div>
    `
}

const Lokasi = {
    name: 'Lokasi',
    props: {
        provinsi: { type: String, required: true },
        kabupaten: { type: String, required: true },
        kecamatan: { type: String, required: true },
        desa: { type: String, required: true },
    },
    delimiters,
    setup(props) {
        const locationData = computed(() => {
            return {
                'Provinsi': props.provinsi,
                'Kabupaten/Kota': props.kabupaten,
                'Kecamatan': props.kecamatan,
                'Desa/Kelurahan': props.desa
            };
        });

        return { locationData };
    },
    template: `
        <ul class="location__list">
            <li v-for="(value, label) in locationData" :key="label">
                <span class="location__label">{{ label }}</span>:
                <span class="location__value">{{ value }}</span>
            </li>
        </ul>
    `
};

const DaftarStakeholder = {
    name: 'DaftarStakeholder',
    delimiters,
    props: ['data'],
    template: `
        <div :class="!data && 'text-center'">
            <ol v-if="data" class="location__list">
                <li v-for="(item, index) in data" :key="index">
                    <span class="location__value">{{ item.nama }}</span>
                </li>
            </ol>
            <span v-else class="text-muted">-</span>
        </div>
    `
};

const DaftarPeserta = {
    name: 'DaftarPeserta',
    delimiters,
    props: ['id', 'data', 'satker'],
    emits: ['detail'],
    setup(props) {
        const showModal = () => $(`#detailPesertaModal_${props.id}`).modal('show');

        const tooMany = computed(() => props.data.length > 3);
        const filteredData = computed(() => {
            if (tooMany.value) {
                return props.data.slice(0, 3)
            } else {
                return props.data;
            }
        });

        return { filteredData, tooMany, showModal };
    },
    template: `
        <div :class="!data && 'text-center'">
            <div v-if="data">
                <ol class="mb-3">
                    <li v-for="(item, index) in filteredData" :key="index">
                        <span class="pe-2">{{ item.nama }}</span>
                        <span class="fw-bold">{{ item.status }}</span>
                    </li>
                </ol>
                <div v-if="tooMany" class="text-muted text-center mb-2">.......</div>
                <a href="javascript:void(0)" @click="showModal">Lihat selengkapnya</a>

                <div class="modal fade" :id="'detailPesertaModal_' + id">
                    <div class="modal-dialog modal-xl modal-dialog-scrollable" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Detail Daftar Peserta untuk Pelaksanaan dari Satuan Kerja <strong>{{ satker }}</strong>
                                </h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="table-responsive">
                                    <table class="table table-sm table-bordered">
                                        <thead>
                                            <tr>
                                                <th class="bg-soft-primary text-center">No.</th>
                                                <th class="bg-soft-primary">Nama</th>
                                                <th class="bg-soft-primary">Alamat</th>
                                                <th class="bg-soft-primary">No HP</th>
                                                <th class="bg-soft-primary">Jenis Kelamin</th>
                                                <th class="bg-soft-primary">Status Kemiskinan</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(peserta, index) in data">
                                                <td>{{ ++index }}</td>
                                                <td>{{ peserta.nama }}</td>
                                                <td>{{ peserta.alamat }}</td>
                                                <td>{{ peserta.notelp }}</td>
                                                <td>{{ peserta.jenis_kelamin == 'L' ? 'Laki-Laki' : 'Perempuan' }}</td>
                                                <td>{{ peserta.status }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-label-secondary" data-bs-dismiss="modal">
                                    <i class="fas fa-xmark me-2"></i>
                                    Tutup
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <span v-else class="text-muted">-</span>
        </div>
    `
};

const ResultNotFound = {
    name: 'ResultNotFound',
    delimiters,
    props: {
        colspan: { type: String, required: true },
        text: {
            type: String,
            required: false,
            default: 'Data yang anda cari tidak ditemukan',
        },
    },
    template: `
        <tr class="bg-soft-light">
            <td :colspan="colspan">
                <h3 class="my-3 text-capitalize">
                    {{ text }}
                </h3>
            </td>
        </tr>
    `
};

const HeaderAction = {
    name: 'HeaderAction',
    delimiters,
    props: {
        rowspan: { type: Number, required: false, default: 1 },
        width: { type: Number, required: false, default: 150 },
        bgColor: { type: String, required: false, default: 'bg-soft-success' },
    },
    template: `
    <th class="text-center" :class="bgColor" :rowspan :style="{ maxWidth: width + 'px' }">
        Aksi <i class="fas fa-edit ms-2"></i>
    </th>`
};

const ItemHeader = {
    name: 'ItemHeader',
    props: ['nama', 'length', 'fade', 'index'],
    props: {
        nama: { type: String, required: true },
        length: { type: Number, required: true },
        fade: { type: Boolean, default: false },
        index: { type: String, required: false, default: '0' },
    },
    delimiters,
    setup(props) {
        const lengthText = computed(() => `(${props.length} kegiatan)`);
        const index = computed(() => props.index.split('.')[1]);
        const indexNumber = computed(() => `<br>(<span class="${index.value == props.length ? 'text-success' : 'text-primary'}">${index.value}</span>/${props.length} kegiatan)`)
        return { lengthText, indexNumber };
    },
    template: `
        <div :class="fade && 'fade-in-text-0 cursor-pointer'">
            <b class="me-2">{{ nama }}</b> <span>{{ lengthText }}</span>
            <span v-html="fade ? indexNumber : lengthText"></span>
        </div>
    `
};

const ItemText = {
    name: 'ItemText',
    delimiters,
    props: {
        text: { type: String, required: true },
        length: { type: Number, required: false, default: 30 },
        hoverable: { type: Boolean, required: false, default: true }
    },
    setup(props) {
        const isExpanded = ref(false);
        const tooFew = ref(false);

        const truncatedText = computed(() => {
            if (props.text.length <= props.length) {
                tooFew.value = true;
                return props.text;
            } else {
                return props.text.slice(0, props.length) + '...';
            }
        });

        const handleMouse = (type) => {
            if (type == 'enter') {
                if (props.hoverable) isExpanded.value = true;
            } else {
                if (props.hoverable) isExpanded.value = false;
            }
        }

        return { truncatedText, isExpanded, tooFew, handleMouse };
    },
    template: `
        <div>
            <span v-text="text"></span>
        </div>
    `
};

/*
<span v-if="isExpanded" v-text="text"></span>
            <span v-else v-text="truncatedText"></span>
            <br v-if="isExpanded">
            <template v-if="!tooFew">
                <a href="javascript:void(0);" class="mt-1" @click="isExpanded = !isExpanded" v-text="isExpanded ? 'Show less' : 'Show more'"></a>
            </template>
*/

const ItemTanggal = {
    name: 'ItemTanggal',
    props: {
        awal: { type: String, required: true },
        akhir: { type: String, required: false }
    },
    delimiters,
    setup(props) {
        const formattedDate = computed(() => getTanggalKegiatan(props.awal, props.akhir))

        const differenceDays = computed(() => {
            if (props.akhir) {
                const startDate = moment(props.awal);
                const endDate = moment(props.akhir);
                const result = endDate.diff(startDate, 'days');
                return `${result < 0 ? 0 : result} hari`;
            } else {
                return '1 hari';
            }
        });


        return { formattedDate, differenceDays }
    },
    template: `
        <div>
            <div v-text="formattedDate"></div>
        </div>
    `
};
// <div class="fade-in-text-0 cursor-pointer text-muted mt-3" v-text="differenceDays"></div>

const ItemDokumentasi = {
    name: 'ItemDokumentasi',
    props: {
        id: { type: Number, required: true },
        file: { type: String, required: true },
        image: { type: String, required: false, default: null },
        information: { type: Object, required: true },
        text: { type: String, required: false, default: 'Lihat dokumentasi' },
    },
    delimiters,
    template: `
        <div class="text-center">
            <a v-if="!image" :href="file" class="badge bg-primary text-white cursor-pointer">
                <i class="fas fa-eye me-2"></i>
                <span v-text="text"></span>
            </a>
            <a v-else href="javascript:;" class="badge bg-primary text-white cursor-pointer" @click="showModal">
                <i class="fas fa-eye me-2"></i>
                <span v-text="text"></span>
            </a>
        </div>

        <div class="modal fade" :id="'detailDokumenModal_' + id">
            <div class="modal-dialog modal-xl modal-dialog-scrollable" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Detail Dokumentasi Kegiatan dari Satuan Kerja <strong>{{ information.satker }}</strong></h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row justify-content-between">
                            <div class="col-md-6">
                                <h4>Unduh dokumentasi file berikut :</h4>
                                <div class="mt-2">
                                    <div class="text-muted fw-bold">Kegiatan {{ information.satker }}</div>
                                    <div class="text-muted">Waktu : {{ information.tanggal }}</div>
                                </div>
                            </div>
                            <div class="col-md-6 d-flex justify-content-end align-items-center">
                                <div>
                                    <a :href="file ? file : 'javascript:;'" class="btn text-uppercase" :class="file ? 'btn-success' : 'btn-secondary'">
                                        <i class="fas fa-download me-2"></i>Unduh File
                                    </a>
                                </div>
                            </div>
                        </div>
                
                        <hr class="my-3">

                        <div class="d-flex">
                            <div class="position-relative w-100 p-3 bg-soft-gray">
                                <img :src="image" alt="Detail Image" class="img-fluid p-0" style="height: 400px; width: -webkit-fill-available; object-fit: contain;">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-label-secondary" data-bs-dismiss="modal">
                            <i class="fas fa-xmark me-2"></i>
                            Tutup
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `,
    methods: {
        showModal() {
            $(`#detailDokumenModal_${this.id}`).modal('show');
        }
    }
};


const InputImage = {
    name: 'InputImage',
    props: {
        id: { type: String, required: true },
        init: { type: String, required: false },
        maxsize: { type: Number, default: 5 },
        text: { type: String, required: false, default: 'Lihat dokumentasi' },
        label: {
            type: String,
            default: 'Tarik gambar anda kesini atau klik untuk mengupload file'
        }
    },
    delimiters,
    emits: ['update:modelValue'],
    setup(props, { emit }) {
        const selectedFile = ref(null);
        const fileSize = ref(null);
        const fileName = ref(null);
        const previewUrl = ref(null);
        const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'];

        const getFileSizeFormatted = (size) => {
            console.log('Ukuran :', size);
            if (!size) return 0;

            if (size < 1024) {
                return size.toFixed(2) + ' B';
            } else if (size < 1024 * 1024) {
                return (size / 1024).toFixed(2) + ' KB';
            } else {
                return (size / (1024 * 1024)).toFixed(2) + ' MB';
            }
        };
        
        const getError = (type, info) => {
            if (type == 'size') {
                return showSwalError('Terjadi Kesalahan', `Ukuran file yang anda upload <b>${info}MB</b> terlalu besar.<br>Yang diizinkan maksimal hanya <b>${props.maxsize}MB</b>`);
            } else if (type == 'mimes') {
                return showSwalError('Terjadi Kesalahan', `Format file yang anda upload <b>${info}</b> tidak valid.<br>Yang diizinkan hanya <b>JPEG, JPG, dan PNG</b>`);
            }
        };

        const getFileDetailsFromUrl = async (url) => {
            console.log(url);
            if (url == '-') return;

            try {
                const response = await axios.get(url, {
                    responseType: 'blob',
                });
                const blob = response.data;
                const file = new File([blob], fileName.value, { type: blob.type });
                selectedFile.value = file;
                const size = file.size;
                fileSize.value = getFileSizeFormatted(size);
            } catch (error) {
                console.error('Error fetching file details:', error);
            }
        };

        const validateFileExtension = (file) => {
            if (!allowedTypes.includes(file.type)) {
                getError('mimes', file.type);
                return false;
            }
            return true;
        };

        const validateFileSize = (file) => {
            const fileSize = getFileSizeFormatted(file.size);
            if (fileSize > props.maxSize) {
                getError('size', fileSize);
                return false;
            }
            return true;
        };

        const validateFile = (file) => {
            return validateFileExtension(file) && validateFileSize(file);
        };

        const onFileChange = (event) => {
            const file = event.target.files[0];

            if (!file) return;

            if (!validateFile(file)) {
                event.target.value = null;
                return;
            }

            selectedFile.value = file;
            fileName.value = file.name;
            fileSize.value = getFileSizeFormatted(file.size);
            emit("update:modelValue", file);
            createPreview(file);
        };

        const onDrop = (event) => {
            event.preventDefault();
            const file = event.dataTransfer.files[0];
            if (!file) return;

            if (!validateFile(file)) {
                event.target.value = null;
                return;
            }

            selectedFile.value = file;
            fileName.value = file.name;
            fileSize.value = getFileSizeFormatted(file.size);

            emit("update:modelValue", file);
            createPreview(file);
        };

        const createPreview = (file) => {
            const reader = new FileReader();
            reader.onload = (e) => {
                previewUrl.value = e.target.result;
            };
            reader.readAsDataURL(file);
        };

        const clearInput = async () => {

            if (props.init) {
                const confirmation = await showSwalConfirm('Apakah anda yakin untuk menghapus file?', 'Ya, saya yakin');

                if (!confirmation.isConfirmed) return
                
                selectedFile.value = null;
                emit("update:modelValue", null);
                previewUrl.value = null;
            } else {
                selectedFile.value = null;
                emit("update:modelValue", null);
                previewUrl.value = null;
            }

        };

        watch(selectedFile, (newValue) => {
            if (!newValue) {
                previewUrl.value = null;
            }
        });

        watch(() => props.init, async (newValue) => {
            previewUrl.value = newValue;
            if (newValue) {
                fileName.value = newValue.substring(newValue.lastIndexOf('/') + 1);
                await getFileDetailsFromUrl(newValue);
            } else {
                selectedFile.value = null;
                fileName.value = null;
                fileSize.value = null;
            }
        });

        return {
            selectedFile,
            previewUrl,
            onFileChange,
            onDrop,
            clearInput,
            allowedTypes,
            fileName,
            fileSize,
        };
    },
    template: `
    <div>
        <div
            class="dropzone"
            @dragover.prevent
            @dragenter.prevent
            @drop="onDrop"
        >
            <label :for="'upload_'+id" class="cursor-pointer">
                <input
                    class="input-image"
                    :id="'upload_'+id"
                    type="file"
                    ref="fileInput"
                    hidden
                    @change="onFileChange"
                    :accept="allowedTypes.join(', ')"
                >
            <p v-if="!previewUrl">{{ label }} <i class="fas fa-arrow-up-from-bracket ms-2"></i></p>
            <p v-else class="text-primary">Upload ulang untuk mengganti file <i class="fas fa-arrow-up-from-bracket ms-2"></i></p>
            </label>
        </div>
        <transition>
            <div v-if="previewUrl"  style="
                border: 1px dashed #d6d6d6;
                border-top: 0;
                padding: 20px !important;
            ">
                <div class="position-relative p-3" style="background-color: #f0f0f0">
                    <img :src="previewUrl" alt="Preview" class="img-fluid p-0" style="height: 300px; width: -webkit-fill-available; object-fit: contain;">
                    <div class="text-muted text-center mt-4">{{ fileName }} - <b>{{ fileSize }}</b></div>
                    <button @click="clearInput" type="button" class="text-danger border-0 bg-transparent" style="position: absolute; right: 30px; top: 20px; font-size: 25pt;"><i class="text-danger fas fa-xmark"></i></button>
                </div>
            </div>
        </transition>
    </div>
    `
};
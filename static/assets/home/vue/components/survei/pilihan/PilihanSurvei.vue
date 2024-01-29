<template>
    <div :class="'card level-' + bobot">
        <div class="card-body">
            <h4 class="card-title" :id="'option' + bobot">{{ getTitle }}</h4>
            <img :src="src" :alt="getTitle">
        </div>
    </div>
</template>
<script>
export default {
    name: 'Pilihan Survei',
    props: {
        bobot: {
            type: String,
            required: true,
            validator: (value) => ["1", "2", "3", "4"].includes(value)
        },
        src: {
            type: String,
            required: true
        }
    },
    methods: {
        jawabSurvei() {
            jawab(this.bobot);
        },
    },
    computed: {
        getTitle() {
            const mapTitle = {
                "1": "Sangat Tidak Setuju",
                "2": "Tidak Setuju",
                "3": "Setuju",
                "4": "Sangat Setuju"
            };
            return mapTitle[this.bobot] || "0";
        }
    }
};
</script>
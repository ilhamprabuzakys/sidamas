<template>
    <div class="row">
        <div class="col-4 d-flex">
            <input class="form-check-input" type="radio" :name="radioName" :id="'rentang_usia-' + value" :value="value"
                @change="handleRadioChange">
        </div>
        <div class="col-7 d-flex">
            <label class="form-check-label" :for="'rentang_usia-' + value">
                <h4 class="card-title">{{ value + " tahun" }}</h4>
            </label>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Pilihan Rentang Usia',
    props: {
        value: { type: String, required: true },
        buttonId: { type: String, required: true },
    },
    data() {
        return {
            radioName: "rentang_usia",
        };
    },
    methods: {
        handleRadioChange() {
            this.emitter.emit(`${this.buttonId}-usia-changed`, this.value);
        },
    },
};
</script>
<template>
    <section id="survei">
        <slot></slot>
    </section>
</template>
<script>
export default {
    props: ["data"],
    data() {
        return {
            responseData: {}
        };
    },
    computed: {
        getJSONData: function () {
            return JSON.parse(this.data);

        }
    },
    mounted() {
        console.log("data raw:", this.data);
        console.log("data json:", this.getJSONData);

    },
};
</script>
<style lang="">
    
</style>
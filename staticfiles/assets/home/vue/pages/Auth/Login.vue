<template>
    <p class="card-text text-center p-2">Masukan nama pengguna anda untuk masuk kedalam aplikasi Sistem Informasi DAYAMAS
    </p>
    <form method="POST" id="__form_login" @submit.prevent="login()">
        <InputGroup label="Nama Pengguna" placeholder="Nama Pengguna Anda" type="text" icon="fas fa-user" name="username"
            v-model="username" required></InputGroup>
        <InputGroup label="Kata Sandi" placeholder="Kata Sandi Anda" type="password" icon="fas fa-lock" name="password"
            v-model="password" required></InputGroup>

        <div class="text-end">
            <span id="forgot-password-text" @click="handleForgotPassword()">Lupa Kata Sandi? Klik <a
                    href="javascript:;">disini</a></span>
        </div>

        <Button type="submit" icon="fa-solid fa-arrow-right-to-bracket">Masuk</Button>
    </form>
</template>
<script setup>
import Button from "../../components/forms/Button.vue";
import InputGroup from "../../components/forms/InputGroup.vue";
import { ref } from 'vue';

const username = ref('');
const password = ref('');

</script>
<script>
export default {
    methods: {
        login() {
            let trimmedUsername = username.value.trim();
            let trimmedPassword = password.value.trim();

            Swal.fire({
                title: "Mengecek data",
                icon: "info",
                html: `Mengecek <b>data kredensials</b> yang anda masukan ...`,
                didOpen: () => {
                    Swal.showLoading();
                },
            }).then((result) => {
                if (result.dismiss === Swal.DismissReason.timer) {
                }
            });

            fetch(window.location.origin + "/accounts/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": document.querySelector(
                        'meta[name="csrf-token"]'
                    ).content,
                },
                body: new URLSearchParams({
                    username: trimmedUsername,
                    password: trimmedPassword,
                }),
            })
                .then((data) => {
                    if (data.redirected) {
                        // Jika login berhasil, redirect ke halaman yang ditentukan
                        Swal.fire({
                            title: "Berhasil",
                            html: `Anda <strong>berhasil</strong> login, akan segera dialihkan.`,
                            icon: "success",
                            confirmButtonText: "OK",
                            timer: 1000,
                        });
                        setTimeout(() => {
                            window.location.href = "/accounts/pilih-direktorat";
                        }, 1000);
                    } else {
                        Swal.fire({
                            title: "Terjadi kesalahan",
                            html: `Data yang anda masukan <strong>tidak valid</strong> atau <strong>tidak ditemukan</strong>!`,
                            icon: "error",
                            confirmButtonText: "OK",
                        });

                        usernameEl.value = "";
                        passwordEl.value = "";
                    }
                })
                .catch((error) => {
                    // console.error("Error:", error);
                    Swal.fire({
                        title: "Terjadi kesalahan",
                        html: `Data yang anda masukan <strong>tidak valid</strong> atau <strong>tidak ditemukan</strong>!`,
                        icon: "error",
                        confirmButtonText: "OK",
                    });

                    usernameEl.value = "";
                    passwordEl.value = "";
                });
        },
        handleForgotPassword() {
            Swal.fire({
                title: "Lupa password anda?",
                html: `Kontak <strong>puslitdatin</strong> untuk mendapatkan <strong>password</strong> anda kembali!`,
                icon: "info",
                confirmButtonText: "Hubungi Puslitdatin.",
                showCancelButton: true,
                cancelButtonText: "Batalkan"
            }).then((result) => {
                if (result.isConfirmed) {
                    // Send to puslitdatin help desk
                    window.location.href = "https://puslitdatin.bnn.go.id/kontak/#fws_65a72cdccd7ed";
                }
            });

            return;
        }
    }
};
</script>
<style lang="">
    
</style>
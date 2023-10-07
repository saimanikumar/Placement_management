<template>
    <div>
        <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand brand-font" href="#">&nbsp;Placement Connect</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-4 mb-lg-0 ">

                        <li class="nav-item">
                            <a @click="" class="btn btn-outline-dark rounded-5 border-0"><i class="fa-solid fa-bell"></i></a>
                            <span class="position-absolute top-25 badge rounded-pill bg-danger translate-middle ">2</span>
                        </li>
                        <li class="nav-item">
                            <a @click="" class="btn btn-outline-dark rounded-5 border-0"><i
                                    class="fa-solid fa-chart-line"></i> Summary</a>
                        </li>

                        <li class="nav-item">
                            <a @click="nav_logout" class="btn btn-outline-dark rounded-5 border-0"><i
                                    class="fa-solid fa-right-to-bracket"></i> Log Out</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>
  


<script>
  import axios from "../../axios.js";

export default {
    methods: {
        dept_details() {
            this.$router.push('/dept_details')
        },
        nav_logout() {
            this.$store.dispatch('logoutUser')
        },
    },
}
//     nav_home() {
//       if (localStorage.getItem('token')) {
//         if (this.$store.state.role == 'admin') {
//           this.$router.push({ name: 'admin_board' })
//         } else {
//           this.$router.push({ name: 'user_board' })
//         }
//       }
//       else {
//         this.$router.push({ name: 'home' })
//       }

//     },
//     entrylogin() {
//       this.$router.push({ name: 'login' })
//     },
//     entryregister() {
//       this.$router.push({ name: 'register' })
//     },
//     nav_summary() {
//       this.$router.push({ name: 'summary' })
//     },
//     nav_bookings() {
//       this.$router.push({ name: 'bookings' })
//     },
//     nav_logout() {
//       this.$store.dispatch('logoutUser')
//     },

//   },
// }
</script>


<style lang="">
</style>
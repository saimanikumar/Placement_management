
<template>
    <div>
        <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand brand-font" href="#">Placement Connect</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0 ">

                        <li class="nav-item">
                            <a class="btn btn-outline-dark rounded-5 border-0" @click="details"><i class="fa-solid fa-table"></i> Details</a>
                        </li>

                        <li class="nav-item">
                            <a class="btn btn-outline-dark rounded-5 border-0" @click="adsum"><i class="fa-solid fa-chart-line"></i>
                                Summary</a>
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
export default {
    methods: {
        details() {
            this.$router.push('/admindetails')
        },
        nav_logout() {
            this.$store.dispatch('logoutUser')
        },
        adsum(){
            this.$router.push('/adsum')
        }
    },
}
</script>
  
  
<style lang="">
  </style>
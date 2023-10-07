<template>
    <Navbar/>
    <div class="body1 row" style="padding-top: 80px;">
        <h2>Welcome to Placement Connect</h2>
        <div class="container-fluid text-center my-4 list-column col-lg-3 col-md-4">

            <div class="container-fluid rounded-4" id="cont1">

                <div class="card border-0 shadow rounded-4" style="width: 18rem;" id="">
                    <img src="../../public/130-man-student-2.svg" class="card-img-top w-100 h-25" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Student</h5>
                        <a href="#" class="btn btn-dark border-0 rounded-5 w-50" @click="stulogin">Login</a>
                    </div>
                </div>

            </div>
        </div>

        <div class="container-fluid text-center my-4 list-column col-lg-3 col-md-4">
            <div class="container-fluid rounded-4" id="cont1">

                <div class="card border-0 shadow rounded-4" style="width: 18rem;" id="">
                    <img src="../../public/coordinator.svg" class="card-img-top w-100 h-25" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Admin</h5>
                        <a href="#" class="btn btn-dark border-0 rounded-5 w-50" @click="admlogin">Login</a>
                    </div>
                </div>

            </div>
        </div>

        <div class="container-fluid text-center my-4 list-column col-lg-3 col-md-4">
            <div class="container-fluid rounded-4" id="cont1">

                <div class="card border-0 shadow rounded-4" style="width: 18rem;" id="">
                    <img src="../../public/Admin.svg" class="card-img-top w-100 h-25" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Department Coordinator</h5>
                        <a href="#" class="btn btn-dark border-0 rounded-5 w-50" @click="deptlogin">Login</a>
                    </div>
                </div>

            </div>
        </div>


    </div>
</template>

<script>
import Navbar from "../components/Navbar.vue"
export default {
    methods: {
        stulogin() {
            this.$router.push('/stulogin')
        },
        admlogin() {
            this.$router.push('/admlogin')
        },
        deptlogin(){
            this.$router.push('/deptlogin')
        }
    },

    components: {
        Navbar,
    },

}
</script>

<style>
.body1 {
    height: 100vh;
    background-image: url("../../public/wave.svg");
    background-repeat: no-repeat;
    background-position: bottom;

}
</style>
<template>

<!-- <error-popup :error-message="errorPopupMessage" @close="closeErrorPopup"></error-popup> -->

    <div class="mask d-flex align-items-center h-100 gradient-custom-3" style="margin-top: 60px;">
        <div class="container h-75">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                    <div class="card p-4 rounded-3 shadow-lg">
                        <div class="card-body">
                            <h2 class="text-center mb-4">Add Details</h2>
                            <form>
                                <div class="mb-3">
                                    <label for="rollNumber" class="form-label">Roll Number</label>
                                    <input type="text" id="rollNumber" class="form-control" v-model="add_details.student_id"
                                        required />

                                </div>

                                <div class="mb-3">
                                    <label for="deptID" class="form-label">Dept Id</label>
                                    <input type="text" id="deptID" class="form-control" v-model="add_details.department_id"
                                        required />
                                </div>

                                <div class="mb-3">
                                    <label for="companyName" class="form-label">Company Name</label>
                                    <input type="text" id="companyName" class="form-control"
                                        v-model="add_details.company_name" required />
                                </div>
                                <div class="mb-3">
                                    <label for="package" class="form-label">Package</label>
                                    <input type="text" id="package" class="form-control" v-model="add_details.package"
                                        required />
                                </div>
                                <div class="mb-3">
                                    <label for="passOutYear" class="form-label">Passed out year</label>
                                    <input type="text" id="passOutYear" class="form-control" v-model="add_details.year"
                                        required />
                                </div>
                                <div class="text-center">
                                    <button type="button" class="btn btn-success rounded-pill px-5" @click="submit">
                                        Submit
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from "../../axios.js";

import ErrorPopup from '../../components/ErrorPopUp.vue';

export default {

    data() {
        return {
            add_details: {
                id: null,
                student_id: null,
                department_id: null,
                company_name: null,
                package: null,
                year: null,
            },

            // theatre_lists: null,
            errorPopupMessage: ''

        }
    },
    // components: {
    //     // Show,
    //     'error-popup': ErrorPopup,
    // },
    methods: {

        async submit() {
            // if (this.$route.params.id) {
            //     var baseUrl = `/api/details_register?id=${this.$route.params.id}`;
            // } else {
            console.log(this.add_details)
            var baseUrl = '/api/details_register';
            // }

            await axios({
                // method: this.$route.params.id ? 'PUT' : 'POST',
                method: 'POST',
                url: baseUrl,
                data: this.add_details,
            })
                .then(() => {
                    // alert('data successfully Inserted')
                    this.$router.push({ name: 'admin_board' })
                })
                // .catch((err) => {
                //     const errorMessage = err.response?.data?.error_message || err.message;
                    
                //     this.showErrorPopup(errorMessage);
                // })
            this.$router.push('/adminboard');
        }
    }
};
</script>
  
<style scoped>
/* Add custom CSS styles here if needed */
</style>
  
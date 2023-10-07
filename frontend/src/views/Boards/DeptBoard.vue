<template>
    <DeptNav />

    <div class="container mt-5">
        <h2 class="mb-4" style="margin-top: 70px;">Placement Details</h2>
        <table class="table table-striped table-bordered fs-5">
            <thead>
                <tr>
                    <th scope="col">Roll Number</th>
                    <th scope="col">Company Name</th>
                    <th scope="col">Package</th>
                    <th scope="col">Year</th>
                    <th scope="col">Edit</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="detail in details" :key="detail.student_id">
                    <td>{{ detail.student_id }}</td>
                    <td>{{ detail.company_name }}</td>
                    <td>{{ detail.package }}</td>
                    <td>{{ detail.year }}</td>
                    <td>
                        <button class="btn btn-primary btn-sm" @click="review">Review</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
import DeptNav from "./DeptNav.vue";
import axios from "../../axios.js";

export default {
    data() {
        return {
            details: null,
            searchQuery: "",
        };

    },
    methods: {

        review() {
            this.$router.push('/review')
        },
        async initBoard() {
            this.details = null;
            var detailsTemp = null;

            await axios
                .get(`/api/dept_details/${this.$route.params.id}`)
                .then((res) => {
                    detailsTemp = res.data;
                })
                .catch((err) => {
                    console.log(err);
                });

            this.details = detailsTemp;
        },

        editDetail(detail) {
            // Handle the edit action for a placement detail
            // You can navigate to an edit page or implement the edit logic here
        },

    },

    components: {
        DeptNav,
    },




    async mounted() {
        await this.initBoard();
    },

}
</script>
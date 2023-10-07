<template>
    <AdminNav />

    <div style="margin-top: 250px;" class="container-lg container-md container-sm w-50 rounded-4 shadow">
        <div class="container-lg  container-md  container-sm p-5">
            <h2 class="fw-bold h2">Add the Placement Details Here!</h2>
            <h1><i class="fa-solid fa-hand-point-down"></i></h1>
            <button @click="add_details" class="btn btn-success rounded-5 fs-5"><i class="fa-solid fa-plus"></i></button>
        </div>
    </div>
</template>
  
<script>
// import axios from "../axios.js";
import AdminNav from "./AdminNav.vue";

export default {
    data() {
        return {
            theatres: null,
            searchQuery: "",
        };
    },

    //     computed: {
    //         filteredTheatres() {
    //             if (!this.theatres) return null; // Handle initial loading
    //             if (!this.searchQuery.trim()) return this.theatres; // No search query, show all theaters

    //             const search = this.searchQuery.trim().toLowerCase();
    //             return this.theatres.filter((theatre) => {
    //                 const locationMatch = theatre.location.toLowerCase().startsWith(search);
    //                 const nameMatch = theatre.name.toLowerCase().startsWith(search);
    //                 const placeMatch = theatre.place.toLowerCase().startsWith(search);
    //                 const showMatch = theatre.shows.some((show) => show.name.toLowerCase().startsWith(search));
    //                 return locationMatch || nameMatch || showMatch || placeMatch;
    //             });
    //         },
    //     },

    components: {
        AdminNav,
    },

    methods: {
        add_details() {
            this.$router.push("/addDetails");
            }
    //         // Method to trigger search when the search query changes
    //         searchTheatres() {

    //         },
    //         formatDate(dateString) {
    //             const date = new Date(dateString);
    //             return date.toLocaleDateString("en-IN");
    //         },
    //         createTheatre() {
    //             this.$router.push({ name: "create_theatre" });
    //         },

    //         updateTheatre(theatre_id) {
    //             this.$router.push({ name: "update_theatre", params: { id: theatre_id } });
    //         },

    //         deleteTheatre(theatre_id) {
    //             const sure = confirm("Are you sure?");
    //             if (sure) {
    //                 axios
    //                     .delete(`/api/theatre?id=${theatre_id}`)
    //                     .then(() => {
    //                         alert("Successfully Deleted");
    //                         this.init_board();
    //                         this.$router.push({ name: "board" });
    //                     })
    //                     .catch((err) => {
    //                         console.log(err.message);
    //                     });
    //             }
    //         },

    //         createShow(theatre_id) {
    //             this.$router.push({ name: "create_show", params: { th_id: theatre_id } });
    //         },

    //         updateShow(ob) {
    //             console.log(ob);
    //             this.$router.push({
    //                 name: "update_show",
    //                 params: { th_id: ob.theatre_id, s_id: ob.id },
    //             });
    //         },

    //         async init_board() {
    //             this.theatres = null;
    //             var theatres_temp = null;

    //             await axios
    //                 .get("/api/theatre")
    //                 .then((res) => {
    //                     theatres_temp = res.data;
    //                 })
    //                 .catch((err) => {
    //                     console.log(err);
    //                 });

    //             for (let i in theatres_temp) {
    //                 await axios
    //                     .get(`/api/show?theatre_id=${theatres_temp[i].id}`)
    //                     .then((res) => {
    //                         if (res.data == undefined) {
    //                             theatres_temp[i].shows = [];
    //                         } else {
    //                             theatres_temp[i].shows = res.data;
    //                         }
    //                     })
    //                     .catch((err) => {
    //                         console.log(err);
    //                     });
    //             }

    //             this.theatres = theatres_temp;
    //         },
    //     },

    //     async mounted() {
    //         await this.init_board();
    //         console.log(this.theatres);
        },
};
</script>
  
<style scoped>
</style>
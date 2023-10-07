<template>
    <StuNav></StuNav>
    <div class="container-fluid">
        <div style="padding-top: 70px;text-align: left;">

        </div>
        <!-- <p class="text-center my-5">Placement History</p> -->
        <div class=" row">
            <div v-for="offer in offers" class="card border-0 shadow rounded-4 col-6 m-5" style="width: 18rem;" id="">
                <div  class="card-body text-center">
                    <h2 class="card-title my-4 fw-bolder">{{offer.company_name}}</h2>
                    <h4 class="card-subtitle mb-3">{{offer.package}} LPA</h4>
                    <button @click="upload" type="button" class="btn">Upload</button>
                </div>
            </div>

        </div>

    </div>
</template>
  
<script>
import axios from "../../axios.js";
import StuNav from "./StudentNav.vue";

export default {


    data() {
        return {
            offers: null,
            name: this.$route.params.id,
            // Store the selected date here
        };
    },

    // computed: {
    //     filteredTheatres() {
    //         if (!this.theatres) return null; // Handle initial loading
    //         if (!this.searchQuery.trim() && !this.selectedDate) return this.theatres; // No search query and no selected date, show all theaters

    components: {
        StuNav,
    },
    

    //         const search = this.searchQuery.trim().toLowerCase();
    //         return this.theatres.filter((theatre) => {
    //             const locationMatch = theatre.location.toLowerCase().startsWith(search);
    //             const nameMatch = theatre.name.toLowerCase().startsWith(search);
    //             const placeMatch = theatre.place.toLowerCase().startsWith(search);
    //             const showMatch = theatre.shows.some((show) => show.name.toLowerCase().startsWith(search));

    //             const showDate = new Date(this.selectedDate);
    //             showDate.setHours(0, 0, 0, 0); // Set the time to 00:00:00 to ignore time for comparison

    //             const filteredShows = theatre.shows.filter((show) => {
    //                 const showDate = new Date(show.show_date);
    //                 showDate.setHours(0, 0, 0, 0); // Set the time to 00:00:00 to ignore time for comparison

    //                 // Compare showDate with the selected date
    //                 return !this.selectedDate || showDate.getTime() === selectedDate.getTime();
    //             });

    //             return (
    //                 locationMatch || nameMatch || showMatch || placeMatch || filteredShows.length > 0
    //             );
    //         });
    //     },
    // },

    methods: {
        // formatDate(dateString) {
        //     const date = new Date(dateString);
        //     return date.toLocaleDateString("en-IN");
        // },

        // book(theatre_id, show_id) {
        //     this.$router.push({ name: "user_booking", params: { th_id: theatre_id, s_id: show_id } });
        // },

        // showAllShows() {
        //     // Method to clear the date selection and show all shows
        //     this.selectedDate = "";
        // },

        // clearSelectedDate() {
        //     // Method to clear the date selection
        //     this.selectedDate = "";
        // },



        // async fetchShowsForSelectedDate() {
        //     if (!this.selectedDate) {
        //         // If the date is cleared, show all shows
        //         this.init_board();
        //         return;
        //     }

        //     const selectedDate = new Date(this.selectedDate);
        //     selectedDate.setHours(0, 0, 0, 0); // Set the time to 00:00:00 to ignore time for comparison

        //     try {
        //         const filteredTheatres = this.theatres.reduce((result, theatre) => {
        //             const filteredShows = theatre.shows.filter((show) => {
        //                 const showDate = new Date(show.show_date);
        //                 showDate.setHours(0, 0, 0, 0); // Set the time to 00:00:00 to ignore time for comparison
        //                 return showDate.getTime() === selectedDate.getTime();
        //             });

        //             if (filteredShows.length > 0) {
        //                 result.push({ ...theatre, shows: filteredShows });
        //             }

        //             return result;
        //         }, []);

        //         this.filteredTheatres = filteredTheatres;
        //     } catch (error) {
        //         console.error(error);
        //     }
        // },

        // Method to trigger search when the search query changes
        // searchTheatres() {
        //     // Your existing search logic
        // },


        async init_board() {
            this.offers = null;

            var offersTemp = null;

            await axios
                .get(`/api/student_details/${this.$route.params.id}`, {
                    headers: {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
                    },
                },)
                .then((res) => {
                    offersTemp = res.data;
                })
                .catch((err) => {
                    console.log(err);
                });

            this.offers = offersTemp;
            console.log(this.offers)
        },


    },

    mounted() {
        this.init_board();
    },

    // watch: {
    //     selectedDate: "fetchShowsForSelectedDate",
    // },
};
</script>


<style scoped>
.cont {
    height: auto;
    margin-top: 10px;
}
</style>
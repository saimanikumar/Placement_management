<template>
  <DCNav />
  <h2 style="margin-top: 72px;" class="h2 text-lg-center text-md-center text-sm-center fw-bold ">Placement details</h2>

  <table class="table table-responsive-md table-hover fs-4 text-center">
      <thead>
          <tr>
              <th scope="col">Roll Number</th>
              <th scope="col">Company Name</th>
              <th scope="col">Package</th>
              <th scope="col">Passed out year</th>
              <th scope="col">Review</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>Y20CS046</td>
              <td>Google</td>
              <td>12Lpa</td>
              <td>2024</td>
              <td><button class="btn btn-primary btn rounded-5 btn-lg " @click="review">Review</button></td>
          </tr>
      </tbody>
  </table>
</template>
<script>
import DCNav from "../components/DCNav.vue";

export default {
  data() {
      return {
          theatres: null,
          searchQuery: "",
      };

  },
  methods: {
      review() {
          this.$router.push('/review')
      }
  },
  components: {
      DCNav,
  }

}
</script>
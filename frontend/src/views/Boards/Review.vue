<template>
    <div>
      <h2>Upload Image</h2>
      <form @submit.prevent="uploadImage">
        <div>
          <label for="student_id">Student ID:</label>
          <input type="text" id="student_id" v-model="studentId" required />

        <div>
          <label for="image">Image:</label>
          <input type="file" id="image" ref="imageInput" @change="handleImageChange" accept="image/jpeg" required />
        </div>

        <div>
          <button type="submit">Upload</button>
        </div>
        
      </form>
      <div v-if="imageUrl">
        <h3>Uploaded Image</h3>
        <img :src="imageUrl" alt="Uploaded" />
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        studentId: '',
        company: '',
        deptId: '',
        image: null,
        imageUrl: null,
      };
    },
    methods: {
      handleImageChange(event) {
        this.image = event.target.files[0];
      },
      async uploadImage() {
        const formData = new FormData();
        formData.append('student_id', this.studentId);
        formData.append('company', this.company);
        formData.append('dept_id', this.deptId);
        formData.append('image', this.image);
  
        try {
          const response = await axios.post('http://127.0.0.1:8080/api/upload_image', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });
          this.imageUrl = response.data.url;
        } catch (error) {
          console.error('Error uploading image:', error);
        }
      },
    },
  };
  </script>
  
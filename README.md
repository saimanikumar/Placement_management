---
# Placement Connect App

Placement Connect is a web application that connects job seekers with potential employers. The frontend of the application is built using Vue.js, while the backend is powered by Flask. This README provides an overview of the project, installation instructions, and other important information for developers.


Tech Stack Used - Vuejs, Flask, Flask-Restful(API's), MongoDB, Python, Bootstrap(Responsiveness)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development](#development)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js and npm installed for the Vue.js frontend.
- Python and pip installed for the Flask backend.
- MongoDB database (or another database of your choice) set up and configured.
- Git installed for version control.

## Getting Started

To get the Placement Connect app up and running, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/placement-connect.git
   ```

2. Navigate to the project directory:

   ```bash
   cd placement-connect
   ```

### Frontend (Vue.js)

3. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

4. Install dependencies:

   ```bash
   npm install
   ```

5. Start the development server:

   ```bash
   npm run serve
   ```



### Backend (Flask)

6. Navigate to the backend directory:

   ```bash
   cd backend
   ```

7. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

8. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

9. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

10. Set up your database and configure the Flask application. You might need to create a `.env` file with your configuration variables (e.g., database URL, secret key).

11. Run the Flask application:

    ```bash
    python app.py
    ```



## Project Structure

The project structure is as follows:

- `frontend/`: Vue.js frontend code.
- `backend/`: Flask backend code.
- `requirements.txt`: Python dependencies for the backend.



---

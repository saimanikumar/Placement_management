import { createStore } from "vuex";
import axios from "../axios.js";
import router from "../router/index.js";

const store = createStore({
  state() {
    return {
      loggedIn: localStorage.getItem("token") ? true : false,
      role: null,
    };
  },
  getters: {
    token(state) {
      if (state.loggedIn === true) {
        return localStorage.getItem("token");
      } else {
        return null;
      }
    },
    role(state) {
      return state.role;
    },
  },

  mutations: {
    login(state, role) {
      state.loggedIn = true;
      state.role = role;
    },
    logout(state) {
      state.loggedIn = false;
    },
    resetRole(state) {
      state.role = null;
    },
  },

  actions: {
    async loginAdmin({ commit }, user) {
      try {
        const response = await axios.post("api/admin_login", user, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods":"GET,PUT,POST,DELETE,PATCH,OPTIONS"
          },
        });

        const authToken = response.data.access_token;
        const role = response.data.role;

        console.log(authToken, role)

        axios.defaults.headers.common["Authorization"] = "Bearer " + authToken;

        localStorage.setItem("token", authToken);

        commit("login", role);

        if (role == "admin") {
          router.push({ name: "admin_board" });
        } else {
          localStorage.removeItem("token");
          commit("logout");
          commit("resetRole");
          router.push({ name: "adminlogin" });
        }
      } catch (error) {
        throw error;
      }
    },


    async loginDept({ commit }, user) {
      try {
        const response = await axios.post("api/dept_login", user, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods":"GET,PUT,POST,DELETE,PATCH,OPTIONS"
          },
        });

        const authToken = response.data.access_token;
        const role = response.data.role;
        const dept_id = response.data.id;

        console.log(authToken, role)

        axios.defaults.headers.common["Authorization"] = "Bearer " + authToken;

        localStorage.setItem("token", authToken);

        commit("login", role);

        if (role == "dept") {
          router.push({ name: "dept_board" , params: {id:dept_id} });
        } else {
          localStorage.removeItem("token");
          commit("logout");
          commit("resetRole");
          router.push({ name: "deptlogin" });
        }
      } catch (error) {
        throw error;
      }
    },

    async loginStudent({ commit }, user) {
      try {
        const response = await axios.post("api/stu_login", user, {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods":"GET,PUT,POST,DELETE,PATCH,OPTIONS"

          },
        });

        const authToken = response.data.access_token;
        const role = response.data.role;
        const student_id = response.data.id;

        console.log(authToken,role,student_id)

        axios.defaults.headers.common["Authorization"] = "Bearer " + authToken;

        localStorage.setItem("token", authToken);
        commit("login", role);

        if (role == "student") {
          router.push({ name: "student_board" , params: {id:student_id} });

        } else {
          localStorage.removeItem("token");
          commit("logout");
          commit("resetRole");
          // console.log("dddfs");

          router.push({ name: "/" });
        }
      } catch (error) {
        throw error;
      }
    },

    logoutUser({ commit }) {
      localStorage.removeItem("token");
      commit("logout");
      commit("resetRole");
      router.push({ name: "home" });
    },
  },
});

export default store;

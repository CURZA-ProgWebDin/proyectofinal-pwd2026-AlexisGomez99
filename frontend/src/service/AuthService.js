import { instance as axios } from "../plugins/axios";

class AuthService {
    auth_user = null;
    async login(user) {
        await axios
            .post('auth/login', user)
            .then(response => this.auth_user = response.data)
            .catch(error => console.log(error.status));
    }
    async register(new_user) {
        await axios
            .post('auth/register', new_user)
            .then(response => console.log(response.data))
            .catch(error => console.log(error.status));
    }
    async getMe(id) {
        const data = await axios
          .get('auth/me',id)
          .then((response) => response.data)
          .catch((error) => this.errors.push(error.response.data));
        if (this.errors.length === 0) {
          return data;
        }
    }
}

export default AuthService;
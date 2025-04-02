import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export const login = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}token/`, {
      username: username,
      password: password,
    });

    localStorage.setItem('token', response.data.access); // Guardamos el token en el localStorage

    const userResponse = await axios.get(`${API_URL}user/profile/`, {
      headers: {
        Authorization: `Bearer ${response.data.access}`,
      },
    });

    console.log(userResponse.data)
    localStorage.setItem('user', JSON.stringify(userResponse.data))

    return { token: response.data.access, user: userResponse.data }; // Retornamos el token y el usuario
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
}

export const register = async (username, email, telefono, password) => {
  try {
    const response = await axios.post(`${API_URL}register/`, {
      username,
      email,
      telefono,
      password: password,
    });
    return response.data; //Aqui recibimos el token
  } catch (error) {
    console.error('Register error:', error);
    throw error;
  }
}

export const getUser = () => {
  const user = localStorage.getItem('user');
  if (user) {
    return JSON.parse(user);
  }
  return null;
}

export const logout = () => {
  localStorage.removeItem('user');
  localStorage.removeItem('token'); 
}
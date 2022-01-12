import axios from 'axios';
import config from '../config';

const apiClient = axios.create({
  baseURL: config.apiServerUrl,
  timeout: 1000,
  headers: {
    'Content-type': 'application/json',
  },
});

export default apiClient;

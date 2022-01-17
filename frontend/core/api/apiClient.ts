import axios from 'axios';
import config from '../config';

const apiClient = axios.create({
  baseURL: config.apiServerUrl,
  timeout: 5000,
  headers: {
    'Content-type': 'application/json',
  },
});

export { apiClient };

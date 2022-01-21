import { useAuth0 } from '@auth0/auth0-react';
import axios, { AxiosError, AxiosResponse } from 'axios';
import config from '../config';
import { notify } from '../utils';

axios.defaults.baseURL = config.apiServerUrl;
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.timeout = 5000;
axios.defaults.headers.common['Authorization'] = 'Bearer random_token';

const useAxios = () => {
  const { getAccessTokenSilently } = useAuth0();

  axios.interceptors.request.use(async (req) => {
    let token = '';

    try {
      token = await getAccessTokenSilently({
        audience: config.authApiAudience,
      });
    } catch (error) {
      console.log({ error });
      notify('error', error as Error);
    }

    if (req.headers !== undefined) {
      req.headers.Authorization = `Bearer ${token}`;
    }
    return req;
  });

  return {
    get: async <T>(url: string): Promise<AxiosResponse<T, AxiosError>> =>
      axios.get(url),

    post: async <T>(
      url: string,
      data?: unknown
    ): Promise<AxiosResponse<T, AxiosError>> => axios.post(url, data),

    put: async <T>(
      url: string,
      data?: unknown
    ): Promise<AxiosResponse<T, AxiosError>> => axios.put(url, data),

    remove: async <T>(url: string): Promise<AxiosResponse<T, AxiosError>> =>
      axios.delete(url),
  };
};

export default useAxios;

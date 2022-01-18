import { useAuth0 } from '@auth0/auth0-react';
import axios, { AxiosError, AxiosResponse } from 'axios';
import config from '../config';

axios.defaults.baseURL = config.apiServerUrl;
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.timeout = 5000;
axios.defaults.headers.common['Authorization'] = 'Bearer random_token';

const useAxios = () => {
  const { getAccessTokenSilently, loginWithRedirect, getAccessTokenWithPopup } =
    useAuth0();

  //   axios.interceptors.request.use(async () => {
  //     if (typeof axios.defaults.headers.common['Authorization'] === 'undefined') {
  //       let token: string;
  //       try {
  //         token = await getAccessTokenSilently({
  //           audience: config.authApiAudience,
  //         });
  //       } catch (error) {
  //         console.log({ 'axios error': error });
  //         if (error.error === 'login_required') {
  //           token = await getAccessTokenWithPopup({
  //             audience: config.authApiAudience,
  //           });
  //         }
  //       }
  //       console.log({ token });
  //
  //       axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  //     }
  //   });

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

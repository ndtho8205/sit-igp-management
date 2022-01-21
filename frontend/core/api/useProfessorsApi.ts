import { Professor } from '../types/professor';
import useAxios from './useAxios';

const useProfessorsApi = () => {
  const { get, post, put, remove } = useAxios();
  const endpoint = '/professors';

  return {
    whoami: async () => {
      const response = await get<Professor>(`/whoami`);
      return response.data;
    },

    createProfessor: async (obj: Professor) => {
      const response = await post<Professor>(`${endpoint}/`, obj);
      return response.data;
    },

    findAllProfessors: async () => {
      const response = await get<Professor[]>(`${endpoint}/`);
      return response.data;
    },

    updateProfessor: async (id: string, obj: Professor) => {
      const response = await put<Professor>(`${endpoint}/${id}`, obj);
      return response.data;
    },

    deleteProfessor: async (id: string) => {
      await remove<Professor>(`${endpoint}/${id}`);
    },
  };
};

export default useProfessorsApi;

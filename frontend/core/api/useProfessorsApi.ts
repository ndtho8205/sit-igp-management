import Professor from '../types/professor';
import useAxios from './useAxios';

const useProfessorsApi = () => {
  const { get, post, put, remove } = useAxios();
  return {
    createProfessor: async (obj: Professor) => {
      const response = await post<Professor>('/professors/', obj);
      return response.data;
    },

    findAllProfessors: async () => {
      const response = await get<Professor[]>('/professors/');
      return response.data;
    },

    findProfessorByID: async (id: string) => {
      const response = await get<Professor>(`/professors/${id}`);
      return response.data;
    },

    updateProfessor: async (id: string, obj: Professor) => {
      const response = await put<Professor>(`/professors/${id}`, obj);
      return response.data;
    },

    deleteProfessor: async (id: string) => {
      await remove<Professor>(`/professors/${id}`);
    },
  };
};

export default useProfessorsApi;

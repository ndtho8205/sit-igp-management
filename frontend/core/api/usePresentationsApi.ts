import moment from 'moment';
import Presentation from '../types/presentation';
import useAxios from './useAxios';

const usePresentationsApi = () => {
  const { get, post, put, remove } = useAxios();
  return {
    createPresentation: async (obj: Presentation) => {
      obj.presentation_date = moment(obj.presentation_date).format(
        'YYYY-MM-DD'
      );
      const response = await post<Presentation>('/presentations/', obj);
      return response.data;
    },

    findAllPresentations: async () => {
      const response = await get<Presentation[]>('/presentations/');
      return response.data;
    },

    findPresentationById: async (id: string) => {
      const response = await get<Presentation>(`/presentations/${id}`);
      return response.data;
    },

    updatePresentation: async (id: string, obj: Presentation) => {
      const response = await put<Presentation>(`/presentations/${id}`, obj);
      return response.data;
    },

    deletePresentation: async (id: string) => {
      await remove<Presentation>(`/presentations/${id}`);
    },
  };
};

export default usePresentationsApi;

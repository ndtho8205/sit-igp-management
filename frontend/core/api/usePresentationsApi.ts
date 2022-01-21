import moment from 'moment';
import { Presentation, PresentationEvaluation } from '../types/presentation';
import useAxios from './useAxios';

const usePresentationsApi = () => {
  const { get, post, put, remove } = useAxios();
  const endpoint = '/presentations';

  return {
    createPresentation: async (obj: Presentation) => {
      obj.presentation_date = moment(obj.presentation_date).format(
        'YYYY-MM-DD'
      );
      const response = await post<Presentation>(`${endpoint}/`, obj);
      return response.data;
    },

    findAllPresentations: async (reviewer_id = '') => {
      const path =
        reviewer_id != ''
          ? `${endpoint}/?reviewer_id=${reviewer_id}`
          : `${endpoint}/`;
      const response = await get<Presentation[]>(path);
      return response.data;
    },

    findPresentationById: async (id: string) => {
      const response = await get<Presentation>(`${endpoint}/${id}`);
      return response.data;
    },

    updatePresentation: async (id: string, obj: Presentation) => {
      const response = await put<Presentation>(`${endpoint}/${id}`, obj);
      return response.data;
    },

    deletePresentation: async (id: string) => {
      await remove<Presentation>(`${endpoint}/${id}`);
    },

    createPresentationEvaluation: async (
      presentation_id: string,
      reviewer_id: string,
      obj: PresentationEvaluation
    ) => {
      const response = await post<PresentationEvaluation>(
        `${endpoint}/${presentation_id}/evaluations/${reviewer_id}`,
        { presentation_id, reviewer_id, ...obj }
      );
      console.log(response.data);
      return response.data;
    },

    updatePresentationEvaluation: async (
      presentation_id: string,
      reviewer_id: string,
      obj: PresentationEvaluation
    ) => {
      const response = await put<PresentationEvaluation>(
        `${endpoint}/${presentation_id}/evaluations/${reviewer_id}`,
        { presentation_id, reviewer_id, ...obj }
      );
      console.log(response.data);
      return response.data;
    },
  };
};

export default usePresentationsApi;

import PresentationEvaluation from '../types/presentationEvaluation';
import useAxios from './useAxios';

const usePresentationEvaluationsApi = () => {
  const { get, post, put, remove } = useAxios();
  return {
    createEvaluation: async (obj: PresentationEvaluation) => {
      const response = await post<PresentationEvaluation>(
        '/presentation_evaluations/',
        obj
      );
      return response.data;
    },

    findAllEvaluations: async () => {
      const response = await get<PresentationEvaluation[]>(
        '/presentation_evaluation/'
      );
      return response.data;
    },

    findEvaluationById: async (id: string) => {
      const response = await get<PresentationEvaluation>(
        `/presentation_evaluation/${id}`
      );
      return response.data;
    },

    updateEvaluation: async (id: string, obj: PresentationEvaluation) => {
      const response = await put<PresentationEvaluation>(
        `/presentation_evaluations/${id}`,
        obj
      );
      return response.data;
    },

    deleteEvaluation: async (id: string) => {
      await remove<PresentationEvaluation>(`/presentation_evaluations/${id}`);
    },
  };
};

export default usePresentationEvaluationsApi;

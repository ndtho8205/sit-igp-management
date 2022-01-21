import LabRotationEvaluation from '../types/labRotationEvaluation';
import LabSeminarEvaluation from '../types/labSeminarEvaluation';
import SemesterEndEvaluationSummary from '../types/semesterEndEvaluationSummary';
import ThesisProgramEvaluation from '../types/thesisProgramEvaluation';
import useAxios from './useAxios';

const useSemesterEndEvaluationApi = () => {
  const { get, post, put } = useAxios();
  const labRotationEndpoint = '/lab_rotation';
  const thesisProgramEndpoint = '/thesis_program';
  const labSeminarEndpoint = '/lab_seminar';

  return {
    getSummary: async (supervisor_id = '') => {
      const path = supervisor_id ? `/summary/${supervisor_id}` : '/summary/';
      const response = await get<SemesterEndEvaluationSummary[]>(path);
      return response.data;
    },

    createLabRotationEvaluation: async (
      presentation_id: string,
      obj: LabRotationEvaluation
    ) => {
      const response = await post<LabRotationEvaluation>(
        `${labRotationEndpoint}/${presentation_id}`,
        {
          ...obj,
          presentation_id,
        }
      );
      return response.data;
    },

    updateLabRotationEvaluation: async (
      presentation_id: string,
      obj: LabRotationEvaluation
    ) => {
      const response = await put<LabRotationEvaluation>(
        `${labRotationEndpoint}/${presentation_id}`,
        {
          ...obj,
          presentation_id,
        }
      );
      return response.data;
    },

    createThesisProgramEvaluation: async (
      presentation_id: string,
      obj: ThesisProgramEvaluation
    ) => {
      const response = await post<ThesisProgramEvaluation>(
        `${thesisProgramEndpoint}/${presentation_id}`,
        {
          ...obj,
          presentation_id,
        }
      );
      return response.data;
    },

    updateThesisProgramEvaluation: async (
      presentation_id: string,
      obj: ThesisProgramEvaluation
    ) => {
      const response = await put<ThesisProgramEvaluation>(
        `${thesisProgramEndpoint}/${presentation_id}`,
        {
          ...obj,
          presentation_id,
        }
      );
      return response.data;
    },

    createLabSeminarEvaluation: async (
      presentation_id: string,
      obj: LabSeminarEvaluation
    ) => {
      const response = await post<LabSeminarEvaluation>(
        `${labSeminarEndpoint}/${presentation_id}`,
        {
          ...obj,
          presentation_id,
        }
      );
      return response.data;
    },

    updateLabSeminarEvaluation: async (
      presentation_id: string,
      obj: LabSeminarEvaluation
    ) => {
      const response = await put<LabSeminarEvaluation>(
        `${labSeminarEndpoint}/${presentation_id}`,
        {
          ...obj,
          presentation_id,
        }
      );
      return response.data;
    },
  };
};

export default useSemesterEndEvaluationApi;

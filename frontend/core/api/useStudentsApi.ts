import moment from 'moment';
import Student from '../types/student';
import useAxios from './useAxios';

const useStudentsApi = () => {
  const { get, post, put, remove } = useAxios();
  const endpoint = '/students';
  return {
    createStudent: async (obj: Student) => {
      obj.admission_date = moment(obj.admission_date).format('YYYY-MM-DD');
      const response = await post<Student>(`${endpoint}/`, obj);
      return response.data;
    },

    findAllStudents: async () => {
      const response = await get<Student[]>(`${endpoint}/`);
      return response.data;
    },

    updateStudent: async (id: string, obj: Student) => {
      const response = await put<Student>(`${endpoint}/${id}`, obj);
      return response.data;
    },

    deleteStudent: async (id: string) => {
      await remove<Student>(`${endpoint}/${id}`);
    },
  };
};

export default useStudentsApi;

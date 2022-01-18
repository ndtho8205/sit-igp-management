import moment from 'moment';
import Student from '../types/student';
import useAxios from './useAxios';

const useStudentsApi = () => {
  const { get, post, put, remove } = useAxios();
  return {
    createStudent: async (obj: Student) => {
      obj.admission_date = moment(obj.admission_date).format('YYYY-MM-DD');
      const response = await post<Student>('/students/', obj);
      return response.data;
    },

    findAllStudents: async () => {
      const response = await get<Student[]>('/students/');
      return response.data;
    },

    findStudentById: async (id: string) => {
      const response = await get<Student>(`/students/${id}`);
      return response.data;
    },

    updateStudent: async (id: string, obj: Student) => {
      const response = await put<Student>(`/students/${id}`, obj);
      return response.data;
    },

    deleteStudent: async (id: string) => {
      await remove<Student>(`/students/${id}`);
    },
  };
};

export default useStudentsApi;

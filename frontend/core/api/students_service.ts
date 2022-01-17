import moment from 'moment';
import Student from '../types/student';
import { apiClient } from './apiClient';

class StudentsService {
  async create(obj: Student) {
    // FIXME: Date format
    obj.admission_date = moment(obj.admission_date).format('YYYY-MM-DD');
    const response = await apiClient.post<Student>('/students/', obj);
    return response.data;
  }

  async findAll() {
    const response = await apiClient.get<Student[]>('/students/');
    return response.data;
  }

  async findById(student_id: string) {
    const response = await apiClient.get<Student | null>(
      `/students/${student_id}`
    );
    return response.data;
  }

  async update(student_id: string, obj: Student) {
    const response = await apiClient.put<Student>(
      `/students/${student_id}`,
      obj
    );
    return response.data;
  }

  async delete(student_id: string) {
    await apiClient.delete(`/students/${student_id}`);
  }
}

const students_service = new StudentsService();

export default students_service;

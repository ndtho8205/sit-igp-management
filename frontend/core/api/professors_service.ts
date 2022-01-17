import Professor from '../types/professor';
import { apiClient } from './apiClient';

class ProfessorsService {
  async create(obj: Professor) {
    const response = await apiClient.post<Professor>('/professors/', obj);
    return response.data;
  }

  async findAll() {
    const response = await apiClient.get<Professor[]>('/professors/');
    return response.data;
  }

  async findById(professor_id: string) {
    const response = await apiClient.get<Professor | null>(
      `/professors/${professor_id}`
    );
    return response.data;
  }

  async update(professor_id: string, obj: Professor) {
    const response = await apiClient.put<Professor>(
      `/professors/${professor_id}`,
      obj
    );
    return response.data;
  }

  async delete(professor_id: string) {
    await apiClient.delete(`/professors/${professor_id}`);
  }
}

const professors_service = new ProfessorsService();

export default professors_service;

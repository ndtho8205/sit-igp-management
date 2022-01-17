import { DatePicker, Form, Input, Select } from 'antd';
import { useQueryClient } from 'react-query';
import students_service from '../../../core/api/students_service';
import Gender from '../../../core/types/gender';
import { rules } from '../../../core/validators';
import ModalForm from '../../common/ModalForm';
import ProfessorAutoComplete from '../../common/ProfessorAutoComplete';

const StudentCreateForm = () => {
  const queryClient = useQueryClient();

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findAllStudents');
  };

  return (
    <ModalForm
      title="New Student"
      okText="Create"
      buttonShape="circle"
      buttonType="primary"
      onOk={students_service.create}
      onSuccess={handleOnSuccess}
    >
      <Form.Item label="Full name" name="full_name" rules={rules.FullName}>
        <Input />
      </Form.Item>

      <Form.Item
        label="Admission date"
        name="admission_date"
        rules={[{ required: true, type: 'date' }]}
      >
        <DatePicker format="YYYY/MM/DD" />
      </Form.Item>

      <Form.Item label="Gender" name="gender">
        <Select allowClear>
          <Select.Option value={Gender.Male}>Male</Select.Option>
          <Select.Option value={Gender.Female}>Female</Select.Option>
          <Select.Option value={Gender.Other}>Other</Select.Option>
        </Select>
      </Form.Item>

      <Form.Item label="Email" name="email" rules={rules.UniversityEmail}>
        <Input />
      </Form.Item>

      <Form.Item label="Area of study" name="area_of_study">
        <Input />
      </Form.Item>

      <Form.Item label="Supervisor" name="supervisor_id">
        <ProfessorAutoComplete />
      </Form.Item>

      <Form.Item label="Advisor 1" name="advisor1_id">
        <ProfessorAutoComplete />
      </Form.Item>

      <Form.Item label="Advisor 2" name="advisor2_id">
        <ProfessorAutoComplete />
      </Form.Item>
    </ModalForm>
  );
};

export default StudentCreateForm;

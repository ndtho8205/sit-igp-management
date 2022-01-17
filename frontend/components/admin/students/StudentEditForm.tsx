import { EditOutlined } from '@ant-design/icons';
import { Form, Input, Select } from 'antd';
import { useQueryClient } from 'react-query';
import students_service from '../../../core/api/students_service';
import Gender from '../../../core/types/gender';
import Student from '../../../core/types/student';
import { rules } from '../../../core/validators';
import ModalForm from '../../common/ModalForm';
import ProfessorAutoComplete from '../../common/ProfessorAutoComplete';

type Props = {
  student: Student;
};

const StudentEditForm = ({ student }: Props) => {
  const queryClient = useQueryClient();

  const handleOnOk = async (obj: Student) => {
    return await students_service.update(student.id_, obj);
  };

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findAllStudents');
  };

  return (
    <ModalForm
      title="Edit Student"
      okText="Update"
      buttonIcon={<EditOutlined />}
      onOk={handleOnOk}
      onSuccess={handleOnSuccess}
      initialValues={student}
    >
      <Form.Item
        label="Full name"
        name="full_name"
        rules={[{ required: true }, ...rules.FullName]}
      >
        <Input />
      </Form.Item>

      {/* FIXME: moment Date
      <Form.Item
        label="Admission date"
        name="admission_date"
        rules={[{ required: true }]}
      >
        <DatePicker />
      </Form.Item> */}

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

export default StudentEditForm;

import { Form, Input } from 'antd';
import { useQueryClient } from 'react-query';
import useProfessorsApi from '../../../core/api/useProfessorsApi';
import { rules } from '../../../core/validators';
import ModalForm from '../../common/ModalForm';

const ProfessorCreateForm = () => {
  const queryClient = useQueryClient();
  const { createProfessor } = useProfessorsApi();

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findAllProfessors');
  };

  return (
    <ModalForm
      title="New Professor"
      okText="Create"
      buttonShape="circle"
      buttonType="primary"
      onOk={createProfessor}
      onSuccess={handleOnSuccess}
    >
      <Form.Item
        label="Full name"
        name="full_name"
        rules={[{ required: true }, ...rules.FullName]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Email"
        name="email"
        rules={[{ required: true }, ...rules.UniversityEmail]}
      >
        <Input />
      </Form.Item>
    </ModalForm>
  );
};

export default ProfessorCreateForm;

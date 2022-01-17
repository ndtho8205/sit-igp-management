import { EditOutlined } from '@ant-design/icons';
import { Form, Input } from 'antd';
import { useQueryClient } from 'react-query';
import professors_service from '../../../core/api/professors_service';
import Professor from '../../../core/types/professor';
import { rules } from '../../../core/validators';
import ModalForm from '../../common/ModalForm';

type Props = {
  professor: Professor;
};

const ProfessorEditForm = ({ professor }: Props) => {
  const queryClient = useQueryClient();

  const handleOnOk = async (obj: Professor) => {
    return await professors_service.update(professor.id_, obj);
  };

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findAllProfessors');
  };

  return (
    <ModalForm
      title="Edit Professor"
      okText="Update"
      buttonIcon={<EditOutlined />}
      onOk={handleOnOk}
      onSuccess={handleOnSuccess}
      initialValues={professor}
    >
      <Form.Item label="Full name" name="full_name" rules={rules.FullName}>
        <Input />
      </Form.Item>

      <Form.Item label="Email" name="email" rules={rules.UniversityEmail}>
        <Input />
      </Form.Item>
    </ModalForm>
  );
};

export default ProfessorEditForm;

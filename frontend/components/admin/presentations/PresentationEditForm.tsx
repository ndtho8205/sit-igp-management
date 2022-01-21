import { EditOutlined } from '@ant-design/icons';
import { Form, Input } from 'antd';
import { useQueryClient } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import { Presentation } from '../../../core/types/presentation';
import ModalForm from '../../common/ModalForm';
import ProfessorAutoComplete from '../../common/ProfessorAutoComplete';

type Props = {
  presentation: Presentation;
};

const PresentationEditForm = ({ presentation }: Props) => {
  const queryClient = useQueryClient();
  const { updatePresentation } = usePresentationsApi();

  const handleOnOk = async (obj: Presentation) => {
    return await updatePresentation(presentation.id_, obj);
  };

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findAllPresentations');
  };

  return (
    <ModalForm
      title="Edit Presentation"
      okText="Update"
      buttonIcon={<EditOutlined />}
      onOk={handleOnOk}
      onSuccess={handleOnSuccess}
      initialValues={presentation}
    >
      <Form.Item label="Presentation time" name="presentation_length">
        <Input />
      </Form.Item>

      <Form.Item label="Reviewer 1" name="reviewer1_id">
        <ProfessorAutoComplete />
      </Form.Item>

      <Form.Item label="Reviewer 2" name="reviewer2_id">
        <ProfessorAutoComplete />
      </Form.Item>

      <Form.Item label="Reviewer 3" name="reviewer3_id">
        <ProfessorAutoComplete />
      </Form.Item>

      <Form.Item label="Reviewer 4" name="reviewer4_id">
        <ProfessorAutoComplete />
      </Form.Item>

      <Form.Item label="Reviewer 5" name="reviewer5_id">
        <ProfessorAutoComplete />
      </Form.Item>
    </ModalForm>
  );
};

export default PresentationEditForm;

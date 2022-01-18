import { DatePicker, Form } from 'antd';
import { useQueryClient } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import ModalForm from '../../common/ModalForm';
import ProfessorAutoComplete from '../../common/ProfessorAutoComplete';
import StudentAutoComplete from '../../common/StudentAutoComplete';

const PresentationCreateForm = () => {
  const queryClient = useQueryClient();
  const { createPresentation } = usePresentationsApi();

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findAllPresentations');
  };

  return (
    <ModalForm
      title="New Presentation"
      okText="Create"
      buttonShape="circle"
      buttonType="primary"
      onOk={createPresentation}
      onSuccess={handleOnSuccess}
    >
      <Form.Item label="Student" name="student_id" rules={[{ required: true }]}>
        <StudentAutoComplete />
      </Form.Item>

      <Form.Item
        label="Presentation date"
        name="presentation_date"
        rules={[{ required: true, type: 'date' }]}
      >
        <DatePicker format="YYYY/MM/DD" />
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

export default PresentationCreateForm;

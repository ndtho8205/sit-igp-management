import { EditOutlined } from '@ant-design/icons';
import { Form, InputNumber } from 'antd';
import { useQueryClient } from 'react-query';
import useSemesterEndEvaluationApi from '../../../core/api/useSemesterEndEvaluationApi';
import SemesterEndEvaluationSummary from '../../../core/types/semesterEndEvaluationSummary';
import ModalForm from '../../common/ModalForm';

type Props = {
  summary: SemesterEndEvaluationSummary;
};

const LabRotationInputForm = ({ summary }: Props) => {
  const queryClient = useQueryClient();
  const { createLabRotationEvaluation, updateLabRotationEvaluation } =
    useSemesterEndEvaluationApi();

  console.log(summary);

  const handleOnOk = async (obj: { course_score: number }) => {
    if (summary.lab_rotation === null) {
      return await createLabRotationEvaluation(summary.presentation.id_, obj);
    }
    return await updateLabRotationEvaluation(summary.presentation.id_, obj);
  };

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('getSummary');
  };

  return (
    <ModalForm
      title="Input Lab Rotation Score"
      okText="Submit"
      buttonIcon={<EditOutlined />}
      onOk={handleOnOk}
      onSuccess={handleOnSuccess}
      initialValues={summary.lab_rotation}
    >
      <Form.Item label="Score" name="course_score">
        <InputNumber min="0.0" max="100.0" step="0.01" style={{ width: 200 }} />
      </Form.Item>
    </ModalForm>
  );
};

export default LabRotationInputForm;

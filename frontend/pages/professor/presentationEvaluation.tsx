import { Space, Typography } from 'antd';
import { ReactElement } from 'react';
import PresentationEvaluationsTable from '../../components/professor/presentationEvaluation/PresentationEvaluationsTable';
import PresentationTimeInputTable from '../../components/professor/presentationEvaluation/PresentationTimeInputTable';
import SemEndPresentationRubric from '../../components/professor/presentationEvaluation/SemEndPresentationRubric';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SemEndPresentationInputScorePage = () => {
  const { Title } = Typography;
  return (
    <Space direction="vertical">
      <SemEndPresentationRubric />
      <Title level={4}>Input Presentation Time (as Session Chair)</Title>
      <PresentationTimeInputTable />
      <Title level={4}>Input Score (as Reviewer)</Title>
      <PresentationEvaluationsTable />
    </Space>
  );
};

SemEndPresentationInputScorePage.getLayout = function getLayout(
  page: ReactElement
) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default SemEndPresentationInputScorePage;

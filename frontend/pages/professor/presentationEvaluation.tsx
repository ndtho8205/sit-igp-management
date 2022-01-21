import { Space } from 'antd';
import { ReactElement } from 'react';
import PresentationEvaluationsTable from '../../components/professor/presentationEvaluation/PresentationEvaluationsTable';
import SemEndPresentationRubric from '../../components/professor/presentationEvaluation/SemEndPresentationRubric';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SemEndPresentationInputScorePage = () => {
  return (
    <Space direction="vertical">
      <SemEndPresentationRubric />
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

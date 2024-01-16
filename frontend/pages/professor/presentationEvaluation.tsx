import { Space } from 'antd';
import { ReactElement } from 'react';
import PresentationEvaluationsTable from '../../components/professor/presentationEvaluation/PresentationEvaluationsTable';
import PresentationTimeInputTable from '../../components/professor/presentationEvaluation/PresentationTimeInputTable';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SemEndPresentationInputScorePage = () => {
  return (
    <Space direction="vertical">
      <PresentationTimeInputTable />
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

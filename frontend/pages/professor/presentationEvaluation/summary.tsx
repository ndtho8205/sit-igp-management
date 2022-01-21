import { ReactElement } from 'react';
import PresentationEvaluationsTable from '../../../components/professor/presentationEvaluation/PresentationEvaluationsTable';
import ProfessorPagesLayout from '../../../layouts/ProfessorPagesLayout';

const SemEndPresentationViewScorePage = () => {
  return (
    <div>
      <h1>Semester End Presentation - View Scores</h1>
      <PresentationEvaluationsTable page="View" />
    </div>
  );
};

SemEndPresentationViewScorePage.getLayout = function getLayout(
  page: ReactElement
) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default SemEndPresentationViewScorePage;

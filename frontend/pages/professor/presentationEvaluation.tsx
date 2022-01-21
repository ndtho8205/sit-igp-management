import { ReactElement } from 'react';
import PresentationEvaluationsTable from '../../components/professor/presentationEvaluation/PresentationEvaluationsTable';
import SemEndPresentationRubric from '../../components/professor/presentationEvaluation/SemEndPresentationRubric';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SemEndPresentationInputScorePage = () => {
  return (
    <div>
      <h1>Semester End Presentation - Input Scores</h1>
      <p>
        {' '}
        <SemEndPresentationRubric />{' '}
      </p>
      <PresentationEvaluationsTable />
    </div>
  );
};

SemEndPresentationInputScorePage.getLayout = function getLayout(
  page: ReactElement
) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default SemEndPresentationInputScorePage;

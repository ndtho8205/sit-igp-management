import { ReactElement } from 'react';
import SemEndPresentationRubric from '../../../components/professor/presentationEvaluation/SemEndPresentationRubric';
import SemEndPresentationTable from '../../../components/professor/presentationEvaluation/SemEndPresentationTable';
import ProfessorPagesLayout from '../../../layouts/ProfessorPagesLayout';

const SemEndPresentationInputScorePage = () => {
  return (
    <div>
      <h1>Semester End Presentation - Input Scores</h1>
      <p>
        {' '}
        <SemEndPresentationRubric />{' '}
      </p>
      <SemEndPresentationTable page="Input" />
    </div>
  );
};

SemEndPresentationInputScorePage.getLayout = function getLayout(
  page: ReactElement
) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default SemEndPresentationInputScorePage;

import { ReactElement } from 'react';
import SemEndPresentationTable from '../../../components/professor/semendpresentation/SemEndPresentationTable';
import ProfessorPagesLayout from '../../../layouts/ProfessorPagesLayout';

const SemEndPresentationViewScorePage = () => {
  return (
    <div>
      <h1>Semester End Presentation - View Scores</h1>
      <SemEndPresentationTable page="View"/>
    </div>
  );
};

SemEndPresentationViewScorePage.getLayout = function getLayout(page: ReactElement) {
    return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
  };

export default SemEndPresentationViewScorePage;
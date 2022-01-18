import { ReactElement } from 'react';
import SupervisorEvaluationTable from '../../components/professor/supervisorevaluation/SupervisorEvaluationTable';
import SemEndPresentationRubric from '../../components/professor/semendpresentation/SemEndPresentationRubric';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SupervisorEvaluationPage = () => {
  return (
    <div>
      <h1>Supervisor Evaluation - Input Scores</h1>
      {/* <p> <SemEndPresentationRubric/> </p> */}
      <SupervisorEvaluationTable page="Input"/>
    </div>
  );
};

SupervisorEvaluationPage.getLayout = function getLayout(page: ReactElement) {
    return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
  };

export default SupervisorEvaluationPage;
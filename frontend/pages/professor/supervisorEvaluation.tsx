import { ReactElement } from 'react';
import SupervisorEvaluationTable from '../../components/professor/supervisorEvaluation/SupervisorEvaluationTable';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SupervisorEvaluationPage = () => {
  return <SupervisorEvaluationTable />;
};

SupervisorEvaluationPage.getLayout = function getLayout(page: ReactElement) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default SupervisorEvaluationPage;

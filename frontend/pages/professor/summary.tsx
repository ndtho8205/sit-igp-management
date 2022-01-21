import { ReactElement } from 'react';
import SummaryTable from '../../components/professor/summary/SummaryTable';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SummaryPage = () => {
  return (
    <div>
      <h1>Summary</h1>
      <SummaryTable />
    </div>
  );
};

SummaryPage.getLayout = function getLayout(page: ReactElement) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default SummaryPage;

import { ReactElement } from 'react';
import SummaryTable from '../../components/admin/summary/SummaryTable';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const SummaryPage = () => {
  return <SummaryTable />;
};

SummaryPage.getLayout = function getLayout(page: ReactElement) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default SummaryPage;

import { ReactElement } from 'react';
import SummaryTable from '../../components/admin/summary/SummaryTable';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const SummaryPage = () => {
  return <SummaryTable />;
};

SummaryPage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default SummaryPage;

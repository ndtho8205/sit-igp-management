import { ReactElement } from 'react';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const AdminHomePage = () => {
  return <h1>Home</h1>;
};

AdminHomePage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default AdminHomePage;

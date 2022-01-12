import { ReactElement } from 'react';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const StudentsManagementPage = () => {
  return (
    <div>
      <h1>Students</h1>
    </div>
  );
};

StudentsManagementPage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default StudentsManagementPage;

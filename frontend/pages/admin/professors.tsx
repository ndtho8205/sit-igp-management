import { ReactElement } from 'react';
import ProfessorCreateForm from '../../components/admin/professors/ProfessorCreateForm';
import ProfessorsTable from '../../components/admin/professors/ProfessorsTable';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const ProfessorsManagementPage = () => {
  return (
    <div>
      <h1>Professors</h1>

      <ProfessorCreateForm />

      <ProfessorsTable />
    </div>
  );
};

ProfessorsManagementPage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default ProfessorsManagementPage;

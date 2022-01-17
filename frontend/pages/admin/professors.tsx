import { Space } from 'antd';
import { ReactElement } from 'react';
import ProfessorCreateForm from '../../components/admin/professors/ProfessorCreateForm';
import ProfessorsTable from '../../components/admin/professors/ProfessorsTable';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const ProfessorsManagementPage = () => {
  return (
    <Space direction="vertical">
      <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
        <ProfessorCreateForm />
      </div>

      <ProfessorsTable />
    </Space>
  );
};

ProfessorsManagementPage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default ProfessorsManagementPage;

import { Space } from 'antd';
import { ReactElement } from 'react';
import PresentationCreateForm from '../../components/admin/presentations/PresentationCreateForm';
import PresentationsTable from '../../components/admin/presentations/PresentationsTable';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const ProfessorsManagementPage = () => {
  return (
    <Space direction="vertical">
      <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
        <PresentationCreateForm />
      </div>

      <PresentationsTable />
    </Space>
  );
};

ProfessorsManagementPage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default ProfessorsManagementPage;

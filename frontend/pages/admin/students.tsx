import { Space } from 'antd';
import { ReactElement } from 'react';
import StudentCreateForm from '../../components/admin/students/StudentCreateForm';
import StudentsTable from '../../components/admin/students/StudentsTable';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const StudentsManagementPage = () => {
  return (
    <Space direction="vertical">
      <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
        <StudentCreateForm />
      </div>

      <StudentsTable />
    </Space>
  );
};

StudentsManagementPage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default StudentsManagementPage;

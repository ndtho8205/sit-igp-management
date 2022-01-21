import { Space } from 'antd';
import { ReactElement } from 'react';
import LabRotationTable from '../../components/admin/lab_rotation/LabRotationTable';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const LabRotationManagementPage = () => {
  return (
    <Space direction="vertical">
      <LabRotationTable />
    </Space>
  );
};

LabRotationManagementPage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default LabRotationManagementPage;

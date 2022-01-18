import { Typography } from 'antd';
import { ReactElement } from 'react';
import AdminPagesLayout from '../../layouts/AdminPagesLayout';

const AdminHomePage = () => {
  return <Typography.Title level={5}>Welcome!</Typography.Title>;
};

AdminHomePage.getLayout = function getLayout(page: ReactElement) {
  return <AdminPagesLayout>{page}</AdminPagesLayout>;
};

export default AdminHomePage;

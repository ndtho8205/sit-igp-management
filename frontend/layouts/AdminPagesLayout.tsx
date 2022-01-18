import {
  DesktopOutlined,
  HomeOutlined,
  IdcardOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Layout } from 'antd';
import { ReactNode, useState } from 'react';
import MainNav from '../components/admin/AdminMainNav';
import RoutePageHeader from '../components/common/RoutePageHeader';
import styles from '../styles/AdminPagesLayout.module.css';

const { Content, Footer, Sider } = Layout;

type Props = {
  children?: ReactNode;
};

const AdminPagesLayout = ({ children }: Props) => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  const menuItems = [
    { href: '/admin', label: 'Home', icon: <HomeOutlined /> },
    {
      href: '/admin/presentations',
      label: 'Semester End Presentations',
      icon: <DesktopOutlined />,
    },
    {
      href: '/admin/professors',
      label: 'Professors',
      icon: <IdcardOutlined />,
    },
    { href: '/admin/students', label: 'Students', icon: <UserOutlined /> },
  ];

  const routeLabels: { [route: string]: string } = menuItems.reduce(
    (result, item) => {
      return {
        ...result,
        [item.href]: item.label,
      };
    },
    {}
  );

  console.log(routeLabels);

  return (
    <Layout className={styles.adminContainer}>
      <Sider
        width="300"
        collapsed={isCollapsed}
        collapsible
        onCollapse={() => setIsCollapsed(!isCollapsed)}
      >
        <div className={styles.logo} />
        <MainNav menuItems={menuItems} />
      </Sider>

      <Layout>
        <RoutePageHeader routeLabels={routeLabels} />
        <Content className={styles.content}>{children}</Content>
        <Footer></Footer>
      </Layout>
    </Layout>
  );
};

export default AdminPagesLayout;

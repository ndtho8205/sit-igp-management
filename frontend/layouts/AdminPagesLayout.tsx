import { Layout } from 'antd';
import { FunctionComponent, ReactNode, useState } from 'react';
import MainNav from '../components/admin/AdminMainNav';
import Profile from '../components/common/Profile';
import styles from '../styles/AdminPagesLayout.module.css';

const { Header, Content, Footer, Sider } = Layout;

type Props = {
  children?: ReactNode;
};

const AdminPagesLayout: FunctionComponent = ({ children }: Props) => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  return (
    <Layout className={styles.adminContainer}>
      <Sider
        collapsed={isCollapsed}
        collapsible
        onCollapse={() => setIsCollapsed(!isCollapsed)}
      >
        <div className={styles.logo} />
        <MainNav />
      </Sider>

      <Layout>
        <Header className="header">
          <Profile />
        </Header>
        <Content className={styles.content}>{children}</Content>
        <Footer></Footer>
      </Layout>
    </Layout>
  );
};

export default AdminPagesLayout;

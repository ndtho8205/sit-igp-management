import { DesktopOutlined, HomeOutlined } from '@ant-design/icons';
import { Layout, Menu } from 'antd';
import Link from 'next/link';
import { useState } from 'react';
import styles from '../styles/AppLayout.module.css';
import { useRouter } from 'next/router';

const { Header, Content, Footer, Sider } = Layout;

function AppLayout({ children }) {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const router = useRouter();
  console.log(router);

  return (
    <Layout className={styles.container}>
      <Sider
        className={styles.sider}
        collapsed={isCollapsed}
        collapsible
        onCollapse={() => setIsCollapsed(!isCollapsed)}
      >
        <div className={styles.logo} />
        <Menu theme="dark" defaultSelectedKeys={[router.route]} mode="inline">
          <Menu.Item key="/" icon={<HomeOutlined />}>
            <Link href="/">Home</Link>
          </Menu.Item>
          <Menu.Item key="/professors" icon={<DesktopOutlined />}>
            <Link href="/professors">Professors</Link>
          </Menu.Item>
          <Menu.Item key="/students" icon={<DesktopOutlined />}>
            <Link href="/students">Students</Link>
          </Menu.Item>
        </Menu>
      </Sider>

      <Layout className={styles.site_container}>
        <Header className={styles.header}></Header>
        <Content className={styles.content}>{children}</Content>
        <Footer className={styles.footer}></Footer>
      </Layout>
    </Layout>
  );
}

export default AppLayout;

import { Layout, Typography } from 'antd';
import { FunctionComponent, ReactNode, useState } from 'react';
import Profile from '../components/common/Profile';
import MainNav from '../components/professor/ProfessorMainNav';
import styles from '../styles/ProfessorPagesLayout.module.css';

const { Header, Content, Footer, Sider } = Layout;
const { Title } = Typography;

type Props = {
  children?: ReactNode;
};

const ProfessorPagesLayout: FunctionComponent = ({ children }: Props) => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  return (
    <Layout className={styles.professorContainer}>
      <Sider
        width={300}
        collapsed={isCollapsed}
        collapsible
        onCollapse={() => setIsCollapsed(!isCollapsed)}
      >
        {/* <div className={styles.logo} /> */}
        <Title className={styles.logo}>TEST</Title>
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

export default ProfessorPagesLayout;

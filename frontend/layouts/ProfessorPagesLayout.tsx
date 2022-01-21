import { Layout } from 'antd';
import { FunctionComponent, ReactNode, useState } from 'react';
import RoutePageHeader from '../components/common/RoutePageHeader';
import MainNav from '../components/professor/ProfessorMainNav';
import styles from '../styles/ProfessorPagesLayout.module.css';

const { Content, Footer, Sider } = Layout;

type Props = {
  children?: ReactNode;
};

const ProfessorPagesLayout: FunctionComponent = ({ children }: Props) => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  const routeLabels = {
    '/professor': 'Home',
    '/professor/presentationEvaluation': 'Semester End Presentation',
    '/professor/summary': 'Summary',
    '/professor/supervisorEvaluation': 'Supervisor Evaluation',
  };

  return (
    <Layout className={styles.professorContainer}>
      <Sider
        width={300}
        collapsed={isCollapsed}
        collapsible
        onCollapse={() => setIsCollapsed(!isCollapsed)}
      >
        <div className={styles.logo} />
        <MainNav />
      </Sider>

      <Layout>
        <RoutePageHeader routeLabels={routeLabels} />
        <Content className={styles.content}>{children}</Content>
        <Footer></Footer>
      </Layout>
    </Layout>
  );
};

export default ProfessorPagesLayout;

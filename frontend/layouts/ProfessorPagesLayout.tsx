import { Layout } from 'antd';
import { FunctionComponent, ReactNode } from 'react';
import Profile from '../components/common/Profile';

const { Header, Content, Footer } = Layout;

type Props = {
  children?: ReactNode;
};

const ProfessorPagesLayout: FunctionComponent = ({ children }: Props) => {
  return (
    <Layout>
      <Header className="header">
        <Profile />
      </Header>
      <Content>{children}</Content>
      <Footer></Footer>
    </Layout>
  );
};

export default ProfessorPagesLayout;

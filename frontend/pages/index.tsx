import { Space, Typography } from 'antd';
import type { NextPage } from 'next';
import LoginButton from '../components/common/LoginButton';

const Home: NextPage = () => {
  return (
    <div
      style={{
        height: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Space direction="vertical" align="center">
        <Typography.Title level={5}>
          Please login using the university email address.
        </Typography.Title>
        <LoginButton type="primary" />
      </Space>
    </div>
  );
};

export default Home;

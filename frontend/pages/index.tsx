import { useAuth0 } from '@auth0/auth0-react';
import { Space, Typography } from 'antd';
import type { NextPage } from 'next';
import LoginButton from '../components/common/LoginButton';
import { notify } from '../core/utils';

const Home: NextPage = () => {
  const auth = useAuth0();

  if (auth.error) {
    notify('error', auth.error);
  }

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
        <LoginButton type="primary" isLoading={auth.isLoading} />
      </Space>
    </div>
  );
};

export default Home;

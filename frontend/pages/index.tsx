import { useAuth0 } from '@auth0/auth0-react';
import { Button, Space, Typography } from 'antd';
import type { NextPage } from 'next';
import { useRouter } from 'next/router';
import { useEffect } from 'react';
import config from '../core/config';
import { notify } from '../core/utils';

const Home: NextPage = () => {
  const auth = useAuth0();
  const router = useRouter();

  if (auth.error) {
    notify('error', auth.error);
  }

  useEffect(() => {
    router.prefetch('/professor');
  });

  const message = <>
    <Typography.Title level={5}>
      Please login using the university email address.
    </Typography.Title>
    <Button
      type="primary"
      onClick={() => auth.loginWithRedirect()}
      loading={auth.isLoading}
    >
      Log In
    </Button>
  </> ? (
    !auth.isAuthenticated
  ) : (
    <Typography.Title level={5}>
      You already logged in. We will redirect you to the SIT IGP Management
      dashboard.
    </Typography.Title>
  );

  if (auth.isAuthenticated) {
    router.push(config.authRedirectUri);
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
        {message}
      </Space>
    </div>
  );
};

export default Home;

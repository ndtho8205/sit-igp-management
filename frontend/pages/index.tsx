import { useAuth0 } from '@auth0/auth0-react';
import { Button, Space, Spin, Typography } from 'antd';
import type { NextPage } from 'next';
import { useRouter } from 'next/router';
import { ReactNode, useEffect } from 'react';
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

  let children: ReactNode;

  if (auth.isAuthenticated) {
    const user_email = auth.user?.email;

    if (
      user_email &&
      user_email.slice(user_email.indexOf('@')) !== '@shibaura-it.ac.jp'
    ) {
      alert(
        'Failed to vefify your login information. Please use university email address to login.'
      );

      auth.logout();
    } else {
      router.push('/professor');
    }
    children = <Spin size="large" />;
  } else {
    children = (
      <Space direction="vertical" align="center">
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
      </Space>
    );
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
      {children}
    </div>
  );
};

export default Home;

import { useAuth0 } from '@auth0/auth0-react';
import { Button, Image, Space } from 'antd';
import { notify } from '../../core/utils';

const Profile = () => {
  const { user, isAuthenticated, error, logout } = useAuth0();

  if (error) {
    notify('error', error);
  }

  if (isAuthenticated && user) {
    return (
      <Space align="center">
        <Image
          src={user.picture}
          alt={user.name}
          width={32}
          height={32}
          style={{ borderRadius: '100%' }}
        />
        {user.name}
        <Button onClick={() => logout({ returnTo: window.location.origin })}>
          Log out
        </Button>
      </Space>
    );
  }

  return <div />;
};

export default Profile;

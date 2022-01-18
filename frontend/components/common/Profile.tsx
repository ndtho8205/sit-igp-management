import { useAuth0 } from '@auth0/auth0-react';
import { Image, notification, Space } from 'antd';
import LoginButton from './LoginButton';
import LogoutButton from './LogoutButton';

const Profile = () => {
  const { user, isAuthenticated, error } = useAuth0();

  if (error) {
    notification['error']({
      key: 'Profile',
      message: 'Oops...',
      description: error.message,
    });
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
        <LogoutButton />
      </Space>
    );
  }

  return <LoginButton />;
};

export default Profile;

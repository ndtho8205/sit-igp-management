import { useAuth0 } from '@auth0/auth0-react';
import { notification, Space } from 'antd';
import Image from 'next/image';
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
      <Space>
        <Image src={user.picture} alt={user.name} width={32} height={32} />
        <span>
          {user.name} ({user.email})
        </span>
        <LogoutButton />
      </Space>
    );
  }

  return <LoginButton />;
};

export default Profile;

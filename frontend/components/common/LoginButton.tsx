import { useAuth0 } from '@auth0/auth0-react';
import { Button } from 'antd';

type Props = {
  type?: 'primary' | 'default';
  isLoading?: boolean;
};

const LoginButton = (props: Props) => {
  const { loginWithRedirect, user } = useAuth0();

  console.log(user);
  console.log(useAuth0);
  return (
    <Button
      type={props.type || 'default'}
      onClick={() => loginWithRedirect()}
      loading={props.isLoading}
    >
      Log In
    </Button>
  );
};

export default LoginButton;

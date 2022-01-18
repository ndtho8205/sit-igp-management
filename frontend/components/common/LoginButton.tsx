import { useAuth0 } from '@auth0/auth0-react';
import { Button } from 'antd';

type Props = {
  type?: 'primary' | 'default';
};

const LoginButton = (props: Props) => {
  const { loginWithRedirect } = useAuth0();

  return (
    <Button type={props.type || 'default'} onClick={() => loginWithRedirect()}>
      Log In
    </Button>
  );
};

export default LoginButton;

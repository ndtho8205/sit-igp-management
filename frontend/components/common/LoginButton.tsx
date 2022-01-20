import { useAuth0 } from '@auth0/auth0-react';
import { Button } from 'antd';
import { notify } from '../../core/utils';

type Props = {
  type?: 'primary' | 'default';
};

const LoginButton = (props: Props) => {
  const auth = useAuth0();

  if (auth.error) {
    notify('error', auth.error);
  }

  if (auth.isAuthenticated) {
    console.log({ user: auth.user });
    return <div> Hello {auth.user?.name}</div>;
  } else {
    return (
      <Button
        type={props.type || 'default'}
        onClick={() => auth.loginWithRedirect()}
        loading={auth.isLoading}
      >
        Log In
      </Button>
    );
  }
};

export default LoginButton;

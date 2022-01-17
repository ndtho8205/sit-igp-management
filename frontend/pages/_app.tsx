import { Auth0Provider } from '@auth0/auth0-react';
import moment from 'moment';
import { NextPage } from 'next';
import type { AppProps } from 'next/app';
import { ReactElement, ReactNode } from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import config from '../core/config';
import '../styles/globals.css';

moment.locale('jp');

const queryClient = new QueryClient();

type NextPageWithLayout = NextPage & {
  getLayout?: (page: ReactElement) => ReactNode;
};

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

function App({ Component, pageProps }: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page: ReactElement) => page);

  return (
    <Auth0Provider
      domain={config.authDomain}
      clientId={config.authClientId}
      redirectUri={config.authRedirectUri}
    >
      <QueryClientProvider client={queryClient}>
        <div id="app">{getLayout(<Component {...pageProps} />)}</div>
      </QueryClientProvider>
    </Auth0Provider>
  );
}

export default App;

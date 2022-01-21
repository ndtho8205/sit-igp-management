import { Auth0Provider } from '@auth0/auth0-react';
import { NextPage } from 'next';
import type { AppProps } from 'next/app';
import Router from 'next/router';
import { ReactElement, ReactNode } from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import config from '../core/config';
import '../styles/globals.css';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 20,
    },
  },
});

type NextPageWithLayout = NextPage & {
  getLayout?: (page: ReactElement) => ReactNode;
};

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

const onRedirectCallback = (appState) => {
  Router.replace(appState?.returnTo || '/');
};

function App({ Component, pageProps }: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page: ReactElement) => page);

  return (
    <QueryClientProvider client={queryClient}>
      <Auth0Provider
        domain={config.authDomain}
        clientId={config.authClientId}
        redirectUri={config.authRedirectUri}
        audience={config.authApiAudience}
        useRefreshTokens
        cacheLocation="localstorage"
      >
        <div id="app">{getLayout(<Component {...pageProps} />)}</div>
      </Auth0Provider>
    </QueryClientProvider>
  );
}

export default App;

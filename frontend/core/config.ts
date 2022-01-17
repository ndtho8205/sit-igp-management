const config = {
  authDomain: process.env.NEXT_PUBLIC_AUTH_DOMAIN as string,
  authClientId: process.env.NEXT_PUBLIC_AUTH_CLIENT_ID as string,
  authRedirectUri: process.env.NEXT_PUBLIC_AUTH_REDIRECT_URI as string,
  authApiAudience: process.env.NEXT_PUBLIC_AUTH_API_AUDIENCE as string,

  apiServerUrl: process.env.NEXT_PUBLIC_API_SERVER_URL as string,
};

export default config;

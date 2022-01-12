const config = {
  authDomain: process.env.NEXT_PUBLIC_AUTH_DOMAIN,
  authClientId: process.env.NEXT_PUBLIC_AUTH_CLIENT_ID,
  authRedirectUri: process.env.NEXT_PUBLIC_AUTH_REDIRECT_URI,
  authApiAudience: process.env.NEXT_PUBLIC_AUTH_API_AUDIENCE,

  apiServerUrl: process.env.NEXT_PUBLIC_API_SERVER_URL,
};

export default config;

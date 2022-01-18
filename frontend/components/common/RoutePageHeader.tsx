import { PageHeader } from 'antd';
import { useRouter } from 'next/router';
import Profile from './Profile';

type Props = {
  routeLabels: { [route: string]: string };
};

const RoutePageHeader = ({ routeLabels }: Props) => {
  const router = useRouter();

  return (
    <PageHeader
      className="header"
      title={routeLabels[router.route]}
      extra={[<Profile key="1" />]}
    ></PageHeader>
  );
};

export default RoutePageHeader;

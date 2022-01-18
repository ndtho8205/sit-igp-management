import { Menu } from 'antd';
import Link from 'next/link';
import { useRouter } from 'next/router';
import { ReactNode } from 'react';

type Props = {
  menuItems: {
    href: string;
    label: string;
    icon: ReactNode;
  }[];
};

const AdminMainNav = ({ menuItems }: Props) => {
  const router = useRouter();

  return (
    <Menu theme="dark" defaultSelectedKeys={[router.route]} mode="inline">
      {menuItems.map(({ href, label, icon }) => (
        <Menu.Item key={href} icon={icon}>
          <Link href={href}>{label}</Link>
        </Menu.Item>
      ))}
    </Menu>
  );
};

export default AdminMainNav;

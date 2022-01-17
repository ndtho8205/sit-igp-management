import { HomeOutlined, IdcardOutlined, UserOutlined } from '@ant-design/icons';
import { Menu } from 'antd';
import Link from 'next/link';
import { useRouter } from 'next/router';

const AdminMainNav = () => {
  const router = useRouter();
  const menuItems = [
    { href: '/admin', label: 'Home', icon: <HomeOutlined /> },
    {
      href: '/admin/professors',
      label: 'Professors',
      icon: <IdcardOutlined />,
    },
    { href: '/admin/students', label: 'Students', icon: <UserOutlined /> },
  ];

  return (
    <Menu theme="dark" defaultSelectedKeys={[router.route]} mode="inline">
      {menuItems.map(({ href, label, icon }) => (
        <Menu.Item key={href} icon={icon}>
          {' '}
          <Link href={href}>{label}</Link>
        </Menu.Item>
      ))}{' '}
    </Menu>
  );
};

export default AdminMainNav;

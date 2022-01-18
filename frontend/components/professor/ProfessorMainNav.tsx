import { HomeOutlined, UserSwitchOutlined, EditOutlined, ProfileOutlined, FundViewOutlined, DesktopOutlined } from '@ant-design/icons';
import { Menu } from 'antd';
import Link from 'next/link';
import { useRouter } from 'next/router';

const AdminMainNav = () => {
  const router = useRouter();
  const { SubMenu } = Menu;
  const menuItems = [
    { href: '/professor', label: 'Home', icon: <HomeOutlined /> },
    {
      href: '/professor/semendpresentation/viewscore',
      label: 'Semester End Presentation',
      icon: <DesktopOutlined />,
      subItems: [
        {
          href: '/professor/semendpresentation/inputscore',
          label: 'Input Score',
          icon: <EditOutlined />,
        },
        {
          href: '/professor/semendpresentation/viewscore',
          label: 'View Score',
          icon: <ProfileOutlined />,
        },
      ],
    },
    { href: '/professor/supervisorevaluation', label: 'Supervisor Evaluation', icon: <FundViewOutlined /> },
    { href: '/professor/labrotation', label: 'Lab Rotation', icon: <UserSwitchOutlined /> },
  ];

  function renderMenuItems() {
    const nav = [];
    for (const menuItem of menuItems) {
      if (menuItem.subItems) {
        nav.push(
          <SubMenu
            key={menuItem.href}
            icon={menuItem.icon}
            title={menuItem.label}
          >
            {menuItem.subItems.map(({ href, label, icon }) => (
              <Menu.Item key={href} icon={icon}>
                <Link href={href}>{label}</Link>
              </Menu.Item>
            ))}
          </SubMenu>
        );
      } else {
        nav.push(
          <Menu.Item key={menuItem.href} icon={menuItem.icon}>
            <Link href={menuItem.href}>{menuItem.label}</Link>
          </Menu.Item>
        );
      }
    }
    return nav;
  }

  return (
    <Menu theme="dark" defaultSelectedKeys={[router.route]} mode="inline">
      {renderMenuItems()}
    </Menu>
  );
};

export default AdminMainNav;

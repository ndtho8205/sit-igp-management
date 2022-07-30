import {
  DesktopOutlined,
  FundViewOutlined,
  HomeOutlined,
  ProfileOutlined,
} from '@ant-design/icons';
import { useAuth0 } from '@auth0/auth0-react';
import { Menu } from 'antd';
import Link from 'next/link';
import { useRouter } from 'next/router';

const ProfessorMainNav = () => {
  const router = useRouter();
  const { SubMenu } = Menu;
  const auth = useAuth0();
  const canViewSummary = () => {
    if (auth.isAuthenticated) {
      const user_email = auth.user?.email;

      if (
        user_email === 'kamioka@shibaura-it.ac.jp' ||
        user_email === 'zam08580@shibaura-it.ac.jp' ||
        user_email === 'nb20501@shibaura-it.ac.jp'
      ) {
        return true;
      }
    }

    return false;
  };

  const menuItems = [
    { href: '/professor', label: 'Home', icon: <HomeOutlined /> },
    {
      href: '/professor/presentationEvaluation',
      label: 'Semester End Presentation',
      icon: <DesktopOutlined />,
    },
    {
      href: '/professor/supervisorEvaluation',
      label: 'Supervisor Evaluation',
      icon: <FundViewOutlined />,
    },
  ];

  if (canViewSummary()) {
    menuItems.push({
      href: '/professor/presentationSummary',
      label: 'Summary',
      icon: <ProfileOutlined />,
    });
  }

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

export default ProfessorMainNav;

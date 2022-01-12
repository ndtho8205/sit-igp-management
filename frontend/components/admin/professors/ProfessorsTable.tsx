import { notification, Space, Table, Tag } from 'antd';
import { useQuery } from 'react-query';
import apiClient from '../../../core/api/apiClient';

function ProfessorsTable() {
  const { isLoading, error, data } = useQuery('professors', () =>
    apiClient.get('/professors/').then((res) => res.data)
  );

  if (error) {
    notification['error']({
      key: 'Profile',
      message: 'Oops...',
      description: error.message,
    });
  }

  const columns = [
    { title: 'Full name', dataIndex: 'full_name', key: 'full_name' },
    { title: 'Email', dataIndex: 'email', key: 'full_name' },
    {
      title: 'Status',
      dataIndex: 'is_active',
      key: 'is_active',
      render: (is_active: boolean) => {
        console.log(is_active);
        const color = is_active ? 'geekblue' : 'volcano';
        const status = is_active ? 'Logged in' : 'Pending Invite';
        return <Tag color={color}>{status}</Tag>;
      },
    },
    {
      title: 'Action',
      key: 'action',
      render: (text, record) => {
        console.log({ text, record });

        return (
          <Space size="middle">
            <a>Edit</a>
            <a>Delete</a>
          </Space>
        );
      },
    },
  ];

  return (
    <Table
      dataSource={data}
      columns={columns}
      loading={isLoading}
      rowKey="professor_id"
      showSorterTooltip
      sticky
    ></Table>
  );
}

export default ProfessorsTable;

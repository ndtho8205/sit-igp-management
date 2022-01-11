import { Space, Table, Tag } from 'antd';
import { useQuery } from 'react-query';

function ProfessorsTable() {
  const { isLoading, error, data } = useQuery('repoData', () =>
    fetch('http://localhost:8000/api/professors').then((res) => res.json())
  );

  console.log({ error });

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

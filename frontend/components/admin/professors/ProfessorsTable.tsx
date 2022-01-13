import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import {
  Button,
  message,
  notification,
  Popconfirm,
  Space,
  Table,
  Tag,
} from 'antd';
import React from 'react';
import { useQuery } from 'react-query';
import apiClient from '../../../core/api/apiClient';

type ProfessorEntity = {
  professor_id: number;
  full_name: string;
  email: string;
  is_active: boolean;
};

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

  const handleDelete = (record: ProfessorEntity) => {
    apiClient
      .delete(`/professors/${record.professor_id}`)
      .then(() => {
        message.success('Delete success!');
      })
      .catch((error) => {
        message.error('Delete fail!');
        console.log(error);
      });
  };

  const columns = [
    { title: 'Full name', dataIndex: 'full_name', key: 'full_name' },
    { title: 'Email', dataIndex: 'email', key: 'full_name' },
    {
      title: 'Status',
      dataIndex: 'is_active',
      key: 'is_active',
      render: (is_active: boolean) => {
        const color = is_active ? 'geekblue' : 'volcano';
        const status = is_active ? 'Logged in' : 'Pending Invite';
        return <Tag color={color}>{status}</Tag>;
      },
    },
    {
      title: 'Action',
      key: 'action',
      render: (_, record: ProfessorEntity) => {
        return (
          <Space size="middle">
            <Button icon={<EditOutlined />} />
            <Popconfirm
              title="Sure to Delete?"
              onConfirm={() => handleDelete(record)}
            >
              <Button danger icon={<DeleteOutlined />} />
            </Popconfirm>
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

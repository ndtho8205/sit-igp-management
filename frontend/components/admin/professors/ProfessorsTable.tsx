import { Space, Table, Tag } from 'antd';
import React from 'react';
import { useQuery, useQueryClient } from 'react-query';
import useProfessorsApi from '../../../core/api/useProfessorsApi';
import Professor from '../../../core/types/professor';
import { notify } from '../../../core/utils';
import DeletePopconfirm from '../../common/DeletePopconfirm';
import ProfessorEditForm from './ProfessorEditForm';

function ProfessorsTable() {
  const queryClient = useQueryClient();
  const { findAllProfessors, deleteProfessor } = useProfessorsApi();
  const { isLoading, data, error } = useQuery<Professor[], Error>(
    'findAllProfessors',
    findAllProfessors
  );

  const handleOnDeleteSuccess = () => {
    queryClient.invalidateQueries('findAllProfessors');
  };

  if (error) {
    notify('error', error);
  }

  const columns = [
    { title: 'Full name', dataIndex: 'full_name', key: 'full_name' },
    { title: 'Email', dataIndex: 'email', key: 'email' },
    {
      title: 'Status',
      dataIndex: 'is_verified',
      key: 'is_verified',
      render: (is_verified: boolean) => {
        const color = is_verified ? 'geekblue' : 'volcano';
        const status = is_verified ? 'Verified' : 'Pending invite';
        return <Tag color={color}>{status}</Tag>;
      },
    },
    {
      title: 'Action',
      key: 'action',
      render: (_: unknown, record: Professor) => {
        return (
          <Space size="middle">
            <ProfessorEditForm professor={record} />
            <DeletePopconfirm
              onOk={() => deleteProfessor(record.id_)}
              onSuccess={handleOnDeleteSuccess}
            />
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
      rowKey="id_"
      showSorterTooltip
      sticky
    ></Table>
  );
}

export default ProfessorsTable;

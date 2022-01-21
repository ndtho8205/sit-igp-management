import { Space, Table } from 'antd';
import React from 'react';
import { useQuery, useQueryClient } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import { Presentation } from '../../../core/types/presentation';
import { notify } from '../../../core/utils';
import DeletePopconfirm from '../../common/DeletePopconfirm';
import PresentationEditForm from './PresentationEditForm';

function PresentationsTable() {
  const queryClient = useQueryClient();
  const { findAllPresentations, deletePresentation } = usePresentationsApi();
  const { isLoading, data, error } = useQuery<Presentation[], Error>(
    'findAllPresentations',
    () => findAllPresentations()
  );

  const handleOnDeleteSuccess = () => {
    queryClient.invalidateQueries('findAllPresentations');
  };

  if (error) {
    notify('error', error);
  }

  console.log(data);

  const columns = [
    {
      title: 'Student',
      dataIndex: ['student', 'full_name'],
      key: 'student_id.full_name',
    },
    {
      title: 'Presentation date',
      dataIndex: 'presentation_date',
      key: 'presentation_date',
    },
    {
      title: 'Presentation time',
      dataIndex: 'presentation_length',
      key: 'presentation_length',
    },
    {
      title: 'Session chair',
      dataIndex: ['session_chair', 'full_name'],
      key: 'session_chair.full_name',
    },
    {
      title: 'Reviewer 1',
      dataIndex: ['reviewer1', 'full_name'],
      key: 'reviewer1.full_name',
    },
    {
      title: 'Reviewer 2',
      dataIndex: ['reviewer2', 'full_name'],
      key: 'reviewer2.full_name',
    },
    {
      title: 'Reviewer 3',
      dataIndex: ['reviewer3', 'full_name'],
      key: 'reviewer3.full_name',
    },
    {
      title: 'Reviewer 4',
      dataIndex: ['reviewer4', 'full_name'],
      key: 'reviewer4.full_name',
    },

    {
      title: 'Action',
      key: 'action',
      render: (_: unknown, record: Presentation) => {
        return (
          <Space size="middle">
            <PresentationEditForm presentation={record} />
            <DeletePopconfirm
              onOk={() => deletePresentation(record.id_)}
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

export default PresentationsTable;

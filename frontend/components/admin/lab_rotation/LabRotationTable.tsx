import { Space, Table } from 'antd';
import React from 'react';
import { useQuery } from 'react-query';
import useSemesterEndEvaluationApi from '../../../core/api/useSemesterEndEvaluationApi';
import SemesterEndEvaluationSummary from '../../../core/types/semesterEndEvaluationSummary';
import { notify } from '../../../core/utils';
import LabRotationInputForm from './LabRotationInputForm';

const LabRotationTable = () => {
  const { getSummary } = useSemesterEndEvaluationApi();
  const summaryQuery = useQuery<SemesterEndEvaluationSummary[], Error>(
    'getSummary',
    getSummary
  );

  if (summaryQuery.error) {
    notify('error', summaryQuery.error);
  }

  const columns = [
    {
      title: 'Student',
      dataIndex: ['presentation', 'student', 'full_name'],
      key: 'full_name',
    },
    {
      title: 'Lab rotation',
      dataIndex: ['lab_rotation', 'course_score'],
      key: 'email',
    },
    {
      title: 'Action',
      key: 'action',
      render: (_: unknown, record: SemesterEndEvaluationSummary) => {
        return (
          <Space size="middle">
            <LabRotationInputForm summary={record} />
          </Space>
        );
      },
    },
  ];

  return (
    <Table
      dataSource={summaryQuery.data}
      columns={columns}
      loading={summaryQuery.isLoading}
      rowKey="id_"
      showSorterTooltip
      sticky
    ></Table>
  );
};

export default LabRotationTable;

import { Space, Table } from 'antd';
import { useQuery } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import { Presentation } from '../../../core/types/presentation';
import { notify } from '../../../core/utils';
import SemEndPresentationForm from './SemEndPresentationForm';

function SemEndPresentationTable({ page }) {
  const { findAllPresentations } = usePresentationsApi();

  const { isLoading, data, error } = useQuery<Presentation[], Error>(
    'findAllPresentations',
    findAllPresentations
  );

  if (error) {
    notify('error', error);
  }

  console.log(data);

  const viewColumns = [
    {
      title: 'Student Name',
      dataIndex: ['student', 'full_name'],
      key: 'student_name',
      width: '250px',
    },
    {
      title: 'Student ID',
      dataIndex: ['student', 'id_'],
      key: 'student_id',
      align: 'center',
      width: '110px',
    },
    {
      title: 'Research Objectives, Goals, and Plans',
      dataIndex: ['reviewer1_evaluation', 'score_research_goal'],
      key: 'score_research_goal',
      align: 'center',
      width: '170px',
      render: (text) => {
        return <>{text == 0 ? '--' : text}</>;
      },
    },
    {
      title: 'Delivery',
      dataIndex: ['reviewer1_evaluation', 'score_delivery'],
      key: 'score_delivery',
      align: 'center',
      width: '120px',
      render: (text) => {
        return <>{text == 0 ? '--' : text}</>;
      },
    },
    {
      title: 'Visual Aids',
      dataIndex: ['reviewer1_evaluation', 'score_visual_aid'],
      key: 'score_visual_aid',
      align: 'center',
      width: '120px',
      render: (text) => {
        return <>{text == 0 ? '--' : text}</>;
      },
    },
    {
      title: 'Time',
      dataIndex: ['reviewer1_evaluation', 'score_time'],
      key: 'score_time',
      align: 'center',
      width: '110px',
      render: (text) => {
        return <>{text == 0 ? '--' : text}</>;
      },
    },
    {
      title: 'Ability to answer Q&A',
      dataIndex: ['reviewer1_evaluation', 'score_qa_ability'],
      key: 'score_qa',
      align: 'center',
      width: '140px',
      render: (text) => {
        return <>{text == 0 ? '--' : text}</>;
      },
    },
    {
      title: 'Comment',
      dataIndex: ['reviewer1_evaluation', 'comment'],
      key: 'comment',
      width: '350px',
    },
  ];

  const inputColumns = [
    {
      title: 'Input',
      key: 'action',
      align: 'center',
      width: '90px',
      render: (text, record) => {
        return (
          <>
            <Space size="middle">
              <SemEndPresentationForm studentData={record} />
            </Space>
          </>
        );
      },
    },
    ...viewColumns,
  ];

  if (page == 'Input') {
    return (
      <Table
        dataSource={data}
        columns={inputColumns}
        // loading={isLoading}
        rowKey="id_"
        showSorterTooltip
        sticky
        scroll={{ x: '100%' }}
        bordered
      ></Table>
    );
  } else if (page == 'View') {
    return (
      <Table
        dataSource={data}
        columns={viewColumns}
        // loading={isLoading}
        rowKey="id_"
        showSorterTooltip
        sticky
        scroll={{ x: '100%' }}
        bordered
      ></Table>
    );
  }
}

export default SemEndPresentationTable;

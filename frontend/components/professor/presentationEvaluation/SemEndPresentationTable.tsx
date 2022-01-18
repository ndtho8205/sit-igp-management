import { Space, Table } from 'antd';
import SemEndPresentationForm from './SemEndPresentationForm';

function SemEndPresentationTable({ page }) {
  // const { isLoading, error, data } = useQuery('professors', () =>
  //   apiClient.get('/professors/').then((res) => res.data)
  // );

  // if (error) {
  //   notification['error']({
  //     key: 'Profile',
  //     message: 'Oops...',
  //     description: error.message,
  //   });
  // }

  const inputColumns = [
    {
      title: 'Student Name',
      dataIndex: 'student_name',
      key: 'student_name',
      width: '250px',
    },
    {
      title: 'Student ID',
      dataIndex: 'student_id',
      key: 'student_id',
      align: 'center',
      width: '110px',
    },
    {
      title: 'Research Objectives, Goals, and Plans',
      dataIndex: 'score_research_goal',
      key: 'score_research_goal',
      align: 'center',
      width: '170px',
    },
    {
      title: 'Delivery',
      dataIndex: 'score_delivery',
      key: 'score_delivery',
      align: 'center',
      width: '120px',
    },
    {
      title: 'Visual Aids',
      dataIndex: 'score_visual_aid',
      key: 'score_visual_aid',
      align: 'center',
      width: '120px',
    },
    {
      title: 'Time',
      dataIndex: 'score_time',
      key: 'score_time',
      align: 'center',
      width: '110px',
    },
    {
      title: 'Ability to answer Q&A',
      dataIndex: 'score_qa',
      key: 'score_qa',
      align: 'center',
      width: '140px',
    },
    {
      title: 'Comment',
      dataIndex: 'comment',
      key: 'comment',
      width: '300px',
      // render: (text, record) => (
      //   <div style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
      //     {text}
      //   </div>
      // ),
    },
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
  ];

  const viewColumns = [
    {
      title: 'Student Name',
      dataIndex: 'student_name',
      key: 'student_name',
      width: '250px',
    },
    {
      title: 'Student ID',
      dataIndex: 'student_id',
      key: 'student_id',
      align: 'center',
      width: '110px',
    },
    {
      title: 'Research Objectives, Goals, and Plans',
      dataIndex: 'score_research_goal',
      key: 'score_research_goal',
      align: 'center',
      width: '170px',
    },
    {
      title: 'Delivery',
      dataIndex: 'score_delivery',
      key: 'score_delivery',
      align: 'center',
      width: '120px',
    },
    {
      title: 'Visual Aids',
      dataIndex: 'score_visual_aid',
      key: 'score_visual_aid',
      align: 'center',
      width: '120px',
    },
    {
      title: 'Time',
      dataIndex: 'score_time',
      key: 'score_time',
      align: 'center',
      width: '110px',
    },
    {
      title: 'Ability to answer Q&A',
      dataIndex: 'score_qa',
      key: 'score_qa',
      align: 'center',
      width: '140px',
    },
    { title: 'Comment', dataIndex: 'comment', key: 'comment', width: '350px' },
  ];

  const testData = [
    {
      student_name: 'Tran Minh Chanh',
      student_id: 'NB20502',
      score_research_goal: 0,
      score_delivery: 0,
      score_visual_aid: 0,
      score_time: 0,
      score_qa: 0,
      comment: '',
    },
    {
      student_name: 'Nguyen Duc Tho',
      student_id: 'NB20501',
      score_research_goal: 3,
      score_delivery: 4,
      score_visual_aid: 1,
      score_time: 1,
      score_qa: 1,
      comment: 'Some comments',
    },
  ];

  if (page == 'Input') {
    return (
      <Table
        dataSource={testData}
        columns={inputColumns}
        // loading={isLoading}
        rowKey="professor_id"
        showSorterTooltip
        sticky
        scroll={{ x: '100%' }}
        bordered
      ></Table>
    );
  } else if (page == 'View') {
    return (
      <Table
        dataSource={testData}
        columns={viewColumns}
        // loading={isLoading}
        rowKey="professor_id"
        showSorterTooltip
        sticky
        scroll={{ x: '100%' }}
        bordered
      ></Table>
    );
  }
}

export default SemEndPresentationTable;

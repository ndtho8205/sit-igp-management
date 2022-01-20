import { Space, Table } from 'antd';
import SupervisorEvaluationForm from './SupervisorEvaluationForm';

function SupervisorEvaluationTable({ page }) {
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
      title:
        'Students can understand basic knowledge and skills for problem-finding and -solving in engineering.',
      children: [
        {
          title: 'Daily Activities',
          dataIndex: 'score_d1',
          key: 'score_d1',
          align: 'center',
          width: '170px',
        },
        {
          title: 'Presentation in Meeting',
          dataIndex: 'score_p1',
          key: 'score_p1',
          align: 'center',
          width: '170px',
        },
      ],
    },
    {
      title:
        'Students can work for a team organized by the laboratory members in solving social issues.',
      children: [
        {
          title: 'Daily Activities',
          dataIndex: 'score_d2',
          key: 'score_d2',
          align: 'center',
          width: '170px',
        },
        {
          title: 'Presentation in Meeting',
          dataIndex: 'score_p2',
          key: 'score_p2',
          align: 'center',
          width: '170px',
        },
      ],
    },
    {
      title: 'Input',
      key: 'action',
      align: 'center',
      width: '90px',
      render: (record) => {
        return (
          <>
          <Space size="middle">
            <SupervisorEvaluationForm studentData={record}/>
          </Space>
          </>
        );
      },
    },
  ];

  const testData = [
    {
      student_name: 'Tran Minh Chanh',
      student_id: 'NB20502',
      thesis_program: {
        score_d1: 0,
        score_p1: 0,
        score_d2: 0,
        score_p2: 0,
        score_course:0
      },
      lab_seminar: {
        score_d1: 0,
        score_p1: 0,
        score_d2: 0,
        score_p2: 0,
        score_course:0
      },
      score_presentation: 84.40,
      school_year: 11
    },
    {
      student_name: 'Nguyen Duc Tho',
      student_id: 'NB20501',
      thesis_program: {
        score_d1: 60,
        score_p1: 60,
        score_d2: 60,
        score_p2: 50,
        score_course:69.17
      },
      lab_seminar: {
        score_d1: 80,
        score_p1: 80,
        score_d2: 80,
        score_p2: 70,
        score_course: 84.17
      },
      score_presentation: 100,
      score_lab_rotation: 100,
      school_year: 21
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
  }
}

export default SupervisorEvaluationTable;

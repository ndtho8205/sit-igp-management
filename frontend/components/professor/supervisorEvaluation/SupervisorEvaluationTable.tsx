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
      title: 'Academic Year',
      dataIndex: 'student_year',
      key: 'student_yea',
      align: 'center',
      width: '150px',
    },
    {
      title: 'Thesis Program',
      dataIndex: ['thesis_program','score_course'],
      key: ['thesis_program','score_course'],
      align: 'center',
      render: (text) => {
        return (
          <>
            {(text == -1) ? "--" : text}
          </>
        );
      },
    },
    {
      title: 'Lab Seminar',
      dataIndex: ['lab_seminar','score_course'],
      key: ['lab_seminar','score_course'],
      align: 'center',
      render: (text) => {
        return (
          <>
            {(text == -1) ? "--" : text}
          </>
        );
      },
    },
  ];

  const testData = [
    {
      student_name: 'Tran Minh Chanh',
      student_id: 'NB20502',
      student_year: 'Freshmen 2',
      thesis_program: {
        score_d1: -1,
        score_p1: -1,
        score_d2: -1,
        score_p2: -1,
        score_course:-1
      },
      lab_seminar: {
        score_d1: -1,
        score_p1: -1,
        score_d2: -1,
        score_p2: -1,
        score_course: -1
      },
      score_presentation: 84.40,
      school_year: 11
    },
    {
      student_name: 'Nguyen Duc Tho',
      student_id: 'NB20501',
      student_year: 'Sophomore 1',
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

import { EditOutlined } from '@ant-design/icons';
import { notification, Space, Table } from 'antd';
import { useQuery } from 'react-query';
import apiClient from '../../../core/api/apiClient';
// import SemEndPresentationForm from './SemEndPresentationForm';

function SupervisorEvaluationTable({page}) {
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
    { title: 'Student Name', dataIndex: 'student_name', key: 'student_name', width: '250px' },
    { title: 'Student ID', dataIndex: 'student_id', key: 'student_id', align: 'center', width: '110px' },
    { 
      title: 'Students can understand basic knowledge and skills for problem-finding and -solving in engineering.',
      children: [
        {
          title: 'Daily Activities',
          dataIndex: 'score_d1',
          key: 'score_d1',
          align: 'center',
          width: '170px'
        },
        {
          title: 'Presentation in Meeting',
          dataIndex: 'score_p1',
          key: 'score_p1',
          align: 'center',
          width: '170px'
        }
      ]
    },
    { 
      title: 'Students can work for a team organized by the laboratory members in solving social issues.',
      children: [
        {
          title: 'Daily Activities',
          dataIndex: 'score_d2',
          key: 'score_d2',
          align: 'center',
          width: '170px'
        },
        {
          title: 'Presentation in Meeting',
          dataIndex: 'score_p2',
          key: 'score_p2',
          align: 'center',
          width: '170px'
        }
      ]
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
      // render: (text, record) => {
      //   return (
      //     <>
      //     <Space size="middle">
      //       <SemEndPresentationForm studentData={record}/>
      //     </Space>
      //     </>
      //   );
      // },
    },
  ];

  const testData = [
    {
      student_name: "Tran Minh Chanh",
      student_id: "NB20502",
      score_d1: 0,
      score_p1: 0,
      score_d2: 0,
      score_p2: 0,
      comment: ""
    },
    {
      student_name: "Nguyen Duc Tho",
      student_id: "NB20501",
      score_d1: 80,
      score_p1: 81,
      score_d2: 82,
      score_p2: 83,
      comment: "Some comments"
    }
  ]

  if(page == "Input") {
    return (
      <Table
        dataSource={testData}
        columns={inputColumns}
        // loading={isLoading}
        rowKey="professor_id"
        showSorterTooltip
        sticky
        scroll={{x:"100%"}}
        bordered
      ></Table>
    );
  }
}

export default SupervisorEvaluationTable;

import { Col, Row, Table } from "antd";
import { useQuery } from "react-query";
import useSemesterEndEvaluationApi from "../../../core/api/useSemesterEndEvaluationApi";
import SemesterEndEvaluationSummary from "../../../core/types/semesterEndEvaluationSummary";
import styles from '../../../styles/ProfessorPagesLayout.module.css';

function SummaryTable() {
  const { getSummary } = useSemesterEndEvaluationApi();
  const { isLoading, data, error } = useQuery<SemesterEndEvaluationSummary[], Error>(
    'getSummary',
    getSummary
  );

  function generateReviewerColumn(
    record : SemesterEndEvaluationSummary,
    reviewerNo : number
  ) {
    if(!record.presentation['reviewer'+reviewerNo])
      return "--"
    return (
      <>
        <Row>
          <Col span={19}>{"Prof. " + record.presentation['reviewer'+reviewerNo].full_name}</Col>
          <Col span={1}><p className={styles.supervisorEvaluationTableCell}>:</p></Col>
          <Col span={4}>
            <p className={styles.supervisorEvaluationTableCell}>{
            (record.presentation['reviewer'+reviewerNo+'_evaluation'])?
            record.presentation['reviewer'+reviewerNo+'_evaluation'].question_score :
            "--"
          }</p></Col>
        </Row>
      </>
    );
  }

  function generateAllReviewerColumns() {
    const columns = [];
    columns.push(
      {
        title: 'Presentation Time',
        dataIndex: ['presentation', 'presentation_length'],
        key: 'presentation_length',
        align: 'center',
        width: '150px',
      },
      {
        title: 'Session Chair',
        dataIndex: ['presentation', 'session_chair', 'full_name'],
        key: 'session_chair',
        align: 'center',
        width: '150px',
      },
    )
    for (let i = 1; i <= 4; ++i){
      columns.push({
        title: 'Reviewer ' + i,
        children: [
          {
            title: 'Reviewer Name',
            dataIndex: ['presentation', 'reviewer'+i,'full_name'],
            key: 'reviewer' + i + '_name',            
            align: 'center',
            width: '150px',
            render: (text: string) => {
              return (text === null) ? "" : "Prof. " + text;
            }
          },
          {
            title: 'Score',
            key: 'reviewer' + i + '_score',
            align: 'center',
            width: '80px',
            render: (record : SemesterEndEvaluationSummary) => {
              return (record.presentation['reviewer'+i+'_evaluation'])?
              record.presentation['reviewer'+i+'_evaluation'].question_score :
              "--";
            }
          }
        ]
      })
    }
    columns.push(
      {
        title: 'Average Score',
        key: 'score_presentation',
        align: 'center',
        width: '150px',
        render: (record : SemesterEndEvaluationSummary) => {
          for (let i = 1; i <= 4 ; ++i){
            let score_presentation = 0;
            if(!record.presentation['reviewer'+i+'_evaluation']){
              return "--";
            }
            else
              score_presentation+=record.presentation['reviewer'+i+'_evaluation'].question_score;
          }
          return Math.round((score_presentation/4) * 100) / 100;

        }
      }
    )
    return columns;
  }  

  const columns = [
    {
      title: 'Student Name',
      dataIndex: ['presentation','student','full_name'],
      key: 'student_name',
      width: '250px',
      fixed: 'left',
    },
    {
      title: 'Gender',
      dataIndex: ['presentation','student','gender'],
      key: 'student_gender',
      align: 'center',
      width: '100px',
      render: (text: string) => {
        return text.toUpperCase();
      }
    },
    {
      title: 'Area of Study',
      dataIndex: ['presentation','student','area_of_study'],
      key: 'student_gender',
      align: 'center',
      width: '200px',
    },
    {
      title: "Presentation Evaluation",
      children: generateAllReviewerColumns(),
    },
    {
      title: "Supervisor Evaluation",
      children: [
        {
          title: "Thesis Program",
          dataIndex: ['thesis_program','course_score'],
          key: 'thesis_program',
          align: 'center',
          width: '150px',
          render: (text : number) => {
            return (text === null) ? '--' : text;
          }
        },
        {
          title: "Lab Seminar",
          dataIndex: ['lab_seminar','course_score'],
          key: 'thesis_program',
          align: 'center',
          width: '150px',
          render: (text : number) => {
            return (text === null) ? '--' : text;
          }
        },
      ]
    }
  ]
  return(
    <Table
      dataSource={data}
      columns={columns}
      loading={isLoading}
      // rowKey="professor_id"
      showSorterTooltip
      sticky
      scroll={{ x: '100%' }}
      bordered
    ></Table>
  );
}

export default SummaryTable;
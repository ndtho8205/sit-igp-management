import { Table } from "antd";
import { useQuery } from "react-query";
import useSemesterEndEvaluationApi from "../../../core/api/useSemesterEndEvaluationApi";
import SemesterEndEvaluationSummary from "../../../core/types/semesterEndEvaluationSummary";
import styles from '../../../styles/ProfessorPagesLayout.module.css';

function SummaryTable() {
  const { getSummary } = useSemesterEndEvaluationApi();
  const { isLoading, data, error } = useQuery<
    SemesterEndEvaluationSummary[],
    Error
  >('getSummary', () => getSummary());

  function generateAllReviewerColumns() {
    const columns = [];
    columns.push({
      title: 'Presentation Average Score',
      key: 'score_presentation',
      align: 'center',
      width: '150px',
      className: styles.summaryTablePresentationAverageCol,
      render: (record: SemesterEndEvaluationSummary) => {
        let score_presentation = 0;
        for (let i = 1; i <= 4; ++i) {          
          if (!record.presentation['reviewer' + i + '_evaluation']) {
            return '--';
          } else
            score_presentation +=
              record.presentation['reviewer' + i + '_evaluation']
                .question_score;
        }
        return Math.round((score_presentation / 4) * 100) / 100;
      },
    });
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
        render: (text: string) => {
          return text === null ? '' : 'Prof. ' + text;
        },
      }
    );
    for (let i = 1; i <= 4; ++i) {
      columns.push({
        title: 'Reviewer ' + i,
        children: [
          {
            title: 'Reviewer Name',
            dataIndex: ['presentation', 'reviewer' + i, 'full_name'],
            key: 'reviewer' + i + '_name',
            align: 'center',
            width: '150px',
            render: (text: string) => {
              return text === null ? '' : 'Prof. ' + text;
            },
          },
          {
            title: 'Score',
            key: 'reviewer' + i + '_score',
            align: 'center',
            width: '80px',
            render: (record: SemesterEndEvaluationSummary) => {
              return record.presentation['reviewer' + i + '_evaluation']
                ? Math.round(record.presentation['reviewer' + i + '_evaluation'].question_score * 100) / 100
                : '--';
                //Math.round should be remove in later time.
            },
          },
        ],
      });
    }
    return columns;
  }

  const columns = [
    {
      title: 'Student Name',
      dataIndex: ['presentation', 'student', 'full_name'],
      key: 'student_name',
      width: '250px',
      fixed: 'left',
    },
    {
      title: 'Student ID',
      // dataIndex: ['student','id'],
      key: 'student_id',
      align: 'center',
      width: '110px',
      render: (record) => {
        if (record.presentation.student.email) {
          return record.presentation.student.email.split('@')[0].toUpperCase();
        }
      },
    },
    {
      title: 'Gender',
      dataIndex: ['presentation', 'student', 'gender'],
      key: 'student_gender',
      align: 'center',
      width: '100px',
    },
    {
      title: 'Area of Study',
      dataIndex: ['presentation', 'student', 'area_of_study'],
      key: 'student_gender',
      align: 'center',
      width: '200px',
    },
    {
      title: 'Supervisor Evaluation',
      children: [
        {
          title: 'Thesis Program',
          dataIndex: ['thesis_program', 'course_score'],
          key: 'thesis_program',
          align: 'center',
          width: '150px',
          className: styles.summaryTableThesisProgramCol,
          render: (text: number) => {
            return text === null ? '--' : Math.round(text);
          },
        },
        {
          title: 'Lab Seminar',
          dataIndex: ['lab_seminar', 'course_score'],
          key: 'thesis_program',
          align: 'center',
          width: '150px',
          className: styles.summaryTableLabSeminarCol,
          render: (text: number) => {
            return text === null ? '--' : Math.round(text);
          },
        },
      ],
    },
    {
      title: 'Presentation Evaluation',
      children: generateAllReviewerColumns(),
    },
  ];

  return (
    <Table
      dataSource={data}
      columns={columns}
      loading={isLoading}
      rowClassName={styles.summaryTableRow}
      pagination={false}
      // rowKey="professor_id"
      showSorterTooltip
      sticky
      scroll={{ x: '100%', y: '60vh'}}
      bordered
    ></Table>
  );
}

export default SummaryTable;

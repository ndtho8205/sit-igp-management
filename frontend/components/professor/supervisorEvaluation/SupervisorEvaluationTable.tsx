import { Col, Row, Table } from 'antd';
import { useQuery } from 'react-query';
import useSemesterEndEvaluationApi from '../../../core/api/useSemesterEndEvaluationApi';
import SchoolYear from '../../../core/types/schoolYear';
import SemesterEndEvaluationSummary from '../../../core/types/semesterEndEvaluationSummary';
import { getSchoolYear } from '../../../core/utils';
import LabSeminarForm from './LabSeminarForm';
import ThesisProgramForm from './ThesisProgramForm';
import styles from '../../../styles/ProfessorPagesLayout.module.css';


function SupervisorEvaluationTable() {
  const { getSummary } = useSemesterEndEvaluationApi();
  const { isLoading, data, error } = useQuery<SemesterEndEvaluationSummary[], Error>(
    'getSummary',
    getSummary
  );

  const inputColumns = [
    {
      title: 'Student Name',
      dataIndex: ['presentation','student','full_name'],
      key: 'student_name',
      width: '250px',
    },
    {
      title: 'Student ID',
      // dataIndex: ['student','id'],
      key: 'student_id',
      align: 'center',
      width: '110px',
      render: (record) =>{
        return record.presentation.student.email.split('@')[0].toUpperCase();
      }
    },
    {
      title: 'Academic Year',
      key: 'academic_year',
      align: 'center',
      width: '150px',
      render: (record) => {
        const schoolYear = getSchoolYear(
          record.presentation.student.admission_date,
          record.presentation.presentation_date
        );
        const schoolYearTexts = SchoolYear[schoolYear].split("_");
        return schoolYearTexts[0] + " " + schoolYearTexts[1];
      }
    },
    {
      title: 'Thesis Program',
      dataIndex: ['thesis_program', 'course_score'],
      key: 'thesis_program_course_score',
      align: 'center',
      render: (text, record) => {
        let score_presentation = 0
        for (let i = 1; i < 5; ++i){
          if(!record.presentation['reviewer'+i+'_evaluation']){
            // return "Not Ready";
            score_presentation+=100;
          }
          else
          score_presentation+=record.presentation['reviewer'+i+'_evaluation'].question_score;
        }
        return (
          <>
            <Row gutter={16}>
              <Col span={12} style={{textAlign: 'right'}}>
                <p className={styles.supervisorEvaluationTableCell}>{text === null ? '--' : text}</p>
              </Col>
              <Col span={12} style={{textAlign: 'left'}}>
                <ThesisProgramForm 
                  record={record} 
                  score_presentation={Math.round( (score_presentation/4)*100 )/100}
                />
              </Col>
            </Row>
          </>
        );
      },
    },
    {
      title: 'Lab Seminar',
      dataIndex: ['lab_seminar', 'course_score'],
      key: 'lab_seminar_course_score',
      align: 'center',
      render: (text, record) => {
        let score_presentation = 0
        for (let i = 1; i < 5; ++i){
          if(!record.presentation['reviewer'+i+'_evaluation']){
            // return "Not Ready";
            score_presentation+=100;
          }
          else
          score_presentation+=record.presentation['reviewer'+i+'_evaluation'].question_score;
        }
        return (
          <>
            <Row gutter={16}>
              <Col span={12} style={{textAlign: 'right'}}>
                <p className={styles.supervisorEvaluationTableCell}>{text === null ? '--' : text}</p>
              </Col>
              <Col span={12} style={{textAlign: 'left'}}>
                <LabSeminarForm 
                  record={record} 
                  score_presentation={Math.round( (score_presentation/4)*100 )/100}
                />
              </Col>
            </Row>
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
        score_daily_activities_1: -1,
        score_meeting_presentation_1: -1,
        score_daily_activities_2: -1,
        score_meeting_presentation_2: -1,
        course_score: -1,
      },
      lab_seminar: {
        score_daily_activities_1: -1,
        score_meeting_presentation_1: -1,
        score_daily_activities_2: -1,
        score_meeting_presentation_2: -1,
        course_score: -1,
      },
      score_presentation: 84.4,
      school_year: 11,
    },
    {
      student_name: 'Nguyen Duc Tho',
      student_id: 'NB20501',
      student_year: 'Sophomore 1',
      thesis_program: {
        score_daily_activities_1: 60,
        score_meeting_presentation_1: 60,
        score_daily_activities_2: 60,
        score_meeting_presentation_2: 50,
        course_score: 69.17,
      },
      lab_seminar: {
        score_daily_activities_1: 80,
        score_meeting_presentation_1: 80,
        score_daily_activities_2: 80,
        score_meeting_presentation_2: 70,
        course_score: 84.17,
      },
      score_presentation: 100,
      score_lab_rotation: 100,
      school_year: 21,
    },
  ];

  return (
    <Table
      dataSource={data}
      columns={inputColumns}
      loading={isLoading}
      // rowKey="professor_id"
      showSorterTooltip
      sticky
      scroll={{ x: '100%' }}
      bordered
    ></Table>
  );
}

export default SupervisorEvaluationTable;

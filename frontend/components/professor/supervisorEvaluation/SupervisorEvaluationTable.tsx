import { Col, Row, Table } from 'antd';
import moment from 'moment';
import { useQuery } from 'react-query';
import useProfessorsApi from '../../../core/api/useProfessorsApi';
import useSemesterEndEvaluationApi from '../../../core/api/useSemesterEndEvaluationApi';
import { Professor } from '../../../core/types/professor';
import SchoolYear from '../../../core/types/schoolYear';
import SemesterEndEvaluationSummary from '../../../core/types/semesterEndEvaluationSummary';
import { getSchoolYear } from '../../../core/utils';
import styles from '../../../styles/ProfessorPagesLayout.module.css';
import LabSeminarForm from './LabSeminarForm';
import ThesisProgramForm from './ThesisProgramForm';

const NUMBER_OF_REVIEWERS = 3;

function SupervisorEvaluationTable() {
  // get user id
  const { whoami } = useProfessorsApi();
  const whoamiQuery = useQuery<Professor, Error>('whoami', whoami);
  const userId = whoamiQuery.data?.id_;

  const { getSummary } = useSemesterEndEvaluationApi();
  const { isLoading, data, error } = useQuery<
    SemesterEndEvaluationSummary[],
    Error
  >(['getSummary', userId], () => getSummary(userId), {
    enabled: !!userId,
    select: (data) => 
      data
      .filter(_data => {
        let presentation_date = moment(_data.presentation.presentation_date);
        let date_now = moment(Date.now());
        if(Math.abs(date_now.diff(presentation_date, 'months')) <= 3){
          return true;
        }
        return false;
      })
  });

  const inputColumns = [
    {
      title: 'Student Name',
      dataIndex: ['presentation', 'student', 'full_name'],
      key: 'student_name',
      width: '250px',
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
      title: 'Academic Year',
      key: 'academic_year',
      align: 'center',
      width: '150px',
      render: (record) => {
        const schoolYear = getSchoolYear(
          record.presentation.student.admission_date,
          record.presentation.presentation_date
        );
        const schoolYearTexts = SchoolYear[schoolYear].split('_');
        return schoolYearTexts[0] + ' ' + schoolYearTexts[1];
      },
    },
    {
      title: 'Thesis Program',
      dataIndex: ['thesis_program', 'course_score'],
      key: 'thesis_program_course_score',
      align: 'center',
      render: (text, record) => {
        let score_presentation = 0;
        for (let i = 1; i <= NUMBER_OF_REVIEWERS; ++i) {
          if (!record.presentation['reviewer' + i + '_evaluation']) {
            return 'Cannot input at the moment';
            // score_presentation += 100;
          } else
            score_presentation +=
              record.presentation['reviewer' + i + '_evaluation']
                .question_score;
        }
        return (
          <>
            <Row gutter={16}>
              <Col span={12} style={{ textAlign: 'right' }}>
                <p className={styles.supervisorEvaluationTableCell}>
                  {text === null ? '--' : text}
                </p>
              </Col>
              <Col span={12} style={{ textAlign: 'left' }}>
                <ThesisProgramForm
                  record={record}
                  score_presentation={
                    Math.round((score_presentation / NUMBER_OF_REVIEWERS) * 100) / 100
                  }
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
        let score_presentation = 0;
        for (let i = 1; i <= NUMBER_OF_REVIEWERS; ++i) {
          if (!record.presentation['reviewer' + i + '_evaluation']) {
            return 'Cannot input at the moment';
            // score_presentation += 100;
          } else
            score_presentation +=
              record.presentation['reviewer' + i + '_evaluation']
                .question_score;
        }
        return (
          <>
            <Row gutter={16}>
              <Col span={12} style={{ textAlign: 'right' }}>
                <p className={styles.supervisorEvaluationTableCell}>
                  {text === null ? '--' : text}
                </p>
              </Col>
              <Col span={12} style={{ textAlign: 'left' }}>
                <LabSeminarForm
                  record={record}
                  score_presentation={
                    Math.round((score_presentation / NUMBER_OF_REVIEWERS) * 100) / 100
                  }
                />
              </Col>
            </Row>
          </>
        );
      },
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

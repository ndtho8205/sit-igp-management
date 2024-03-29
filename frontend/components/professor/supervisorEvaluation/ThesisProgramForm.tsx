import { EditOutlined } from '@ant-design/icons';
import { useQueryClient } from 'react-query';
import useSemesterEndEvaluationApi from '../../../core/api/useSemesterEndEvaluationApi';
import { Criteria } from '../../../core/data/supervisorEvaluationCriteria';
import SchoolYear from '../../../core/types/schoolYear';
import SemesterEndEvaluationSummary from '../../../core/types/semesterEndEvaluationSummary';
import Cell from '../../../core/types/supervisorEvaluation';
import ThesisProgramEvaluation from '../../../core/types/thesisProgramEvaluation';
import { getSchoolYear } from '../../../core/utils';
import ModalForm from '../../common/ModalForm';
import SupervisorEvaluationInput from './SupervisorEvaluationInput';

type SupervisorEvaluation = {
  record: SemesterEndEvaluationSummary;
  score_presentation: number;
};

const ThesisProgramForm = ({
  record,
  score_presentation,
}: SupervisorEvaluation) => {
  const queryClient = useQueryClient();
  const { createThesisProgramEvaluation, updateThesisProgramEvaluation } =
    useSemesterEndEvaluationApi();

  const schoolYear = getSchoolYear(
    record.presentation.student.admission_date,
    record.presentation.presentation_date,
    record.presentation.student.email.split('@')[0]
  );

  const schoolYearTexts = SchoolYear[schoolYear].split('_');

  function calculateCourseScore(obj: ThesisProgramEvaluation): number {
    const originalCourseScore =
      obj.score_daily_activities_1 * 0.35 +
      obj.score_daily_activities_2 * 0.35 +
      obj.score_meeting_presentation_1 * 0.1 +
      obj.score_meeting_presentation_2 * 0.1 +
      score_presentation * 0.1;
    if (Criteria[SchoolYear[schoolYear]].hasLabRotation) {
      return (
        Math.round(
          (originalCourseScore * (5 / 6) +
            record.lab_rotation.course_score * (1 / 6)) *
            100
        ) / 100
      );
    }
    return Math.round(originalCourseScore * 100) / 100;
  }

  function generateCriteriaRows(criteria: any[]) {
    const criteriaRows = [];
    for (const criterion of criteria) {
      const rowNo = criteria.indexOf(criterion) + 1;
      if (rowNo == 3) {
        criteriaRows.push([
          {
            type: Cell.Text,
            value: criterion,
          },
          {
            type: Cell.Blank,
          },
          {
            type: Cell.Blank,
          },
          {
            type: Cell.Text,
            value: score_presentation,
          },
        ]);
      } else {
        criteriaRows.push([
          {
            type: Cell.Text,
            value: criterion,
          },
          {
            type: Cell.FormItem,
            value: 'score_daily_activities_' + rowNo,
          },
          {
            type: Cell.FormItem,
            value: 'score_meeting_presentation_' + rowNo,
          },
          {
            type: Cell.Blank,
          },
        ]);
      }
    }
    return criteriaRows;
  }

  const handleOnOk = async (obj: ThesisProgramEvaluation) => {
    obj.course_score = calculateCourseScore(obj);
    if (record.thesis_program) {
      return await updateThesisProgramEvaluation(record.presentation.id_, obj);
    } else {
      return await createThesisProgramEvaluation(record.presentation.id_, obj);
    }
  };

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('getSummary');
  };

  return (
    <ModalForm
      buttonType="primary"
      title={
        record.presentation.student.full_name +
        ' - ' +
        record.presentation.student.email?.split('@')[0].toUpperCase()
      }
      okText="Input"
      buttonIcon={<EditOutlined />}
      onOk={handleOnOk}
      onSuccess={handleOnSuccess}
      width={'65%'}
      // initialValues={professor}
    >
      {schoolYearTexts[0] + ' Thesis Program ' + schoolYearTexts[1]}
      <SupervisorEvaluationInput
        record={record}
        criteria={generateCriteriaRows(Criteria[SchoolYear[schoolYear]].thesis)}
        score_presentation={score_presentation}
        typeOfTable={'thesis_program'}
      />
    </ModalForm>
  );
};

export default ThesisProgramForm;

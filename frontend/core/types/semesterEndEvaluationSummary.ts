import LabRotationEvaluation from './labRotationEvaluation';
import LabSeminarEvaluation from './labSeminarEvaluation';
import { Presentation } from './presentation';
import ThesisProgramEvaluation from './thesisProgramEvaluation';

type SemesterEndEvaluationSummary = {
  presentation: Presentation;
  thesis_program: ThesisProgramEvaluation | null;
  lab_seminar: LabSeminarEvaluation | null;
  lab_rotation: LabRotationEvaluation | null;
};

export default SemesterEndEvaluationSummary;

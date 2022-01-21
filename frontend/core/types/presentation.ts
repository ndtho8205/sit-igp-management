import { ProfessorBasics } from './professor';
import Student from './student';

type Presentation = {
  id_: string;

  student: Student;
  presentation_date: string;

  presentation_length?: string;

  session_chair: ProfessorBasics | null;
  reviewer1: ProfessorBasics | null;
  reviewer2: ProfessorBasics | null;
  reviewer3: ProfessorBasics | null;
  reviewer4: ProfessorBasics | null;

  reviewer1_evaluation: PresentationEvaluation | null;
  reviewer2_evaluation: PresentationEvaluation | null;
  reviewer3_evaluation: PresentationEvaluation | null;
  reviewer4_evaluation: PresentationEvaluation | null;
};

type PresentationEvaluation = {
  score_research_goal: number;
  score_delivery: number;
  score_visual_aid: number;
  score_time: number;
  score_qa_ability: number;
  comment: string;

  question_score: number;
};

type PresentationEvaluationGivenByUser = {
  presentation_id: string;
  reviewer_id: string;
  student: { full_name: string };
  evaluation: PresentationEvaluation | null;
};

export type {
  Presentation,
  PresentationEvaluation,
  PresentationEvaluationGivenByUser,
};

import { ProfessorBasics } from './professor';
import Student from './student';

type Presentation = {
  id_: string;

  student: Student;
  presentation_date: string;

  presentation_length?: string;

  session_chair?: ProfessorBasics;
  reviewer1?: ProfessorBasics;
  reviewer2?: ProfessorBasics;
  reviewer3?: ProfessorBasics;
  reviewer4?: ProfessorBasics;

  reviewer1_evaluation?: PresentationEvaluation;
  reviewer2_evaluation?: PresentationEvaluation;
  reviewer3_evaluation?: PresentationEvaluation;
  reviewer4_evaluation?: PresentationEvaluation;
};

type PresentationEvaluation = {
  id_: string;

  score_research_goal: number;
  score_delivery: number;
  score_visual_aid: number;
  score_time: number;
  score_qa_ability: number;
  comment: string;

  question_score: number;
};

export type { Presentation, PresentationEvaluation };

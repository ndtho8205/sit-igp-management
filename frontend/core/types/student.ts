import Gender from './gender';
import { ProfessorBasics } from './professor';

type Student = {
  id_: string;

  full_name: string;
  admission_date: string;

  email?: string;
  gender?: Gender;
  area_of_study?: string;

  supervisor?: ProfessorBasics;
  advisor1?: ProfessorBasics;
  advisor2?: ProfessorBasics;
};

export default Student;

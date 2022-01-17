import Gender from './gender';

type Student = {
  id_: string;
  full_name: string;
  email: string;
  gender: Gender;
  area_of_study: string;
  admission_date: string;

  supervisor_id: string;
  advisor1_id: string;
  advisor2_id: string;

  is_deleted: boolean;
};

export default Student;

type Professor = {
  id_: string;
  is_deleted: boolean;

  full_name: string;
  email: string;
  is_verified: boolean;
  is_superuser: boolean;
};

type ProfessorBasics = {
  id_: string;
  full_name: string;
  email: string;
};

export type { Professor, ProfessorBasics };

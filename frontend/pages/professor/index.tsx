import { ReactElement } from 'react';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const ProfessorHomePage = () => {
  return <h1>Welcome</h1>;
};

ProfessorHomePage.getLayout = function getLayout(page: ReactElement) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default ProfessorHomePage;

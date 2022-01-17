import { ReactElement } from 'react';
import SemEndPresentationTable from '../../../components/professor/semendpresentation/SemEndPresentationTable';
import SemEndPresentationRubric from '../../../components/professor/semendpresentation/SemEndPresentationRubric';
import ProfessorPagesLayout from '../../../layouts/ProfessorPagesLayout';

const SemEndPresentationInputScorePage = () => {
  return (
    <div>
      <h1>Semester End Presentation - Input</h1>
      {/* <NewButton title="New Professor">
        <ProfessorCreateForm />
      </NewButton>
      <ProfessorsTable /> */}
      {/* <SemEndPresentationForm studentData={null}/> */}
      <SemEndPresentationRubric/>
      <SemEndPresentationTable page="Input"/>
    </div>
  );
};

SemEndPresentationInputScorePage.getLayout = function getLayout(page: ReactElement) {
    return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
  };

export default SemEndPresentationInputScorePage;
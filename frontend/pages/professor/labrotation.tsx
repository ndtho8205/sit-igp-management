import { ReactElement } from 'react';
// import ProfessorCreateForm from '../../components/admin/professors/ProfessorCreateForm';
// import ProfessorsTable from '../../components/admin/professors/ProfessorsTable';
// import NewButton from '../../components/common/NewButton';
import ProfessorPagesLayout from '../../layouts/ProfessorPagesLayout';

const LabRotationPage = () => {
  return (
    <div>
      <h1>Lab Rotation</h1>
      {/* <NewButton title="New Professor">
        <ProfessorCreateForm />
      </NewButton>
      <ProfessorsTable /> */}
    </div>
  );
};

LabRotationPage.getLayout = function getLayout(page: ReactElement) {
  return <ProfessorPagesLayout>{page}</ProfessorPagesLayout>;
};

export default LabRotationPage;

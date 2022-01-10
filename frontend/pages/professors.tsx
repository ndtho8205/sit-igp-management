import type { NextPage } from "next";
import ProfessorsTable from "../components/professors/ProfessorsTable";

const Professors: NextPage = () => {
  return (
    <div>
      <h1>Professors</h1>
      <ProfessorsTable />
    </div>
  );
};

export default Professors;

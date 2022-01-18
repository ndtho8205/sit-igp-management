type Presentation = {
  id_: string;

  student_id: string;
  presentation_date: string;
  presentation_length: string;

  reviewer1_id: string;
  reviewer2_id: string;
  reviewer3_id: string;
  reviewer4_id: string;
  reviewer5_id: string;

  is_deleted: boolean;
};

export default Presentation;

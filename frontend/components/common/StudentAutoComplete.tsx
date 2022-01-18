import { AutoComplete } from 'antd';
import { useQuery } from 'react-query';
import useStudentsApi from '../../core/api/useStudentsApi';
import Student from '../../core/types/student';
import { notify } from '../../core/utils';

type Props = {
  value: string;
  onChange?: (value: string) => void;
};

const StudentAutoComplete = (props: Props) => {
  const { findAllStudents } = useStudentsApi();
  const { data, error } = useQuery<Student[], Error>(
    'findAllStudents',
    findAllStudents
  );

  if (error) {
    notify('error', error);
  }

  const handleOnSelect = (
    _: unknown,
    option: { key: string; value: string }
  ) => {
    props.onChange?.(option.key);
  };

  return (
    <AutoComplete onSelect={handleOnSelect}>
      {data?.map((student: Student) => (
        <AutoComplete.Option key={student.id_} value={student.full_name}>
          {student.full_name}
        </AutoComplete.Option>
      ))}
    </AutoComplete>
  );
};

export default StudentAutoComplete;

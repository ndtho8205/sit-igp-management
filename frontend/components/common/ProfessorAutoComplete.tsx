import { AutoComplete } from 'antd';
import { useQuery } from 'react-query';
import useProfessorsApi from '../../core/api/useProfessorsApi';
import Professor from '../../core/types/professor';
import { notify } from '../../core/utils';

type Props = {
  onChange?: (value: string) => void;
};

const ProfessorAutoComplete = (props: Props) => {
  const { findAllProfessors } = useProfessorsApi();
  const { data, error } = useQuery<Professor[], Error>(
    'findAllProfessors',
    findAllProfessors
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
      {data?.map((professor: Professor) => (
        <AutoComplete.Option key={professor.id_} value={professor.full_name}>
          {professor.full_name}
        </AutoComplete.Option>
      ))}
    </AutoComplete>
  );
};

export default ProfessorAutoComplete;

import { DeleteOutlined } from '@ant-design/icons';
import { Button, Popconfirm } from 'antd';
import { AxiosError } from 'axios';
import { useMutation } from 'react-query';
import { notify } from '../../core/utils';

type Props = {
  onOk: () => Promise<void>;
  onSuccess: () => void;
};

const DeletePopconfirm = (props: Props) => {
  const submitMutation = useMutation(props.onOk, {
    onSuccess: () => {
      notify('success', 'Delete success!');
      props.onSuccess();
    },
    onError: (error: Error | AxiosError) => {
      notify('error', error);
    },
  });

  const handleDelete = async () => {
    submitMutation.mutate();
  };

  return (
    <Popconfirm
      title="Sure to Delete?"
      okButtonProps={{ loading: submitMutation.isLoading }}
      onConfirm={handleDelete}
    >
      <Button danger icon={<DeleteOutlined />} />
    </Popconfirm>
  );
};

export default DeletePopconfirm;

/*


*/

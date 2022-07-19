import { PlusOutlined } from '@ant-design/icons';
import { Button, Form, Modal} from 'antd';
// import Modal from 'antd/lib/modal/Modal';
import { AxiosError } from 'axios';
import { CSSProperties, ReactNode, useState } from 'react';
import { useMutation } from 'react-query';
import { notify } from '../../core/utils';

type Props<T> = {
  title: string;
  children: ReactNode;
  initialValues?: T;
  okText: string;
  buttonType?: 'primary' | 'default';
  buttonShape?: 'circle' | 'default';
  buttonIcon?: ReactNode;
  width?: number | string;
  bodyStyle?: CSSProperties;
  modalLayout?: object;
  formLayout?: object;
  onOk: (data: T) => Promise<T>;
  onSuccess: () => void;
  confirmText?: string;
  needConfirm?: boolean;
};

const ModalForm = <T,>(props: Props<T>) => {
  const [isFormVisible, setFormVisible] = useState(false);
  const [form] = Form.useForm();

  const { confirm } = Modal;

  const submitMutation = useMutation(props.onOk, {
    onSuccess: () => {
      // form.resetFields();
      setFormVisible(false);
      notify('success', `${props.okText} success!`);
      props.onSuccess();
    },
    onError: (error: Error | AxiosError) => {
      notify('error', error);
    },
  });

  const showForm = () => {
    setFormVisible(true);
  };

  const handleConfirm = async () => {
    let values: T;
    try {
      values = await form.validateFields();
    } catch {
      return;
    }
    submitMutation.mutate(values);
  };

  const handleSubmit = () => {
    confirm({
      title: "Confirmation",
      content: props.confirmText !== undefined ? props.confirmText : "Are you sure?",
      onOk() {
        handleConfirm()
      },
      okText: "Yes",
      cancelText: "No",

    });
  };

  const handleCancel = () => {
    // form.resetFields();
    setFormVisible(false);
  };

  const handleAfterClose = () => {
    form.resetFields();
  };

  return (
    <>
      <Button
        type={props.buttonType || 'default'}
        shape={props.buttonShape || 'default'}
        onClick={showForm}
        icon={props.buttonIcon || <PlusOutlined />}
      />

      <Modal
        visible={isFormVisible}
        title={props.title}
        okText={props.okText}
        cancelText="Cancel"
        confirmLoading={submitMutation.isLoading}
        onOk={
          (props.needConfirm === undefined ||
            props.needConfirm === false)?
           handleConfirm : handleSubmit
        }
        onCancel={handleCancel}
        afterClose={handleAfterClose}
        destroyOnClose={true}
        width={props.width}
        bodyStyle={props.bodyStyle}
        {...props.modalLayout}
      >
        <Form
          form={form}
          layout="vertical"
          name="form_in_modal"
          labelWrap
          initialValues={props.initialValues}
          {...props.formLayout}
        >
          {props.children}
        </Form>
      </Modal>
    </>
  );
};

export default ModalForm;

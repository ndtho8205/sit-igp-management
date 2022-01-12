import { PlusOutlined } from '@ant-design/icons';
import { Button, Modal } from 'antd';
import React, { ReactNode, useState } from 'react';

type Props = {
  title: string;
  children: ReactNode;
};

const NewButton = ({ title, children }: Props) => {
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const showModal = () => {
    setIsModalVisible(true);
  };

  const onHandleCreate = () => {
    setIsLoading(true);
    setTimeout(() => {
      setIsModalVisible(false);
      setIsLoading(false);
    });
  };

  const onHandleCancel = () => {
    setIsModalVisible(false);
  };

  return (
    <>
      <Button type="primary" onClick={showModal}>
        <PlusOutlined />
      </Button>
      <Modal
        title={title}
        visible={isModalVisible}
        confirmLoading={isLoading}
        onOk={onHandleCreate}
        onCancel={onHandleCancel}
      >
        {children}
      </Modal>
    </>
  );
};

export default NewButton;

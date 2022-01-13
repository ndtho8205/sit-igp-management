import { PlusOutlined } from '@ant-design/icons';
import { Button, Form, Input, message } from 'antd';
import Modal from 'antd/lib/modal/Modal';
import { useState } from 'react';
import apiClient from '../../../core/api/apiClient';

type ProfessorCreateValues = {
  fullName: string;
  email: string;
};

const ProfessorCreateForm = () => {
  const [isFormVisible, setFormVisible] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [form] = Form.useForm();

  const showForm = () => {
    setFormVisible(true);
  };

  const handleCreate = () => {
    form
      .validateFields()
      .then((values: ProfessorCreateValues) => {
        setIsLoading(true);
        apiClient
          .post('/professors/', values)
          .then((res) => {
            message.success('Create success!');
            setIsLoading(false);
            form.resetFields();
            setFormVisible(false);
          })
          .catch((error) => {
            console.log(error);
          });
      })
      .catch((info) => {
        console.log('validate failed: ', info);
      });
  };

  const handleCancel = () => {
    setFormVisible(false);
  };

  return (
    <>
      <Button
        type="primary"
        shape="circle"
        onClick={showForm}
        icon={<PlusOutlined />}
      />

      <Modal
        visible={isFormVisible}
        title="New Professor"
        okText="Create"
        cancelText="Cancel"
        confirmLoading={isLoading}
        onOk={handleCreate}
        onCancel={handleCancel}
      >
        <Form
          form={form}
          layout="vertical"
          name="form_in_modal"
          initialValues={{ modifier: 'public' }}
        >
          <Form.Item
            label="Full name"
            name="full_name"
            rules={[{ required: true, message: 'Full name is required' }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Email"
            name="email"
            rules={[{ required: true, message: 'Email is required' }]}
          >
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default ProfessorCreateForm;

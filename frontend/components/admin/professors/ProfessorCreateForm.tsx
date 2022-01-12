import { Form, Input } from 'antd';
import { FunctionComponent } from 'react';

const ProfessorCreateForm: FunctionComponent = () => {
  const onFinish = (values) => {
    console.log('Success: ', values);
  };

  const onFinishFailed = (error) => {
    console.log('Failed: ', error);
  };

  return (
    <Form
      name="basic"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="on"
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
  );
};

export default ProfessorCreateForm;

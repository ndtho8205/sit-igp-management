import { EditOutlined, QuestionCircleOutlined } from '@ant-design/icons';
import { Button, Form, Input, message, Slider, Table, Popover, Row, Col } from 'antd';
import Modal from 'antd/lib/modal/Modal';
import React, { useState } from 'react';
import apiClient from '../../../core/api/apiClient';
import semEndRubric from '../../../core/semEndRubric';
import styles from '../../../styles/ProfessorPagesLayout.module.css'

type ProfessorCreateValues = {
  score_research_goal: number;
  score_delivery: number;
  score_visual_aid: number;
  score_time: number;
  score_qa: number;
};

class ScoreInput extends React.Component{
  state = {
    inputValue: this.props.scoreData,
  };

  onChange = value => {
    this.setState({
      inputValue: value,
    });
  };

  marks = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5'
  };

  formItemTipFormatter(value) {
    let marksTip = {
      1: 'Poor',
      2: 'Weak',
      3: 'Average',
      4: 'Good',
      5: 'Excellent'
    };
    return marksTip[value];
  };

  render() {
    const { inputValue } = this.state;
    return (
      <Row gutter={10}>
        <Col span={3}>
          <span className={styles.scoreInputDescription}>
            {inputValue ? this.formItemTipFormatter(inputValue): "Not yet rated."}
          </span>
        </Col>
        <Col span={21}>
          <Slider 
            marks={this.marks} 
            step={1} 
            max={5} 
            min={0} 
            tipFormatter={this.formItemTipFormatter}
            onChange={this.onChange}
            value={typeof inputValue === 'number' ? inputValue : 0}
          />
        </Col>
      </Row>
    );
  }
  
}

const SemEndPresentationForm = ({studentData}) => {
  const [isFormVisible, setFormVisible] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [form] = Form.useForm();

  const showForm = () => {
    setFormVisible(true);
    console.log(studentData);
    console.log("ahihi" + studentData.student_name)
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

  const marksTip = {
    1: 'Poor',
    2: 'Weak',
    3: 'Average',
    4: 'Good',
    5: 'Excellent'
  }

  function formItemTipFormatter(value) {
    return marksTip[value];
  }

  const columns = [
    // { title: 'Criteria', dataIndex: 'criteria', key: 'criteria' },
    { title: 'Weight', dataIndex: 'weight', key: 'weight' },
    { title: '1: Poor', dataIndex: 'poor', key: 'poor' },
    { title: '2: Weak', dataIndex: 'weak', key: 'weak' },
    { title: '3: Average', dataIndex: 'average', key: 'average' },
    { title: '4: Good', dataIndex: 'good', key: 'good' },
    { title: '5: Excellent', dataIndex: 'excellent', key: 'excellent' },
  ];

  const formItemLayout = {
    labelCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 6,
      },
    },
    wrapperCol: {
      xs: {
        span: 24,
      },
      sm: {
        span: 18,
      },
    },
  };

  const validateMessages = {
    required: '"${label}" score is required!',
    number: {
      range: '"${label}" score must be between ${min} and ${max}',
    },
  };

  function insertFormItems() {
    const items = [];
    for (const criterion of semEndRubric){
      items.push(
        <Form.Item
          label={
            <>
              {criterion.criteria}
              <Popover 
              content={<Table dataSource={[criterion]} columns={columns} pagination={{ position: ['none','none'] }} bordered></Table>}
              title={criterion.criteria}
              placement="bottomLeft"
              trigger={"click"}
              overlayStyle={{
                width: "55%"
              }}>
              <QuestionCircleOutlined style={{fontSize:'1.5em' ,paddingLeft:'6px'}}/>
              </Popover>
            </>
          }
          name={criterion.key}
          rules={[
            { required: true},
            { type: 'number', min: 1, max: 5 }
          ]}
          initialValue={studentData[criterion.key]}
          // initialValue={0}
        >
          {/* <Slider marks={marks} step={1} max={5} min={1} tipFormatter={formItemTipFormatter}/> */}
          <ScoreInput scoreData={studentData[criterion.key]}/>
        </Form.Item>
      );
    }
    return items;
  }

  return (
    <>
      <Button
        type="primary"
        shape="circle"
        onClick={showForm}
        icon={<EditOutlined />}
      />

      <Modal
        visible={isFormVisible}
        title={
          studentData.student_name + " - " + studentData.student_id
        }
        okText="Input"
        cancelText="Cancel"
        confirmLoading={isLoading}
        onOk={handleCreate}
        onCancel={handleCancel}
        width={"65%"}
      >
        <Form
          {...formItemLayout}
          form={form}
          layout="horizontal"
          name="form_in_modal"
          labelWrap
          initialValues={{ modifier: 'public' }}
          validateMessages={validateMessages}
          requiredMark={false}
        >
          {insertFormItems()}

          <Form.Item
            label="Comment (Optional)"
            name="comment"
            initialValue={studentData.comment}
          >
            <Input.TextArea 
              autoSize={{minRows: 5, maxRows: 5}} 
              // maxLength={500} 
              // showCount={true}
            />
          </Form.Item>

        </Form>
      </Modal>
    </>
  );
};

export default SemEndPresentationForm;

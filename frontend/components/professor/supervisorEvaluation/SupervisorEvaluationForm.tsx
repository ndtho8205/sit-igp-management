import { EditOutlined, QuestionCircleOutlined } from '@ant-design/icons';
import {
  Button,
  Col,
  Form,
  Input,
  InputNumber,
  message,
  Popover,
  Row,
  Slider,
  Table,
} from 'antd';
import Modal from 'antd/lib/modal/Modal';
import React, { useState } from 'react';
import styles from '../../../styles/ProfessorPagesLayout.module.css';
import Cell from '../../../core/types/supervisorEvaluation';
import {Header, Criteria} from '../../../core/data/supervisorEvaluationCriteria';
import SchoolYear from '../../../core/types/schoolYear';

type ProfessorCreateValues = {
  score_research_goal: number;
  score_delivery: number;
  score_visual_aid: number;
  score_time: number;
  score_qa: number;
};

const SupervisorEvaluationForm = ({ studentData }) => {
  const [isFormVisible, setFormVisible] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [form] = Form.useForm();

  const showForm = () => {
    setFormVisible(true);
    // console.log(studentData);
    // console.log('ahihi' + studentData.student_name);
  };

  const handleCreate = async () => {
    form
      .validateFields()
      .then((values: ProfessorCreateValues) => {
        setIsLoading(true);
        apiClient
          ?.post('/professors/', values)
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

  const validateMessages = {
    required: '"${label}" score is required!',
    number: {
      range: '"${label}" score must be between ${min} and ${max}',
    },
  };

  function generateCell(cellItem: any){
    if(cellItem.type == Cell.Blank){
      return (<p className={styles.supervisorEvaluationFormGreyOutCell}></p>);
    }
    else if (cellItem.type == Cell.Text){
      return (
        <p className={styles.supervisorEvaluationFormCell}>
          {cellItem.value}
        </p>
      );
    }
    else if (cellItem.type == Cell.FormItem){
      return (
        <p className={styles.supervisorEvaluationFormCell}>
          <Form.Item
            name={cellItem.value}
            initialValue={studentData[cellItem.value]}
            style={{margin: 0}}
          >
            <InputNumber 
              min={0} 
              max={100} 
              size='large'
              controls={false}
              style={{ width:'100%' }}
            />
          </Form.Item>
        </p>
      );
    }
    else {
      return null;
    }
  }

  function generateRow(
    rowCells: any,
    noOfCol: number,
  ){
    const row = [];
    for (const item of rowCells) {
      if(rowCells.indexOf(item) >= noOfCol){
        break;
      }
      row.push(
        <Col 
          span={rowCells.indexOf(item)==0 ? 24 - (Math.floor(24/noOfCol)*(noOfCol-1)): Math.floor(24/noOfCol)} 
          style={{border:"1px solid black"}}
        >
          {generateCell(item)}
        </Col>
      );
    }
    return row;
  }
  
  function generateForm(
    criteria: any
  ){
    const noOfCol = (studentData.school_year == SchoolYear.Freshmen_1) ? 4 : 
                    (studentData.school_year == SchoolYear.Freshmen_2) ? 4 : 5;
    return (
      <>
        <Form
          form={form}
          layout="horizontal"
          name="form_in_modal"
          labelWrap
          initialValues={{ modifier: 'public' }}
          validateMessages={validateMessages}
          requiredMark={false}
          style={{border: "1px solid black"}}
        >
          <Row>
            {
              (() => {                
                if (noOfCol < 5){
                  const rows = [];
                  rows.push(generateRow(Header,noOfCol));
                  for (const criterion of criteria) {
                    rows.push(generateRow(criterion,noOfCol));
                  }
                  return rows;
                }
                else {
                  return(
                    <>
                      <Col span={20}>
                        <Row>
                          {generateRow(Header,noOfCol - 1)}
                        </Row>
                      </Col>
                      <Col span={4} style={{border:"1px solid black"}}>
                        {generateCell(Header[Header.length - 1])}
                      </Col>
                      
                      <Col span={20}>
                        <Row>                        
                          {(() => {
                            const rows = [];
                            for (const criterion of criteria) {
                              rows.push(generateRow(criterion, noOfCol - 1));
                            }
                            return rows;
                          })()}
                        </Row>
                      </Col>
                      <Col span={4} style={{border:"1px solid black"}}>
                        {generateCell({type: Cell.Text, value: studentData.score_lab_rotation})}
                      </Col>
                    </>
                  );
                }
              })()
            }
          </Row>
        </Form>
        
      </>
    );
  }

  function generateCriteriaRows(
    criteria: any []
  ){
    const criteriaRows = [];
    for (const criterion of criteria)
    {
      const rowNo = criteria.indexOf(criterion) + 1;
      if(rowNo == 3){
        criteriaRows.push(
          [
            {
              type: Cell.Text,
              value: criterion,
            },
            {
              type: Cell.Blank
            },
            {
              type: Cell.Blank
            },
            {
              type: Cell.Text,
              value: studentData.score_presentation
            }
          ]
        );
      }
      else {
        criteriaRows.push(
          [
            {
              type: Cell.Text,
              value: criterion,
            },
            {
              type: Cell.FormItem,
              value: "score_d" + rowNo
            },
            {
              type: Cell.FormItem,
              value: "score_p" + rowNo
            },
            {
              type: Cell.Blank
            }
          ]
        );
      }
    }
    return criteriaRows;
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
        title={studentData.student_name + ' - ' + studentData.student_id}
        okText="Input"
        cancelText="Cancel"
        confirmLoading={isLoading}
        onOk={handleCreate}
        onCancel={handleCancel}
        width={'65%'}
        bodyStyle={{height: '70vh',overflowY: "scroll"}}
      >
        Thesis Program
        {generateForm(generateCriteriaRows(Criteria[0].criteria.thesis))}
        <br/>
        Lab Seminar
        {generateForm(generateCriteriaRows(Criteria[0].criteria.labSeminar))}
      </Modal>
    </>
  );
};

export default SupervisorEvaluationForm;

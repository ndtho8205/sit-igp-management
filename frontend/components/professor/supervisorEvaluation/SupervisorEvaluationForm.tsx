import { EditOutlined, QuestionCircleOutlined } from '@ant-design/icons';
import {
  Button,
  Col,
  Form,
  FormInstance,
  InputNumber,
  message,
  Row,
} from 'antd';
import Modal from 'antd/lib/modal/Modal';
import React, { useState } from 'react';
import styles from '../../../styles/ProfessorPagesLayout.module.css';
import Cell from '../../../core/types/supervisorEvaluation';
import {
  Header,
  Criteria,
} from '../../../core/data/supervisorEvaluationCriteria';
import SchoolYear from '../../../core/types/schoolYear';

type ProfessorCreateValues = {
  score_research_goal: number;
  score_delivery: number;
  score_visual_aid: number;
  score_time: number;
  score_qa: number;
};

// let formThesis : FormInstance<any>
// let formLabSeminar : FormInstance<any>

class ScoreInput extends React.Component<any, any> {
  hasLabRotation: boolean;
  constructor(props: {
    scoreData: any;
    criteria: any;
    isThesis: boolean;
    form: FormInstance;
  }) {
    super(props);
    this.state = {
      score_d1: props.scoreData[
        props.isThesis ? 'thesis_program' : 'lab_seminar'
      ].score_d1 as number,
      score_p1: props.scoreData[
        props.isThesis ? 'thesis_program' : 'lab_seminar'
      ].score_p1 as number,
      score_d2: props.scoreData[
        props.isThesis ? 'thesis_program' : 'lab_seminar'
      ].score_d2 as number,
      score_p2: props.scoreData[
        props.isThesis ? 'thesis_program' : 'lab_seminar'
      ].score_p2 as number,
      score_course: props.scoreData[
        props.isThesis ? 'thesis_program' : 'lab_seminar'
      ].score_course as number,
    };
    this.hasLabRotation =
      props.scoreData.school_year == SchoolYear.Freshmen_1
        ? false
        : props.scoreData.school_year == SchoolYear.Freshmen_2
        ? false
        : true;
  }

  calculateCourseScore = () => {
    setTimeout(function (this: ScoreInput) {
      let score_course;
      if (this.props.isThesis) {
        score_course =
          Math.round(this.calculateThesisCourseScore() * 100) / 100;
      } else {
        score_course =
          Math.round(this.calculateLabSeminarCourseScore() * 100) / 100;
      }
      this.setState({
        score_course: score_course,
      });
      // if(this.props.isThesis) {
      //   formThesis.setFieldsValue({score_course: score_course});
      // }
      // else{
      //   formLabSeminar.setFieldsValue({score_course: score_course});
      // }
      this.props.form.setFieldsValue({ score_course: score_course });
    }, 1000);
    return null;
  };

  calculateThesisCourseScore = (): number => {
    const { score_d1, score_d2, score_p1, score_p2 } = this.state;
    const originalCourseScore =
      score_d1 * 0.35 +
      score_d2 * 0.35 +
      score_p1 * 0.1 +
      score_p2 * 0.1 +
      this.props.scoreData.score_presentation * 0.1;
    if (this.hasLabRotation) {
      return (
        originalCourseScore * (5 / 6) +
        this.props.scoreData.score_lab_rotation * (1 / 6)
      );
    } else {
      return originalCourseScore;
    }
  };

  calculateLabSeminarCourseScore = () => {
    const { score_d1, score_d2, score_p1, score_p2 } = this.state;
    const originalCourseScore =
      score_d1 * 0.35 +
      score_d2 * 0.15 +
      score_p1 * 0.3 +
      score_p2 * 0.1 +
      this.props.scoreData.score_presentation * 0.1;
    if (this.hasLabRotation) {
      return (
        originalCourseScore * 0.5 +
        this.props.scoreData.score_lab_rotation * 0.5
      );
    } else {
      return originalCourseScore;
    }
  };

  getOnChange = (score: string) => {
    switch (score) {
      case 'score_d1':
        return this.onD1Change;
      case 'score_d2':
        return this.onD2Change;
      case 'score_p1':
        return this.onP1Change;
      case 'score_p2':
        return this.onP2Change;
      default:
        return undefined;
    }
  };
  onD1Change = (value: number) => {
    this.setState({
      score_d1: value,
    });
    this.calculateCourseScore();
  };

  onD2Change = (value: number) => {
    this.setState({
      score_d2: value,
    });
    this.calculateCourseScore();
  };

  onP1Change = (value: number) => {
    this.setState({
      score_p1: value,
    });
    this.calculateCourseScore();
  };

  onP2Change = (value: number) => {
    this.setState({
      score_p2: value,
    });
    this.calculateCourseScore();
  };

  generateCell = (cellItem: any) => {
    if (cellItem.type == Cell.Blank) {
      return <p className={styles.supervisorEvaluationFormGreyOutCell}></p>;
    } else if (cellItem.type == Cell.Text) {
      return (
        <p className={styles.supervisorEvaluationFormCell}>{cellItem.value}</p>
      );
    } else if (cellItem.type == Cell.FormItem) {
      return (
        <p className={styles.supervisorEvaluationFormCell}>
          <Form.Item
            label={cellItem.label}
            name={cellItem.value}
            initialValue={
              this.props.scoreData[
                this.props.isThesis ? 'thesis_program' : 'lab_seminar'
              ][cellItem.value]
            }
            style={{ margin: 0 }}
          >
            <InputNumber
              min={0}
              max={100}
              size="large"
              controls={false}
              style={{ width: '100%' }}
              onChange={this.getOnChange(cellItem.value)}
              value={this.state[cellItem.value]}
              disabled={cellItem.disabled}
            />
          </Form.Item>
        </p>
      );
    } else {
      return undefined;
    }
  };

  generateRow = (rowCells: any, noOfCol: number) => {
    const row = [];
    for (const item of rowCells) {
      if (rowCells.indexOf(item) >= noOfCol) {
        break;
      }
      row.push(
        <Col
          span={
            rowCells.indexOf(item) == 0
              ? 24 - Math.floor(24 / noOfCol) * (noOfCol - 1)
              : Math.floor(24 / noOfCol)
          }
          style={{ border: '1px solid black' }}
        >
          {this.generateCell(item)}
        </Col>
      );
    }
    return row;
  };

  render() {
    const noOfCol = this.hasLabRotation ? 5 : 4;

    return (
      <>
        <Row>
          {(() => {
            if (noOfCol < 5) {
              const rows = [];
              rows.push(this.generateRow(Header, noOfCol));
              for (const criterion of this.props.criteria) {
                rows.push(this.generateRow(criterion, noOfCol));
              }
              rows.push(
                <Col span={24} style={{ border: '1px solid black' }}>
                  {this.generateCell({
                    type: Cell.FormItem,
                    value: 'score_course',
                    disabled: true,
                    label: 'Course Score',
                  })}
                </Col>
              );
              return rows;
            } else {
              return (
                <>
                  <Col span={20}>
                    <Row>{this.generateRow(Header, noOfCol - 1)}</Row>
                  </Col>
                  <Col span={4} style={{ border: '1px solid black' }}>
                    {this.generateCell(Header[Header.length - 1])}
                  </Col>

                  <Col span={20}>
                    <Row>
                      {(() => {
                        const rows = [];
                        for (const criterion of this.props.criteria) {
                          rows.push(this.generateRow(criterion, noOfCol - 1));
                        }
                        return rows;
                      })()}
                    </Row>
                  </Col>
                  <Col span={4} style={{ border: '1px solid black' }}>
                    {this.generateCell({
                      type: Cell.Text,
                      value: this.props.scoreData.score_lab_rotation,
                    })}
                  </Col>

                  <Col span={24} style={{ border: '1px solid black' }}>
                    {this.generateCell({
                      type: Cell.FormItem,
                      value: 'score_course',
                      disabled: true,
                      label: 'Course Score',
                    })}
                  </Col>
                </>
              );
            }
          })()}
          {this.calculateCourseScore()}
        </Row>
      </>
    );
  }
}

const SupervisorEvaluationForm = ({ studentData }) => {
  const [isFormVisible, setFormVisible] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [formThesis] = Form.useForm();
  const [formLabSeminar] = Form.useForm();
  const showForm = () => {
    setFormVisible(true);
  };

  const handleCreate = async () => {
    formThesis
      .validateFields()
      .then((values: ProfessorCreateValues) => {
        setIsLoading(true);
        apiClient
          ?.post('/professors/', values)
          .then((res) => {
            message.success('Create success!');
            setIsLoading(false);
            Form.resetFields();
            setFormVisible(false);
          })
          .catch((error) => {
            console.log(error);
          });
      })
      .catch((info) => {
        console.log('validate failed: ', info);
      });

    formLabSeminar
      .validateFields()
      .then((values: ProfessorCreateValues) => {
        setIsLoading(true);
        apiClient
          ?.post('/professors/', values)
          .then((res) => {
            message.success('Create success!');
            setIsLoading(false);
            Form.resetFields();
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

  function generateForm(criteria: any, isThesis: boolean, form: FormInstance) {
    return (
      <>
        <Form
          form={isThesis ? formThesis : formLabSeminar}
          layout="horizontal"
          name="form_in_modal"
          labelWrap
          initialValues={{ modifier: 'public' }}
          validateMessages={validateMessages}
          requiredMark={false}
          style={{ border: '1px solid black' }}
        >
          <ScoreInput
            scoreData={studentData}
            criteria={criteria}
            isThesis={isThesis}
            form={form}
          />
        </Form>
      </>
    );
  }

  function generateCriteriaRows(criteria: any[]) {
    const criteriaRows = [];
    for (const criterion of criteria) {
      const rowNo = criteria.indexOf(criterion) + 1;
      if (rowNo == 3) {
        criteriaRows.push([
          {
            type: Cell.Text,
            value: criterion,
          },
          {
            type: Cell.Blank,
          },
          {
            type: Cell.Blank,
          },
          {
            type: Cell.Text,
            value: studentData.score_presentation,
          },
        ]);
      } else {
        criteriaRows.push([
          {
            type: Cell.Text,
            value: criterion,
          },
          {
            type: Cell.FormItem,
            value: 'score_d' + rowNo,
          },
          {
            type: Cell.FormItem,
            value: 'score_p' + rowNo,
          },
          {
            type: Cell.Blank,
          },
        ]);
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
        bodyStyle={{ height: '70vh', overflowY: 'scroll' }}
      >
        Thesis Program
        {generateForm(
          generateCriteriaRows(Criteria[0].criteria.thesis),
          true,
          formThesis
        )}
        <br />
        Lab Seminar
        {generateForm(
          generateCriteriaRows(Criteria[0].criteria.labSeminar),
          false,
          formLabSeminar
        )}
      </Modal>
    </>
  );
};

export default SupervisorEvaluationForm;

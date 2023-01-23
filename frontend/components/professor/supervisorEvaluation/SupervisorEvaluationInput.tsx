import { Col, Form, InputNumber, Row } from 'antd';
import React from 'react';
import {
  Criteria,
  Header,
} from '../../../core/data/supervisorEvaluationCriteria';
import SchoolYear from '../../../core/types/schoolYear';
import Cell from '../../../core/types/supervisorEvaluation';
import { getSchoolYear } from '../../../core/utils';
import styles from '../../../styles/ProfessorPagesLayout.module.css';

class SupervisorEvaluationInput extends React.Component<any, any> {
  constructor(props: {
    record: any;
    criteria: any;
    score_presentation: number;
    typeOfTable: string;
    //   form: FormInstance,
  }) {
    super(props);

    //   this.state = (props.record[props.typeOfTable])? {
    //     score_daily_activities_1: props.record[props.typeOfTable].score_daily_activities_1 as number,
    //     score_meeting_presentation_1: props.record[props.typeOfTable].score_meeting_presentation_1 as number,
    //     score_daily_activities_2: props.record[props.typeOfTable].score_daily_activities_2 as number,
    //     score_meeting_presentation_2: props.record[props.typeOfTable].score_meeting_presentation_2 as number,
    //     course_score: props.record[props.typeOfTable].course_score as number,
    //   } : {
    //     score_daily_activities_1: 0 as number,
    //     score_meeting_presentation_1: 0 as number,
    //     score_daily_activities_2: 0 as number,
    //     score_meeting_presentation_2: 0 as number,
    //     course_score: 0 as number,
    //   };
  }

  // calculateCourseScore = () => {
  //   setTimeout(function (this: SupervisorEvaluationInput) {
  //     let course_score;
  //     if (this.props.typeOfTable == "thesis_program") {
  //       course_score =
  //         Math.round(this.calculateThesisCourseScore() * 100) / 100;
  //     } else {
  //       course_score =
  //         Math.round(this.calculateLabSeminarCourseScore() * 100) / 100;
  //     }
  //     this.setState({
  //       course_score: course_score,
  //     });
  //     this.props.form.setFieldsValue({course_score: course_score});
  //   }, 1000);
  //   return null;
  // };

  // calculateThesisCourseScore = (): number => {
  //   const { score_daily_activities_1, score_daily_activities_2, score_meeting_presentation_1, score_meeting_presentation_2 } = this.state;
  //   const originalCourseScore =
  //     score_daily_activities_1 * 0.35 +
  //     score_daily_activities_2 * 0.35 +
  //     score_meeting_presentation_1 * 0.1 +
  //     score_meeting_presentation_2 * 0.1 +
  //     this.props.score_presentation * 0.1;
  //   if (this.hasLabRotation) {
  //     return (
  //       originalCourseScore * (5 / 6) +
  //       this.props.record.lab_rotation.course_score * (1 / 6)
  //     );
  //   } else {
  //     return originalCourseScore;
  //   }
  // };

  // calculateLabSeminarCourseScore = () => {
  //   const { score_daily_activities_1, score_daily_activities_2, score_meeting_presentation_1, score_meeting_presentation_2 } = this.state;
  //   const originalCourseScore =
  //     score_daily_activities_1 * 0.35 +
  //     score_daily_activities_2 * 0.15 +
  //     score_meeting_presentation_1 * 0.3 +
  //     score_meeting_presentation_2 * 0.1 +
  //     this.props.score_presentation * 0.1;
  //   if (this.hasLabRotation) {
  //     return (
  //       originalCourseScore * 0.5 +
  //       this.props.record.lab_rotation.course_score * 0.5
  //     );
  //   } else {
  //     return originalCourseScore;
  //   }
  // };

  // getOnChange = (score: string) => {
  //   switch (score) {
  //     case 'score_daily_activities_1':
  //       return this.onD1Change;
  //     case 'score_daily_activities_2':
  //       return this.onD2Change;
  //     case 'score_meeting_presentation_1':
  //       return this.onP1Change;
  //     case 'score_meeting_presentation_2':
  //       return this.onP2Change;
  //     default:
  //       return undefined;
  //   }
  // };
  // onD1Change = (value: number) => {
  //   this.setState({
  //     score_daily_activities_1: value,
  //   });
  //   this.calculateCourseScore();
  // };

  // onD2Change = (value: number) => {
  //   this.setState({
  //     score_daily_activities_2: value,
  //   });
  //   this.calculateCourseScore();
  // };

  // onP1Change = (value: number) => {
  //   this.setState({
  //     score_meeting_presentation_1: value,
  //   });
  //   this.calculateCourseScore();
  // };

  // onP2Change = (value: number) => {
  //   this.setState({
  //     score_meeting_presentation_2: value,
  //   });
  //   this.calculateCourseScore();
  // };

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
              this.props.record[this.props.typeOfTable]
                ? this.props.record[this.props.typeOfTable][cellItem.value]
                : 0
            }
            style={{ margin: 0 }}
          >
            <InputNumber
              min={0}
              max={100}
              size="large"
              controls={false}
              style={{ width: '100%' }}
              // onChange={this.getOnChange(cellItem.value)}
              // value={this.state[cellItem.value]}
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
    const schoolYear = getSchoolYear(
      this.props.record.presentation.student.admission_date,
      this.props.record.presentation.presentation_date,
      this.props.record.presentation.student.email.split('@')[0]
    );
    const noOfCol = Criteria[SchoolYear[schoolYear]].hasLabRotation ? 5 : 4;

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
                <Col span={24} style={{ display: 'none' }}>
                  {this.generateCell({
                    type: Cell.FormItem,
                    value: 'course_score',
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
                      value: this.props.record.lab_rotation.course_score,
                    })}
                  </Col>

                  <Col span={24} style={{ display: 'none' }}>
                    {this.generateCell({
                      type: Cell.FormItem,
                      value: 'course_score',
                      disabled: true,
                      label: 'Course Score',
                    })}
                  </Col>
                </>
              );
            }
          })()}
          {/* {this.calculateCourseScore()} */}
        </Row>
      </>
    );
  }
}

export default SupervisorEvaluationInput;

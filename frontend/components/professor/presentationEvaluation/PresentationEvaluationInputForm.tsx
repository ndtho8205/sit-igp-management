import { EditOutlined, QuestionCircleOutlined } from '@ant-design/icons';
import { Form, Input, Popover, Table } from 'antd';
import React from 'react';
import { useQueryClient } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import { compute_presentaion_question_score } from '../../../core/computeScore';
import presentationEvaluationRubric from '../../../core/data/presentationEvaluationRubric';
import {
  PresentationEvaluation,
  PresentationEvaluationGivenByUser,
} from '../../../core/types/presentation';
import InputRatingScore from '../../common/InputRatingScore';
import ModalForm from '../../common/ModalForm';

type Props = {
  evaluation: PresentationEvaluationGivenByUser;
};

const PresentationEvaluationInputForm = ({ evaluation }: Props) => {
  const queryClient = useQueryClient();
  const { createPresentationEvaluation, updatePresentationEvaluation } =
    usePresentationsApi();

  const handleOnOk = async (obj: PresentationEvaluation) => {
    obj.question_score = compute_presentaion_question_score(
      obj.score_research_goal,
      obj.score_delivery,
      obj.score_visual_aid,
      obj.score_time,
      obj.score_qa_ability
    );

    if (evaluation.evaluation === null) {
      return await createPresentationEvaluation(
        evaluation.presentation_id,
        evaluation.reviewer_id,
        obj
      );
    } else {
      return await updatePresentationEvaluation(
        evaluation.presentation_id,
        evaluation.reviewer_id,
        obj
      );
    }
  };

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findAllPresentations');
  };

  const columns = [
    // { title: 'Criteria', dataIndex: 'criteria', key: 'criteria' },
    { title: 'Weight', dataIndex: 'weight', key: 'weight' },
    { title: '1: Poor', dataIndex: 'poor', key: 'poor' },
    { title: '2: Weak', dataIndex: 'weak', key: 'weak' },
    { title: '3: Average', dataIndex: 'average', key: 'average' },
    { title: '4: Good', dataIndex: 'good', key: 'good' },
    { title: '5: Excellent', dataIndex: 'excellent', key: 'excellent' },
  ];

  const formLayout = {
    layout: 'horizontal',
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

  const insertFormItems = () => {
    const items = [];
    for (const criterion of presentationEvaluationRubric) {
      items.push(
        <Form.Item
          label={
            <>
              {criterion.criteria}
              <Popover
                content={
                  <Table
                    dataSource={[criterion]}
                    columns={columns}
                    pagination={{ position: ['none', 'none'] }}
                    bordered
                  ></Table>
                }
                title={criterion.criteria}
                placement="bottomLeft"
                trigger={'click'}
                overlayStyle={{
                  width: '55%',
                }}
              >
                <QuestionCircleOutlined
                  style={{ fontSize: '1.5em', paddingLeft: '6px' }}
                />
              </Popover>
            </>
          }
          name={criterion.key}
          rules={[{ required: true }, { type: 'number', min: 1, max: 5 }]}
          initialValue={
            evaluation.evaluation ? evaluation.evaluation[criterion.key] : null
          }
          // initialValue={0}
        >
          {/* <Slider marks={marks} step={1} max={5} min={1} tipFormatter={formItemTipFormatter}/> */}
          <InputRatingScore
            value={
              evaluation.evaluation
                ? evaluation.evaluation[criterion.key]
                : null
            }
          />
        </Form.Item>
      );
    }
    return items;
  };

  return (
    <ModalForm
      title={evaluation.student.full_name}
      okText="Submit"
      buttonType="primary"
      buttonIcon={<EditOutlined />}
      onOk={handleOnOk}
      onSuccess={handleOnSuccess}
      modalLayout={{ width: '65%' }}
      formLayout={formLayout}
    >
      {insertFormItems()}

      <Form.Item
        label="Comment (Optional)"
        name="comment"
        initialValue={evaluation.evaluation?.comment}
      >
        <Input.TextArea autoSize={{ minRows: 5, maxRows: 5 }} />
      </Form.Item>
    </ModalForm>
  );
};

export default PresentationEvaluationInputForm;

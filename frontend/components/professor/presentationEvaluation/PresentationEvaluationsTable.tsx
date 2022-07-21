import { CheckSquareOutlined } from '@ant-design/icons';
import { Space, Table, Tooltip } from 'antd';
import { ColumnsType } from 'antd/lib/table';
import moment from 'moment';
import { useQuery } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import useProfessorsApi from '../../../core/api/useProfessorsApi';
import {
  Presentation,
  PresentationEvaluation,
  PresentationEvaluationGivenByUser,
} from '../../../core/types/presentation';
import { Professor } from '../../../core/types/professor';
import { notify } from '../../../core/utils';
import PresentationEvaluationInputForm from './PresentationEvaluationInputForm';

const PresentationEvaluationsTable = () => {
  // get user id
  const { whoami } = useProfessorsApi();
  const whoamiQuery = useQuery<Professor, Error>('whoami', whoami);
  const userId = whoamiQuery.data?.id_;

  // fetch Presentations data & transform it
  const { findAllPresentations } = usePresentationsApi();
  const presentationsQuery = useQuery<
    Presentation[],
    Error,
    PresentationEvaluationGivenByUser[]
  >(['findAllPresentations', userId], () => findAllPresentations(userId), {
    enabled: !!userId,
    select: (data) =>
      data
      .filter(_data => {
        let presentation_date = moment(_data.presentation_date);
        let date_now = moment(Date.now());
        if(Math.abs(date_now.diff(presentation_date, 'months')) <= 3){
          return true;
        }
        return false;
      })
      .map((presentation) => {
        let evaluation: PresentationEvaluation | null = null;

        switch (userId) {
          case presentation.reviewer1?.id_:
            evaluation = presentation.reviewer1_evaluation;
            break;
          case presentation.reviewer2?.id_:
            evaluation = presentation.reviewer2_evaluation;
            break;
          case presentation.reviewer3?.id_:
            evaluation = presentation.reviewer3_evaluation;
            break;
          case presentation.reviewer4?.id_:
            evaluation = presentation.reviewer4_evaluation;
            break;
        }

        return {
          presentation_id: presentation.id_,
          reviewer_id: userId as string,
          student: { full_name: presentation.student.full_name },
          evaluation,
        };
      }),
  });

  if (presentationsQuery.error) {
    notify('error', presentationsQuery.error);
  }

  // render
  const columns: ColumnsType<PresentationEvaluationGivenByUser> = [
    {
      title: '',
      key: 'action',
      align: 'center',
      width: '90px',
      render: (_: string, record: PresentationEvaluationGivenByUser) => {
        // if(!record.evaluation){
          return (
            <>
              <Space size="middle">
                <PresentationEvaluationInputForm evaluation={record} />
              </Space>
            </>
          );
        // }
        // else{
        //   return (
        //     <>
        //       <Tooltip placement='right' title='You have submitted the scores for this student.'>
        //         <CheckSquareOutlined 
        //         style={{ fontSize: '2em', color: "green"}}/>
        //       </Tooltip>
        //     </>
        //   )
        // }
      },
    },
    {
      title: 'Student Name',
      dataIndex: ['student', 'full_name'],
    },
    {
      title: 'Research Objectives, Goals, and Plans',
      dataIndex: ['evaluation', 'score_research_goal'],
      align: 'center',
    },
    {
      title: 'Delivery',
      dataIndex: ['evaluation', 'score_delivery'],
      align: 'center',
    },
    {
      title: 'Visual Aids',
      dataIndex: ['evaluation', 'score_visual_aid'],
      align: 'center',
    },
    {
      title: 'Time',
      dataIndex: ['evaluation', 'score_time'],
      align: 'center',
    },
    {
      title: 'Ability to answer Q&A',
      dataIndex: ['evaluation', 'score_qa_ability'],
      align: 'center',
    },
    {
      title: 'Question score',
      dataIndex: ['evaluation', 'question_score'],
      align: 'center',
    },
    {
      title: 'Comment',
      dataIndex: ['evaluation', 'comment'],
      width: '350px',
      ellipsis: true,
    },
  ];

  return (
    <Table
      dataSource={presentationsQuery.data}
      columns={columns}
      loading={presentationsQuery.isLoading}
      rowKey="presentation_id"
      showSorterTooltip
      bordered
    />
  );
};

export default PresentationEvaluationsTable;

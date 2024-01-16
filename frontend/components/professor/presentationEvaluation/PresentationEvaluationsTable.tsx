import { EditOutlined } from '@ant-design/icons';
import { Button, Popover, Space, Table, Typography } from 'antd';
import { ColumnsType } from 'antd/lib/table';
import moment from 'moment';
import { useState } from 'react';
import { useQuery, useQueryClient } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import useProfessorsApi from '../../../core/api/useProfessorsApi';
import {
  Presentation,
  PresentationEvaluation,
  PresentationEvaluationGivenByUser,
} from '../../../core/types/presentation';
import { Professor } from '../../../core/types/professor';
import { getSchoolYear, notify } from '../../../core/utils';
import PresentationEvaluationInputForm from './PresentationEvaluationInputForm';
import SemEndPresentationRubric from './SemEndPresentationRubric';

const PresentationEvaluationsTable = () => {
  const { Title } = Typography;

  // get user id
  const { whoami } = useProfessorsApi();
  const whoamiQuery = useQuery<Professor, Error>('whoami', whoami);
  const userId = whoamiQuery.data?.id_;

  // fetch Presentations data & transform it
  const { findAllPresentations } = usePresentationsApi();
  const [isRefreshBtnClicked, setIsRefreshBtnClicked] =
    useState<boolean>(false);
  const presentationsQuery = useQuery<
    Presentation[],
    Error,
    PresentationEvaluationGivenByUser[]
  >(['findAllPresentations', userId], () => findAllPresentations(userId), {
    enabled: !!userId,
    onSuccess: () => {
      setIsRefreshBtnClicked(false);
    },
    select: (data) =>
      data
        .filter((_data) => {
          let presentation_date = moment(_data.presentation_date);
          let date_now = moment(Date.now());
          if (Math.abs(date_now.diff(presentation_date, 'months')) <= 3) {
            return true;
          }
          return false;
        })
        .map((presentation: Presentation) => {
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
            presentation_length: presentation.presentation_length,
            presentation_date: presentation.presentation_date,
            reviewer_id: userId as string,
            student: { 
              full_name: presentation.student.full_name,
              admission_date: presentation.student.admission_date,
              email: presentation.student.email,
            },
            evaluation,
          };
        }),
  });
  const queryClient = useQueryClient();

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
      render: (_: string, record) => {
        if(record.presentation_length){
          const schoolYear = getSchoolYear(
            record.student.admission_date,
            record.presentation_date,
            record.student.email.split('@')[0]
          );
          const max_allowed_time = schoolYear == 0 ? moment.duration({minutes: 10}) : moment.duration({minutes: 15})
          const [score_time_minutes, score_time_seconds] = record.presentation_length.split(':')
          const score_time = Math.max(
            1,
            5 - Math.abs(
              moment.duration({
                minutes: score_time_minutes,
                seconds: score_time_seconds,
              }).subtract(max_allowed_time).minutes())
          )
          return (
            <>
              <Space size="middle">
                <PresentationEvaluationInputForm 
                  evaluation={record as PresentationEvaluationGivenByUser} 
                  score_time={score_time} 
                />
              </Space>
            </>
          );
        }
        else{
          return (
            <Popover
              placement="topRight"
              title="Missing presentation time"
              content="Please wait until the Session Chair has input the presentation time."
              overlayStyle={{ maxWidth: '500px', textAlign: 'justify' }}
              arrowPointAtCenter={true}
            >
              <EditOutlined />
            </Popover>
          )
          
        }
      },
    },
    {
      title: 'Student Name',
      dataIndex: ['student', 'full_name'],
    },
    {
      title: 'Presentation Time',
      dataIndex: ['presentation_length'],
      align: 'center',
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
    <>
      <Title level={4}>Input Score (as Reviewer)</Title>
      <Space>
        <SemEndPresentationRubric />
        <Button 
          onClick={() => {
            setIsRefreshBtnClicked(true);
            queryClient.invalidateQueries(['findAllPresentations', userId]);
          }}
          loading={isRefreshBtnClicked && queryClient.isFetching() > 0}
        />      
      </Space>
      <Table
        dataSource={presentationsQuery.data}
        columns={columns}
        loading={presentationsQuery.isLoading}
        rowKey="presentation_id"
        showSorterTooltip
        bordered
      />
    </>
  );
};

export default PresentationEvaluationsTable;

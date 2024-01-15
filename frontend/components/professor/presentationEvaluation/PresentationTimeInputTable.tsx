import { Space, Table } from 'antd';
import { ColumnsType } from 'antd/lib/table';
import moment from 'moment';
import { useQuery } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import useProfessorsApi from '../../../core/api/useProfessorsApi';
import {
  Presentation,
} from '../../../core/types/presentation';
import { Professor } from '../../../core/types/professor';
import { notify } from '../../../core/utils';
import PresentationTimeInputForm from './PresentationTimeInputForm';

const PresentationTimeInputTable = () => {
  // get user id
  const { whoami } = useProfessorsApi();
  const whoamiQuery = useQuery<Professor, Error>('whoami', whoami);
  const userId = whoamiQuery.data?.id_;

  // fetch Presentations data & transform it
  const { findSessionChairPresentations } = usePresentationsApi();
  const presentationsQuery = useQuery<
    Presentation[],
    Error
  >(['findSessionChairPresentations', userId], () => findSessionChairPresentations(userId), {
    enabled: !!userId,
    select: (data) =>
      data
        .filter((_data) => {
          let presentation_date = moment(_data.presentation_date);
          let date_now = moment(Date.now());
          if (Math.abs(date_now.diff(presentation_date, 'months')) <= 3) {
            return true;
          }
          return false;
        }),
  });

  if (presentationsQuery.error) {
    notify('error', presentationsQuery.error);
  }

  // render
  const columns: ColumnsType<Presentation> = [
    {
      title: '',
      key: 'action',
      align: 'center',
      width: '90px',
      render: (_: string, record: Presentation) => {
        return (
          <>
            <Space size="middle">
              <PresentationTimeInputForm presentation={record} />
            </Space>
          </>
        );
      },
    },
    {
      title: 'Student Name',
      dataIndex: ['student', 'full_name'],
      key: 'student_id.full_name',
      width: '200px',
    },
    {
      title: 'Presentation Time',
      dataIndex: ['presentation_length'],
      key: 'presentation_length',
      width: '200px',
      align: 'center',
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

export default PresentationTimeInputTable;

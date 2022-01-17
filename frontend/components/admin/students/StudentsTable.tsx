import { Space, Table } from 'antd';
import React from 'react';
import { useQuery, useQueryClient } from 'react-query';
import students_service from '../../../core/api/students_service';
import Student from '../../../core/types/student';
import { notify } from '../../../core/utils';
import DeletePopconfirm from '../../common/DeletePopconfirm';
import StudentEditForm from './StudentEditForm';

function StudentsTable() {
  const queryClient = useQueryClient();
  const { isLoading, data, error } = useQuery<Student[], Error>(
    'findAllStudents',
    students_service.findAll
  );

  const handleOnDeleteSuccess = () => {
    queryClient.invalidateQueries('findAllStudents');
  };

  if (error) {
    notify('error', error);
  }
  console.log(data);

  const columns = [
    { title: 'Full name', dataIndex: 'full_name', key: 'full_name' },
    { title: 'Email', dataIndex: 'email', key: 'email' },
    { title: 'Gender', dataIndex: 'gender', key: 'gender' },
    {
      title: 'Area of Study',
      dataIndex: 'area_of_study',
      key: 'area_of_study',
    },
    {
      title: 'Admission date',
      dataIndex: 'admission_date',
      key: 'admission_date',
    },
    {
      title: 'Supervisor',
      dataIndex: ['supervisor', 'full_name'],
      key: 'supervisor.full_name',
    },
    {
      title: 'Advisor 1',
      dataIndex: ['advisor1', 'full_name'],
      key: 'advisor1.full_name',
    },
    {
      title: 'Advisor 2',
      dataIndex: ['advisor2', 'full_name'],
      key: 'advisor2.full_name',
    },
    {
      title: 'Action',
      key: 'action',
      render: (_: unknown, record: Student) => {
        return (
          <Space size="middle">
            <StudentEditForm student={record} />
            <DeletePopconfirm
              onOk={() => students_service.delete(record.id_)}
              onSuccess={handleOnDeleteSuccess}
            />
          </Space>
        );
      },
    },
  ];

  return (
    <Table
      dataSource={data}
      columns={columns}
      loading={isLoading}
      rowKey="id_"
      showSorterTooltip
      sticky
    ></Table>
  );
}

export default StudentsTable;

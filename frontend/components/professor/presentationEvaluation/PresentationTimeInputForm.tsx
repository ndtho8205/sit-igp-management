import { EditOutlined } from '@ant-design/icons';
import { Form, Input } from 'antd';
import React from 'react';
import { useQueryClient } from 'react-query';
import usePresentationsApi from '../../../core/api/usePresentationsApi';
import { Presentation } from '../../../core/types/presentation';
import ModalForm from '../../common/ModalForm';
import { notify } from '../../../core/utils';

type Props = {
  presentation: Presentation;
};

const PresentationTimeInputForm = ({ presentation }: Props) => {
  const queryClient = useQueryClient();
  const { updatePresentation } = usePresentationsApi();

  const handleOnOk = async (obj: Presentation) => {
    return await updatePresentation(presentation.id_, obj);
  };

  const handleOnSuccess = () => {
    queryClient.invalidateQueries('findSessionChairPresentations');
    notify('success', "Please kindly ask the Reviewers to refresh their pages.")
  };

  return (
    <ModalForm
      title="Update Presentation Time"
      okText="Update"
      buttonIcon={<EditOutlined />}
      onOk={handleOnOk}
      onSuccess={handleOnSuccess}
      initialValues={presentation}
    >
      <Form.Item label="Presentation Time" name="presentation_length">
        <Input />
      </Form.Item>
    </ModalForm>
  );
};

export default PresentationTimeInputForm;

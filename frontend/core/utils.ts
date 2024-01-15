import { message, notification } from 'antd';
import axios, { AxiosError } from 'axios';
import moment from 'moment';

type NotificationType = 'success' | 'error';

const notify = (
  notification_type: NotificationType,
  msg: string | Error | AxiosError
) => {
  if (notification_type == 'error') {
    let error_msg: string = msg as string;

    if (axios.isAxiosError(msg)) {
      switch (msg.response?.status) {
        case 422:
          error_msg = `Validation error. ${JSON.stringify(msg.response.data)}`;
          break;
        case 409:
        case 404:
        default:
          error_msg = msg.response?.data.detail;
      }
    } else if (msg instanceof Error) {
      error_msg = msg.message;
    }

    notification['error']({
      key: 'notify_error',
      message: 'Oops...',
      description: error_msg,
    });
  } else {
    message[notification_type](msg);
  }
};

const getSchoolYear = (
  admissionDate: string,
  considerDate: string,
  id: string
): number => {
  // console.log(id);
  const duplicated_sem = id == 'am20004' ? 1 : id == 'am22101' ? 2 : 0;
  return (
    Math.floor(
      moment(considerDate).diff(moment(admissionDate), 'years', true) * 2
    ) /
      2 -
    duplicated_sem * 0.5
  );
};

export { notify, getSchoolYear };

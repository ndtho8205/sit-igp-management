import { message, notification } from 'antd';
import axios, { AxiosError } from 'axios';

type NotificationType = 'success' | 'error';

const notify = (
  notification_type: NotificationType,
  msg: string | Error | AxiosError
) => {
  console.log({ msg });
  if (notification_type == 'error') {
    let error_msg: string = msg as string;

    if (axios.isAxiosError(msg)) {
      switch (msg.response?.status) {
        case 422:
          error_msg = 'Validation error.';
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

export { notify };

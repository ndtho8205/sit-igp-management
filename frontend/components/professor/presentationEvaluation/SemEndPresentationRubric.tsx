import { Button, Modal, Table } from 'antd';
import semEndRubric from '../../../core/data/presentationEvaluationRubric';
import styles from '../../../styles/ProfessorPagesLayout.module.css';

const SemEndPresentationRubric = () => {
  // const [isFormVisible, setFormVisible] = useState(false);

  const columns = [
    { title: 'Criteria', dataIndex: 'criteria', key: 'criteria' },
    { title: 'Weight', dataIndex: 'weight', key: 'weight' },
    { title: '1: Poor', dataIndex: 'poor', key: 'poor' },
    { title: '2: Weak', dataIndex: 'weak', key: 'weak' },
    { title: '3: Average', dataIndex: 'average', key: 'average' },
    { title: '4: Good', dataIndex: 'good', key: 'good' },
    { title: '5: Excellent', dataIndex: 'excellent', key: 'excellent' },
  ];

  function showRubric() {
    Modal.info({
      // title: 'This is a notification message',
      content: (
        <Table
          id={'semEndRubricTable'}
          dataSource={semEndRubric}
          columns={columns}
          pagination={{ position: ['none', 'none'] }}
          className={styles.myTable}
          bordered
        ></Table>
      ),
      width: '90%',
      maskClosable: true,
      okType: 'ghost',
      okText: 'Close',
      onOk() {},
    });
  }

  return <Button onClick={showRubric}>Show Rubric</Button>;
};

export default SemEndPresentationRubric;

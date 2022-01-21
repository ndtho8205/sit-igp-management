import { Col, Row, Slider } from 'antd';
import { useState } from 'react';
import styles from '../../styles/ProfessorPagesLayout.module.css';

type Props = {
  value: number;
  onChange?: (value: number) => void;
};

const InputRatingScore = (props: Props) => {
  const [currentValue, setValue] = useState(props.value || 0);

  const handleOnChange = (value: number) => {
    console.log({ value });
    setValue(value);
    props.onChange?.(value);
  };

  const marks = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
  };

  const formatTooltip = (value?: number) => {
    if (!value) return null;

    const marksTip = {
      1: 'Poor',
      2: 'Weak',
      3: 'Average',
      4: 'Good',
      5: 'Excellent',
    };
    return <span>{marksTip[value]}</span>;
  };

  return (
    <Row gutter={10}>
      <Col span={3}>
        <span className={styles.scoreInputDescription}>
          {formatTooltip(currentValue) || 'Not yet rated.'}
        </span>
      </Col>

      <Col span={21}>
        <Slider
          marks={marks}
          step={1}
          max={5}
          min={0}
          tipFormatter={formatTooltip}
          onChange={handleOnChange}
          value={currentValue}
        />
      </Col>
    </Row>
  );
};

export default InputRatingScore;

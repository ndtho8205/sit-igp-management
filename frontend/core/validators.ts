// @ts-nocheck
import { Rule } from 'antd/lib/form';

const FullName: Rule[] = [{ max: 256, min: 1, type: 'string' }];
const UniversityEmail: Rule[] = [
  {
    max: 256,
    min: 1,
    type: 'email',
  },
  {
    validator(rule, value: string): Error[] {
      if (value && value.slice(value.indexOf('@')) !== '@shibaura-it.ac.jp') {
        return Promise.reject(
          new Error(`${rule.field} must be provided by SIT`)
        );
      }

      return Promise.resolve();
    },
  },
];

const rules = { FullName, UniversityEmail };
export { rules };

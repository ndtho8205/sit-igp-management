type ValidationError = {
  loc: string[];
  msg: string;
  type: string;
};

type HTTPValidationError = {
  detail: ValidationError[];
};

export default HTTPValidationError;

import Cell from '../types/supervisorEvaluation';

const Header = [
  {
    type: Cell.Text,
    value: 'Evaluation Criteria',
  },
  {
    type: Cell.Text,
    value: 'Daily Activities\n(0 - 100 scale)',
  },
  {
    type: Cell.Text,
    value: 'Presentation in Meeting\n(0 - 100 scale)',
  },
  {
    type: Cell.Text,
    value: 'Presentation at the End of the Semester\n(0 - 100 scale)',
  },
  {
    type: Cell.Text,
    value: 'Lab Rotation\n(0 - 100 scale)',
  },
];
const Criteria = {
  Freshmen_1: {
    thesis: [
      'Students can understand basic knowledge and skills for problem-finding and -solving in engineering.',
      'Students can work for a team organized by the laboratory members in solving social issues.',
      'Students can develop thinking skills and present their research progress at the end of semester presentation.',
    ],
    labSeminar: [
      'Students can understand the research conducted in the laboratory based on the knowledge of basic STEM subjects and identyfy unclear points in discussions.',
      'Students can use communication skills and creative mindset in discussions with various types of laboratory members such as the supervisor, post-doctoral researchers, teaching assistants and senior students.',
      'Students can connect book knowledge to real-world applications, develop an appreciation for research in their field and show their achievement at the end of semester presentation.',
    ],
    hasLabRotation: false,
  },

  Freshmen_2: {
    thesis: [
      'Students can use computer, software and research equipment to conduct research along with acquired basic STEM skills.',
      "Students can understand the effects and impact of engineering on society and nature, and of engineers' social responsibilities or engineering ethics.",
      'Students can develop thinking skills and present their research progress at the end of semester presentation.',
    ],
    labSeminar: [
      'Students can consult a wide range of reference papers in a self-directed manner.',
      'Students can understand the research conducted in the laboratory through discussions with the laboratory members, and use the ability to work as a team which consists of the supervisor, post-doctoral researchers, teaching assistants and senior students.',
      'Students can connect book knowledge to real-world applications, develop an appreciation for research in their field and show their achievement at the end of semester presentation.',
    ],
    hasLabRotation: false,
  },

  Sophomore_1: {
    thesis: [
      'Students can clarify what are common and different in conducting research by comparing different laboratory works.',
      'Students can apply basic knowledge for science and engineering to problem-solving in real R&D sites.',
      'Students can develop thinking skills and present their research progress at the end of semester presentation.',
    ],
    labSeminar: [
      'Students can understand a wide range of research and clearly identify what they cannot understand in the topic being discussed.',
      'Students can explain their own research to people who are not in the same research areas and understand the importance of multidisciplinary approach.',
      'Students can connect book knowledge to real-world applications, develop an appreciation for research in their field and show their achievement at the end of semester presentation.',
    ],
    hasLabRotation: true,
  },

  Sophomore_2: {
    thesis: [
      'Students can clarify what are common and different in conducting research by comparing different laboratory works.',
      'Students can apply basic knowledge for science and engineering to problem-solving in real R&D sites.',
      'Students can develop thinking skills and present their research progress at the end of semester presentation.',
    ],
    labSeminar: [
      'Students can understand a wide range of research and clearly identify what they cannot understand in the topic being discussed.',
      'Students can explain their own research to people who are not in the same research areas and understand the importance of multidisciplinary approach.',
      'Students can connect book knowledge to real-world applications, develop an appreciation for research in their field and show their achievement at the end of semester presentation.',
    ],
    hasLabRotation: true,
  },

  Junior_1: {
    thesis: [
      'Students can clarify what are common and different in conducting research by comparing different laboratory works.',
      'Students can apply basic knowledge for science and engineering to problem-solving in real R&D sites.',
      'Students can develop thinking skills and present their research progress at the end of semester presentation.',
    ],
    labSeminar: [
      'Students can understand a wide range of research and clearly identify what they cannot understand in the topic being discussed.',
      'Students can explain their own research to people who are not in the same research areas and understand the importance of multidisciplinary approach.',
      'Students can connect book knowledge to real-world applications, develop an appreciation for research in their field and show their achievement at the end of semester presentation.',
    ],
    hasLabRotation: false,
  },

  Junior_2: {
    thesis: [
      'Students can clarify what are common and different in conducting research by comparing different laboratory works.',
      'Students can apply basic knowledge for science and engineering to problem-solving in real R&D sites.',
      'Students can develop thinking skills and present their research progress at the end of semester presentation.',
    ],
    labSeminar: [
      'Students can understand a wide range of research and clearly identify what they cannot understand in the topic being discussed.',
      'Students can explain their own research to people who are not in the same research areas and understand the importance of multidisciplinary approach.',
      'Students can connect book knowledge to real-world applications, develop an appreciation for research in their field and show their achievement at the end of semester presentation.',
    ],
    hasLabRotation: false,
  },
};

export { Header, Criteria };

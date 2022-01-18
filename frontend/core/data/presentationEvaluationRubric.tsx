const presentationEvaluationRubric = [
  {
    criteria: 'Research Objectives, Goals, and Plans',
    key: 'score_research_goal',
    weight: '35%',
    excellent: [
      'Includes an engaging introduction, a fully detailed body and an effective conclusion (in which key points are clearly recapped and highlighted).',
    ],
    good: [
      'Includes an engaging introduction, almost full detailed body, and an effective conclusion (in which majority of key points are recapped and highlighted.)',
    ],
    average: [
      'Includes an introduction, a detailed body, and a reasonable conclusion (in which some of the key points are not highlighted effectively).',
    ],
    weak: [
      'Includes an introduction, a less detailed body, and a brief conclusion (which may need additional development).',
    ],
    poor: [
      'Some content facts seem questionable and is missing an introduction, body and/or conclusion.',
    ],
  },
  {
    criteria: 'Delivery',
    weight: '20%',
    key: 'score_delivery',
    excellent: [
      'The logic is fully developed.',
      'No verbal fillers.',
      'The audience can understand the whole content clearly and completely.',
    ],
    good: [
      'The logic is well developed.',
      'Mostly no verbal fillers.',
      'The audience can understand most of the content clearly.',
    ],
    average: [
      'The logic is adequately and appropriately developed.',
      'A few verbal fillers.',
      'The audience can understand the whole content well.',
    ],
    weak: [
      'The logic is sometimes not adequately and appropriately developed.',
      'Frequent verbal fillers.',
      'The audience cannot understand the whole content well.',
    ],
    poor: [
      'There is no logic at all.',
      'A lot of verbal fillers.',
      'The audience cannot understand the whole content at all.',
    ],
  },
  {
    criteria: 'Visual Aids',
    weight: '20%',
    key: 'score_visual_aid',
    excellent: [
      'Visual aids are informative, innovative, and easy to read.',
      'All the data and diagrams are effectively used.',
    ],
    good: [
      'Visual aids are mostly informative, innovative, and easy to read.',
      'Most of the data and diagrams are effectively used.',
    ],
    average: [
      'Visual aids are informative and generally supportive of the presentation.',
      'Some could be improved to complement the speaker’s content more effectively.',
    ],
    weak: [
      'The visual aids are reasonably supportive of the presentation.',
      'Some of them are difficult to read, and/or not necessary for the intent of the topic.',
    ],
    poor: [
      "Visual aid does not connect to the speech and lacks information to convey the speaker's intention.",
      'Some data and diagrams are not effectively or appropriately used at all.',
    ],
  },
  {
    criteria: 'Time',
    weight: '5%',
    key: 'score_time',
    excellent: ['Speech is given within the time allotted.'],
    good: ['Speech is 1 minute short or over the allotted time.'],
    average: ['Speech is 2 minutes short or over the allotted time.'],
    weak: ['Speech is 3 minutes short or over the allotted time.'],
    poor: ['Speech is more than 4 minutes short or over the allotted time.'],
  },
  {
    criteria: 'Ability to answer Q&A',
    weight: '20%',
    key: 'score_qa',
    excellent: [
      'Confidently demonstrates an excellent interpretation and knowledge of the subject and responds to every question by reviewers.',
    ],
    good: [
      'Demonstrates a very good interpretation and knowledge of the subject and responds to almost all the questions asked.',
    ],
    average: [
      'Demonstrates a good understanding of the subject and responds to almost all the questions asked.',
    ],
    weak: [
      'Demonstrates a fair understanding of questions but answers somewhat vaguely.',
    ],
    poor: [
      'Lacks understanding of the questions, gives incorrect responses or fails to respond at all to questions.',
    ],
  },
];

export default presentationEvaluationRubric;

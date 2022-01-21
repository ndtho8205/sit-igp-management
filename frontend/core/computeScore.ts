const compute_presentaion_question_score = (
  score_research_goal: number,
  score_delivery: number,
  score_visual_aid: number,
  score_time: number,
  score_qa_ability: number
) => {
  return (
    (score_research_goal * 0.35 +
      score_delivery * 0.2 +
      score_visual_aid * 0.2 +
      score_time * 0.05 +
      score_qa_ability * 0.2) *
    20
  );
};

export { compute_presentaion_question_score };

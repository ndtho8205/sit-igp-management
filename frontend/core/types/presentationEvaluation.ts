type PresentationEvaluation = {
  id_: string;

  presentation_id: string;
  reviewer_id: string;
  score_research_goal: number;
  score_delivery: number;
  score_visual_aid: number;
  score_time: number;
  score_qa: number;
  comment: string;

  is_deleted: boolean;
};

export default PresentationEvaluation;

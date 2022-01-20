from backend.entities import (
    Professor,
    PresentationEvaluation,
    compute_presentation_question_score,
)
from backend.usecases.inputs import PresentationEvaluationCreateInput
from backend.usecases.validators import validate_presentation_evaluation_reviewer_rights
from backend.usecases.repositories.presentation_repository import PresentationRepository
from backend.usecases.repositories.presentation_evaluation_repository import (
    PresentationEvaluationRepository,
)


def create_new_presentation_evaluation(
    current_user: Professor,
    presentation_repository: PresentationRepository,
    presentation_evaluation_repository: PresentationEvaluationRepository,
    inp: PresentationEvaluationCreateInput,
) -> PresentationEvaluation:
    validate_presentation_evaluation_reviewer_rights(
        presentation_repository,
        presentation_evaluation_repository,
        current_user.id_,
        inp.reviewer_id,
    )

    question_score = compute_presentation_question_score(
        research_goal=inp.score_research_goal,
        delivery=inp.score_delivery,
        visual_aid=inp.score_visual_aid,
        time=inp.score_time,
        qa_ability=inp.score_qa_ability,
    )
    evaluation = presentation_evaluation_repository.create(
        inp,
        question_score=question_score,
    )
    return evaluation

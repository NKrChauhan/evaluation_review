from apps.review.models import Review, ReviewDetail


class ReviewService:
    @staticmethod
    def get_review_details(content):
        return ReviewDetail.objects.filter(review__content=content)

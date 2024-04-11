from apps.compliance.models import Guideline


class GuidelineService:
    @staticmethod
    def get_guideline_by_id(guideline_id):
        try:
            return Guideline.objects.get(id=guideline_id)
        except Guideline.DoesNotExist:
            raise ValueError('Guideline does not exist')

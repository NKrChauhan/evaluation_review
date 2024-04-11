from apps.content.models import Content


class ContentService:
    @staticmethod
    def get_contnet_by_id(content_id):
        try:
            return Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            raise ValueError('Content does not exist')
        
    @staticmethod
    def get_all_content():
        return Content.objects.all()
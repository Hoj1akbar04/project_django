import uuid
from django.db.models import TextChoices


class SaveMediaFile(object):
    def image_speciality(self, filename):
        image_extension = filename.split('.')[-1]
        return f'course/speciality//{uuid.uuid4()}.{image_extension}'

    def image_course(self, filename):
        image_extension = filename.split('.')[-1]
        return f'course/course//{uuid.uuid4()}.{image_extension}'


class Choices(object):
    class PriceType(TextChoices):
        s = "USD", "$"
        sum = "UZS", "SO'M"

    class CourseStatus(TextChoices):
        DRAFT = 'df', 'Draft'
        PUBLISHED = 'pb', 'Published'
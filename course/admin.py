from django.contrib import admin
from .models import Speciality, Course, Teacher, Position


admin.site.register(Speciality)
admin.site.register(Position)
admin.site.register(Teacher)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'image')
    prepopulated_fields = {'slug': ('title',)}

from django.contrib import admin

from .models import Company, Job, Patent, ResumeSummary, Skill, SkillArea

# Register your models here.

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Patent)
admin.site.register(ResumeSummary)
admin.site.register(Skill)
admin.site.register(SkillArea)

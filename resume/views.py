from django.shortcuts import render

from .models import Company, Job, Patent, ResumeSummary, Skill, SkillArea

def index(request):

    resume_summary = ResumeSummary.objects.last()

    context = {
        'resume_summary': resume_summary,
    }

    return render(request, 'main/resume.html', context)
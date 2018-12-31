from django.shortcuts import render

from .models import Company, Job, Patent, ResumeSummary, Skill, SkillArea

def index(request):

    resume_summary = ResumeSummary.objects.last()
    jobs = Job.objects.order_by('-date_started')
    skills = Skill.objects.order_by('skill_area__display_order', 'name').prefetch_related('skill_area')
    patents = Patent.objects.order_by('-uspto_number')

    context = {
        'resume_summary': resume_summary,
        'jobs': jobs,
        'skills': skills,
        'patents': patents,
    }

    return render(request, 'main/resume.html', context)
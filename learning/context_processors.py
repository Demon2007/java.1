from .models import Lesson, LessonProgress


def global_progress(request):
    total_lessons = Lesson.objects.count()

    completed_count = 0
    if request.user.is_authenticated:
        completed_count = LessonProgress.objects.filter(
            user=request.user,
            is_completed=True
        ).count()

    progress_percent = 0
    if total_lessons > 0:
        progress_percent = round((completed_count / total_lessons) * 100)

    return {
        "total_lessons": total_lessons,
        "completed_count": completed_count,
        "progress_percent": progress_percent,
    }
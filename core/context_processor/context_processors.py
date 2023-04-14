from core.models import Settings

def base(request):
    settings = Settings.objects.first()
    context = {
        'settings' : settings,
    }
    return context
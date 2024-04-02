from django.http import JsonResponse

def demo(request, *args, **kwargs):
    return JsonResponse({"message": "Hi, Welcome here!"})

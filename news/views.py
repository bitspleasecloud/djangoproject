from django.http import HttpResponse, JsonResponse


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

# CSRF - Cross Site Resource Forgery
@csrf_exempt
def get_news(request):
    if request.method == "POST":
        data = {
            "response": "Hello world"
        }
        return JsonResponse(data)
    return HttpResponse("Hello from Get response")

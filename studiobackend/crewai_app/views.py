from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def crewai_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('input')
        response_data = {"message": f"Processed {user_input}"}
        return JsonResponse(response_data)
    return JsonResponse({"error": "Invalid request method"}, status=400)

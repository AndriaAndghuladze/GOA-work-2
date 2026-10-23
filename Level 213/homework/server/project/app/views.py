from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# api_view -> ამის საშუალებით შეგვიძლია მივუთითოთ view ს რა სახის http method ბის მიღება შეუძლია, ამ შემთხვევაში იღებს მხოლოდ GET ს, ანუ ეს view გამოიყენება მხოლოდ იმისათვის რომ მომხარებელმა რაიმე ინფორმაცია წამოიღოს
@api_view(['GET'])
def task_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        # გარდავქმნით ჩვენს პითონის ობიექტებს JSON ად, რახან გადავცემთ აქ ბევრ პითონის ობიექტს (querySet ს), უნდა მივუთით ასევე many=True ატრიბუტი რომ JSON ში შექმნას სია და სიის სახით გააგზავნოს response
        serializer = TaskSerializer(tasks, many=True)
        # Response ფუნქცია მეხმარება იმაში რომ response ად დავაბრუნოთ JSON ის ინფორმაცია, ამ შემთხევვაში serializer.data ანუ JSON ად გარდაქმნილი ინფორმაცია
        return Response(serializer.data)
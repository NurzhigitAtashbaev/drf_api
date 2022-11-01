from rest_framework.views import Response
from rest_framework import views


class OrderView(views.APIView):
    def get(self, request):
        print(request.method)
        return Response({'data:': 'Hello'})

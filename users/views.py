from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    """APIView for order"""

    def get(self, request):
        print(request.method)
        return Response({"data": "Hi, Python !"})
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from incidents.serializers import SubscriberSerializer


class SubscriberView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

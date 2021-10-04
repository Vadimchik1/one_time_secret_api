from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Secret
from django.http import Http404, JsonResponse
from .serializers import SecretSerializer, ShowSecretSerializer


class SecretView(APIView):
    @swagger_auto_schema(operation_description="description", request_body=SecretSerializer)
    def post(self, request, format=None):
        serializer = SecretSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'your_secret_key': serializer.data['password']}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecretDetail(APIView):
    def get_object(self, password):
        try:
            return Secret.objects.get(password=password)
        except Secret.DoesNotExist:
            raise Http404

    def get(self, request, password, format=None):
        secret = self.get_object(password)
        serializer = ShowSecretSerializer(secret)
        if secret.password == password:
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=401)

    def delete(self, request, password, format=None):
        secret = self.get_object(password)
        serializer = ShowSecretSerializer(secret)
        if secret.password == password:
            secret.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(serializer.errors, status=401)
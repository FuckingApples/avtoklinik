from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.api.serializers.templates import TemplateSerializer
from apps.templates.models import Template


class TemplateListCreateAPI(APIView):
    def get(self, request):
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TemplateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        template = Template.objects.create(**serializer.validated_data.__dict__)
        return Response(TemplateSerializer(template).data, status=status.HTTP_201_CREATED)

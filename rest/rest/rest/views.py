from django.shortcuts import render
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.serializers import CountrySerializers
from app.models import Country

class Api(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        querySet = Country.objects.all()
        serializers = CountrySerializers(querySet, many=True)

        return Response(serializers.data)


    def post(self, request, *args, **kwargs):
        serializers = CountrySerializers(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
        return Response(serializers.errors)
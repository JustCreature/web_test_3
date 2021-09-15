from django.shortcuts import render
from django.db import models
from .models import StatusVals

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Site, Pivot
from .serializers import (SiteListSerializer, SiteCreateSerializer,
                          SiteDetailSerializer, CreateStatusSerializer)

# Create your views here.

class AddStatusView(APIView):

    def post(self, request):
        serializer = CreateStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

class SiteListView(APIView):

    def get(self, request):
        sites = Site.objects.all()
        # print(sites[0].url)
        # sites = Site.objects.annotate(
        #     status=models.ForeignKey(
        #
        #     )
        # )
        serializer = SiteListSerializer(sites)
        # print(serializer.data)
        return Response(serializer.data)

class SiteDetailView(APIView):
    def get(self, request, pk):
        site = Site.objects.get(name=pk)

        serializer = SiteDetailSerializer(site)
        return Response(serializer.data)


class AddSiteView(APIView):

    def post(self, request):
        site = SiteCreateSerializer(data=request.data)
        if site.is_valid():
            site.save()
        return Response(status=201)

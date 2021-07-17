from django.shortcuts import render
from rest_framework import ApiView

class SongAPIView(ApiView):

    def get(self,request):
        return Response(data={"Hello, song"})
from django.contrib.auth.decorators import login_required
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from os import environ
from pyarlo import PyArlo


class ArloCameraSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, read_only=True)
    battery_level = serializers.IntegerField(read_only=True)


class ArloBaseStationSerializer(serializers.Serializer):
    mode = serializers.CharField(required=False, read_only=True)


class ArloStatusSerializer(serializers.Serializer):
    base_station=ArloBaseStationSerializer(many=False)
    cameras = ArloCameraSerializer(many=True)
    mode = serializers.CharField(required=False, read_only=True)


@api_view(['GET'])
@login_required
def summary(request):
    username = environ.get("arlo_username")
    password = environ.get("arlo_password")

    arlo = PyArlo(username, password)

    serializer = ArloStatusSerializer({"base_station": arlo.base_stations[0], "cameras": arlo.cameras}, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@login_required
def cameras(request):
    username = environ.get("arlo_username")
    password = environ.get("arlo_password")

    arlo = PyArlo(username, password)

    serializer = ArloCameraSerializer(arlo.cameras, many=True)
    return Response(serializer.data)


from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from testApp.serializers import ContactSerializer, GroupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from testApp.models import Contact, Group
import logging
from rest_framework.views import APIView
import json
from rest_framework.permissions import AllowAny


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    logging.warning("~~~Create Contact~~~")
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]


class ContactListAPIView(generics.ListAPIView):
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        logging.warning("~~~Get Contacts~~~")
        qs = Contact.objects.all()
        id = self.request.GET.get("id", None)
        if id is not None:
            qs = qs.filter(id=id)
        return qs


class ContactRetrieveAPIView(generics.RetrieveAPIView):
    logging.warning("~~~Contact by id~~~")
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]


class ContactUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    # lookup_field = "id"

    def get_queryset(self):
        data = Contact.objects.all()
        return data

    def update(self, request, *args, **kwargs):
        logging.warning("~~~Update contact~~~")
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        instance.name = request.data.get("name", instance.name)
        instance.phone = request.data.get("phone", instance.phone)
        instance.address = request.data.get("address", instance.address)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance.save()
        result = {
            "detail": serializer.data,
        }
        return Response(result)


class ContactDestroyAPIView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializers_class = ContactSerializer
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": "successfully deleted contact"}, status=status.HTTP_204_NO_CONTENT
        )


class GroupView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def get(self, request, format=None):
        group = Group.objects.all()
        serializer = GroupSerializer(group, many=True)
        return Response(serializer.data)


class GroupAdd(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        JSONWebTokenAuthentication,
    ]

    def get_object(self, pk):
        try:
            return Group.objects.get(id=pk)
        except Group.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_object(pk)
        contacts = [i.id for i in group.contacts.all()]
        if len(contacts) == 0:
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            msg = {
                "detail": "You cant perform delete operation because {count} contact available in this group".format(
                    count=len(contacts)
                )
            }
            return Response(json.dumps(msg), status=status.HTTP_400_BAD_REQUEST)

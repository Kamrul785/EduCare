from django.shortcuts import render
from tuition.serializers import TuitionSerializer
from tuition.models import Tuition
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from tuition.filters import TuitionFilter
from tuition.paginations import DefaultPagination
# Create your views here.

class IsTutor(permissions.BasePermission):
    """Only tutors can create/update/delete tuition posts"""
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        return request.user.is_authenticated and request.user.role == 'Tutor' or request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        if view.action in ["put", "patch", "destroy"]:
            return obj.tutor == request.user
        return True

class TuitionViewSet(ModelViewSet):
    serializer_class = TuitionSerializer
    queryset = Tuition.objects.all()
    permission_classes = [IsTutor]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TuitionFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description', 'subject', 'class_level']
    ordering_fields = ['created_at', 'class_level']
    
    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)
# coding=utf-8
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ('url', 'id', 'todo', 'done', 'desc', 'priority',
                  'expire', 'expire_date', 'add_time', 'modify_time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name="task-detail", read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'tasks')

# coding=utf-8
import sys
from django.db import models

reload(sys)
sys.setdefaultencoding("utf8")
# Create your models here.


class Task(models.Model):
    """
    name 任务名
    desc 描述
    done 完成情况
    priority 优先级
    expire 是否有截止
    expire_date 截止日期
    add_time 创建时间
    modify_time 修改时间
    owner 拥有者
    """
    todo = models.CharField(max_length=50)
    desc = models.TextField(blank=True, default="")
    done = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    expire = models.BooleanField(default=False)
    expire_date = models.DateTimeField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.todo

    class Meta:
        # 按是否完成、优先级以及创建时间排序
        ordering = ('done', 'priority', 'add_time')

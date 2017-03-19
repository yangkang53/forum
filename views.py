from django.shortcuts import render
from django.db import models

class Block(models.Model):
    name = models.CharField(u"版块名称",max_length=100)
    desc = models.CharField(u"版块描述", max_length=100)
    manager_name = models.CharField(u"管理员名称", max_length=100)


def index(request):
    block_infos = Block.objects.all().order_by("-id")
    return render(request, "index.html", {"blocks": block_infos})

# -*- coding:utf-8 -*-
from django.db import models

TEA_KINDS = (
    ("english", u"英式红茶"),
    ("chinese", u"中国茶"),
    ("japanese", u"日本茶"),
)

class TeaManager(models.Manager):
    def recommended(self):
        """仅显示推荐商品 """
        return self.filter(is_flavor=True)

    def count_each_kind(self):
        """以字典形式返回各类茶的件数 """
        result = self.values_list("kind").annotate(
                    count=models.Count("kind"))
        return dict(result)

class Tea(models.Model):
    objects = TeaManager()

    name = models.CharField(u"名称", max_length=255)
    kind = models.CharField(u"种类", max_length=255, choices=TEA_KINDS)
    price = models.IntegerField(u"价格")
    is_recommended = models.BooleanField(
                        u"推荐商品", default=False)

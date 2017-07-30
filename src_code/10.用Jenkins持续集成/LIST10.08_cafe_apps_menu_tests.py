# -*- coding:utf-8 -*-
import unittest
from django.test import TestCase as DjangoTest

from menu.models import Tea
from menu.forms import TeaSearchForm

row = lambda L: (dict(zip(L[0], x)) for x in L[1:])

class TeaManagerTest(DjangoTest):
    def setUp(self):
        datas = (
            ("name", "kind"),
            (u"大吉岭", "english"),
            (u"锡兰红茶", "english"),
            (u"乌龙茶", "chinese"),
            (u"铁观音", "chinese"),
            (u"普洱茶", "chinese"),
            (u"静冈茶", "japanese"),
        )
        for data in row(datas):
            Tea.objects.create(price=100, **data)

    def test_count_each_kind(self):
        result = Tea.objects.count_each_kind()
        self.assertEqual(result, dict(english=2, chinese=3, japanese=1))

class TeaSearchFormTest(unittest.TestCase):
    def test_valid(self):
        """检查输入正常时是否会报错 """
        params = dict(name="foo", kind=["english"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

    def test_either1(self):
        """检查名称和种类都无输入时是否会报错 """
        params = dict()
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), False, form.errors.as_text())
    
    def test_either2(self):
        """检查输入名称后是否会报错 """
        params = dict(name="foo")
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())
    
    def test_either3(self):
        """检查输入种类后是否会报错 """
        params = dict(kind=["english", "chinese"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())

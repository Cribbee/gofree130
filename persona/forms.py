#coding: utf-8
from django import forms

class PersonaForm(forms.Form):
        userId = forms.IntegerField(label=u"用户ID",
                                   max_length=25,
                                   min_length=1,
                                   required=True,
                                   error_messages={'required': "用户Id不能为空"})
        scenicId = forms.IntegerField(label=u"景点Id",
                                   max_length=120,
                                   min_length=1,
                                   required=True,
                                   error_messages={'required': "景点Id不能为空"})

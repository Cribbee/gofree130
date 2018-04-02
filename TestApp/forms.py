# coding: utf-8
from django import forms

class AddForm(forms.Form):
    name = forms.CharField(label=u"用户名zi", max_length=25)
    phone = forms.CharField(label=u"手机号", max_length=20)

class RegisterForm(forms.Form):
        username = forms.CharField(label=u"用户名",
                                   max_length=25,
                                   min_length=3,
                                   required=True,
                                   error_messages={'required': "用户名不能为空"})
        password = forms.CharField(label=u"密码",
                                   widget=forms.PasswordInput,
                                   max_length=120,
                                   min_length=4,
                                   required=True,
                                   error_messages={'required': "密码不能为空"})
        confirm = forms.CharField(label=u"确认密码",
                                  widget=forms.PasswordInput,
                                   max_length=120,
                                   min_length=4,
                                   required=True,
                                   error_messages={'required': "请确认密码"})
        email = forms.EmailField(required=False)
        phone = forms.CharField(label=u"手机号",
                                max_length=20,
                                min_length=11,
                                required=True,
                                error_messages={'required': "手机号不能为空"})
        veri_code = forms.CharField(label=u"短信验证码",
                                    max_length=6,
                                min_length=4,
                                required=True,
                                error_messages={'required': "短信验证码不能为空"})
        #invite_code = forms.CharField(required=True, error_messages={'required': "验证码不能为空"})

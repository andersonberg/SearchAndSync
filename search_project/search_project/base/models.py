from django.db import models
from django import forms
from haystack.forms import SearchForm
# from chosen import forms as chosenforms


class UserBase(models.Model):
    user_name = models.CharField(max_length=200)


class Log(models.Model):
    data_log = models.DateTimeField(auto_now_add=True)
    text_log = models.CharField(max_length=500)


# class UserBaseSearchForm(SearchForm):
#     users_base = chosenforms.ChosenChoiceField(queryset=UserBase.objects.all())
#
#     def search(self):
#         sqs = super(UserBaseSearchForm, self).search()
#
#         return sqs

from django.shortcuts import render
from django.views.generic import ListView
from search_project.base.models import UserBase, Log


class UserBaseList(ListView):
    model = UserBase


class LogList(ListView):
    model = Log

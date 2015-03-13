from django.shortcuts import render
from django.views.generic import ListView
from search_project.base.models import UserBase, Log


class UserBaseList(ListView):
    model = UserBase
    paginate_by = 500


class LogList(ListView):
    model = Log
    paginate_by = 500

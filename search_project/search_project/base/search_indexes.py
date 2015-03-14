__author__ = 'andersonberg'

import datetime
from haystack import indexes
from base.models import UserBase


class UserBaseIndex(indexes.SearchIndex, indexes.Indexable):
    user_name = indexes.CharField(model_attr='user_name')
    text = indexes.CharField(document=True, use_template=True)
    content_auto = indexes.EdgeNgramField(model_attr='user_name')

    def get_model(self):
        return UserBase

    def index_queryset(self, using=None):
        return UserBase.objects.filter()

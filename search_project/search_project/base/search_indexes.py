__author__ = 'andersonberg'

import datetime
from haystack import indexes
from base.models import UserBase


class UserBaseIndex(indexes.SearchIndex, indexes.Indexable):
    id = indexes.IntegerField(model_attr='id')
    text = indexes.CharField(document=True, use_template=True)

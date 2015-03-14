import simplejson as json
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet
from search_project.base.models import UserBase, Log


class UserBaseSearchView(SearchView):

    def get_queryset(self):
        queryset = super(UserBaseSearchView, self).get_queryset()
        return queryset


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))
    suggestions = [result.user_name for result in sqs]
    the_data = json.dumps({
        'results': suggestions
    })

    return HttpResponse(the_data, content_type='application/json')

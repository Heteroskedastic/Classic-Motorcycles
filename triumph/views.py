from django.shortcuts import render
from django.views.generic import ListView

from .models import Triumph, UserSearchHistory

from .triumph import definitions
import datetime


class SearchView(ListView):
    model = Triumph
    context_object_name = 'triumphs'
    template_name = 'triumph_search_results.html'

    def get_queryset(self):
        term = self.request.GET.get('term')
        results = Triumph.objects.filter(term=term)
        if not results:
            results = self.get_new_search_term(term)
        
        if not self.request.user.is_authenticated():
            try:
                self.save_to_history(results)
            except:
                pass

        return results
        
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context.update({'term':self.request.GET.get('term')})
        return context

    def get_new_search_term(self, term):
        for fun in definitions:
            try:
                result = fun(term)
            except:
                return []
            if result:
                results = Triumph(term = term, result = result)
                results.save()
                return [results]
        return []

    def save_to_history(self, results):
        request = self.request
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        term = request.GET.get('term')
        if results:
            for result in results:
                get_ip= UserSearchHistory(ip_address=ipaddress, pub_date = datetime.datetime.now())
                get_ip.term= result.term
                get_ip.result = result.result
                get_ip.save()
        else:
            get_ip= UserSearchHistory(ip_address=ipaddress, pub_date = datetime.datetime.now())
            get_ip.term= term
            get_ip.result = 'No Result'
            get_ip.save()
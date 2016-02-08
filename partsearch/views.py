import datetime

import vinlookup.bsa
import vinlookup.triumph

from django.shortcuts import render
from django.views.generic import ListView

from .models import Search, UserSearchHistory

class SearchView(ListView):
    model = Search
    context_object_name = 'parts'
    template_name = 'search_results.html'

    def get_queryset(self):
        brand = self.request.GET.get('brand')
        term = self.request.GET.get('term')
        print("brand="+brand)
        print("term="+term)
        results = Search.objects.filter(brand=brand, term=term)
        if not results:
            if brand == "bsa":
                results = vinlookup.bsa.decode(term)
            elif brand == "triumph":
                import pdb
                pdb.set_trace()
                results = vinlookup.triumph.decode(term)
            else:
                raise Exception("Invalid brand!")
        
        if not self.request.user.is_authenticated():
            try:
                self.save_to_history(results)
            except:
                pass

        return results
        
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context.update({'brand':self.request.GET.get('brand'),
                        'term':self.request.GET.get('term')})
        return context

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
import datetime

import vinlookup.bsa
import vinlookup.triumph

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView


from .models import Part, Search, UserSearchHistory, UserFeedback

class SearchView(ListView):
    model = Search
    context_object_name = 'parts'
    template_name = 'search_results.html'

    def get_queryset(self):
        brand = self.request.GET.get('brand')
        term = self.request.GET.get('term')
        search, created = Search.objects.get_or_create(brand=brand, term=term)
        results = None
        if not created:
            if brand == "bsa":
                results = vinlookup.bsa.decode(term)
            elif brand == "triumph":
                results = vinlookup.triumph.decode(term)
            else:
                raise Exception("Invalid brand!")
            for result in results:
                part, created = Part.objects.get_or_create(description=str(result))
                search.results.add(part)
        else:
            results = search.results
        search.save()
        
        self.request.session['last_search_id'] = search.id
        
        if not self.request.user.is_authenticated():
            try:
                self.save_to_history(search)
            except:
                pass

        return results
        
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context.update({'brand':self.request.GET.get('brand'),
                        'term':self.request.GET.get('term')})
        return context

    def save_to_history(self, search):
        request = self.request
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        term = request.GET.get('term')
        get_ip= UserSearchHistory(ip_address=ipaddress, pub_date = datetime.datetime.now())
        if search:
            get_ip.search = search
        get_ip.save()
        
def SaveFeedback(request):
    user_feedback = UserFeedback.objects.create(
        comment=request.POST.get('feedback'),
        search=Search.objects.get(pk=request.session['last_search_id']),
        date=timezone.now())
    return HttpResponse('Feedback received succesfully!')
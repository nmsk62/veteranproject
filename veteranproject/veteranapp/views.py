from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Remember, Ad


def index(request):
    #   Словарь для передачи данных в шаблон
    text_head = ''
    remember = Remember.objects
    num_remember = Remember.objects.count()
    ads = Ad.objects.all()
    context = {'text_head': text_head,
               'remember': remember, 'num_remember': num_remember, 'ad_list': ads}
    # nередача словаря context с данными в шаблон
    return render(request, 'veteranapp/index.html', context)


def about(request):
    return render(request, 'veteranapp/about.html')


def contact(request):
    return render(request, 'veteranapp/contact.html')


class RememberListView(ListView):
    model = Remember


class RememberDetailView(DetailView):
    model = Remember


class AdView(View):
    ''' вывод записей'''

    def get(self, request):
        ads = Ad.objects.all()
        return render(request, 'veteranapp/ad_list.html', {'ad_list': ads})


class AdDetail(View):
    '''отдельная страница'''

    def get(self, request, pk):
        ad = Ad.objects.get(id=pk)
        return render(request, 'veteranapp/ad_detail.html', {'ad': ad})

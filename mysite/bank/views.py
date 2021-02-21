from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

from .models import account
from .models import history


class user(generic.ListView):
    template_name='bank/user.html'
    context_object_name='account_list'
    def get_queryset(self):
        return account.objects.all()

class transferprocess(generic.DetailView):
    model = account
    template_name = 'bank/transferprocess.html'   

class transactions(generic.ListView):
    template_name='bank/history.html'
    context_object_name='tans_his'
    def get_queryset(self):
        return history.objects.all()    
    
def index(request):   
    return render(request, 'bank/index.html')

def about(request):
    return render(request,'bank/about.html')    



class transfernow(generic.ListView):
    template_name='bank/transfernow.html'
    context_object_name='account_list'
    def get_queryset(self):
        return account.objects.all()

def sucess(request):
    return render(request,'bank/sucess.html')




def transfer(request, account_id):
    fromid=get_object_or_404(account, pk=account_id)
    toid= account.objects.get(pk=int(request.POST['toid']))
    fund=int(request.POST['fund'])
    fromid.amount=fromid.amount-fund   
    fromid.save()

    toid.amount=toid.amount+fund
    toid.save()

    h=history(sender=fromid.user_name,receiver=toid.user_name,amount=fund)
    h.save()
    return HttpResponseRedirect(reverse('bank:sucess'))
    

    


    
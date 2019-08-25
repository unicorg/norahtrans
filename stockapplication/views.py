from django.shortcuts import render

# Create your views here.
from .models import Stock
from .models import Investor
from .models import Bond

# Create your views here.
def index(request):
    stockObject = Stock.objects.all()
    BondObject = Bond.objects.all()
    InvestorObject = Investor.objects.all()
    context = {'investor': InvestorObject, 'stock': stockObject, 'bond': BondObject}
    return render(request, 'stockapplication/index.html', context)

def StockCreate(request):
    stockObject = Stock.objects.all()
    BondObject = Bond.objects.all()
    InvestorObject = Investor.objects.all()
    context = {'investor': InvestorObject, 'stock': stockObject, 'bond': BondObject}
    return render(request, 'stockapplication/StockCreate.html', context)

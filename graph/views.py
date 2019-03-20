from django.shortcuts import render
from .models import Stocks
# Create your views here.

def homeView(request):
    company='TVS'
    if request.method=='POST':
        print('hi')
        company = request.POST['company']
        print(company)

    stocks = Stocks.objects.filter(company=company)
    print(stocks)
    actual = []
    predicted = []
    print(stocks[0].timestamp.timestamp())
    for stock in stocks:
        actual.append([stock.timestamp.timestamp(), stock.actual_price])
        predicted.append(([stock.timestamp.timestamp(), stock.predicted_price]))
    # data = [[3,1],[2,5],[1,1]]
    arg = {'actual':actual, 'predicted':predicted}
    return render(request,'test_data.html',arg)
    # return render(requests, 'home.html')

def send_company_stocks_price(request):
    if request.method=='POST':
        print('hi')

    return render(request, 'home.html')
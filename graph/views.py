from django.shortcuts import render
import csv, time
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def history(request):
    if request.method=='POST':
        company = request.POST['company']
        csvFile = company + ".csv"
        
        file = open(csvFile)
        reader = csv.reader(file)
        data = list(reader)
        prices = []
        for row in data:
            temp = []
            temp.append(datetime.timestamp(datetime.strptime((row[0]) + " 09:30:00 +0000", '%Y-%m-%d %H:%M:%S %z')) * 1000)
            temp.append(float(row[1]))
            prices.append(temp)

        arg = {'symbol':company, 'prices':prices, 'company':company}
        return render(request, 'history.html', arg)

    return render(request, 'history.html')

def predict(request):
    if request.method=='POST':
        company = request.POST['company']
        csvFile = company + "predict.csv"
        
        # 1. get real time tweets of that day into MSFTtweets.json

        # 2. send tweets to model and get predicted diff
        
        # 3. get real time stock price
        
        # 4. compute predicted val

        # all of the above, which is machine learning part is in another repo

        # for now, let's take some dummy values
        todayPrice = 117.66 
        predictPrice = 111.21

        if(todayPrice > predictPrice):
            arrowCode = '&#8595;'
            sign = '-'
            diff = format(todayPrice - predictPrice, '.2f')
        else:
            arrowCode = '&#8593;'
            sign = '+'
            diff = format(predictPrice - todayPrice, '.2f')

        file = open(csvFile)
        reader = csv.reader(file)
        data = list(reader)
        actual = []
        predict = []
        for row in data:
            temp1 = []
            temp2 = []
            temp1.append(datetime.timestamp(datetime.strptime((row[0]) + " 09:30:00 +0000", '%Y-%m-%d %H:%M:%S %z')) * 1000)
            temp1.append(float(row[1]))
            temp2.append(datetime.timestamp(datetime.strptime((row[0]) + " 09:30:00 +0000", '%Y-%m-%d %H:%M:%S %z')) * 1000)
            temp2.append(float(row[2]))
            actual.append(temp1)
            predict.append(temp2)

        arg = {'actual':actual, 'predict':predict, 'todayPrice':todayPrice, 'predictPrice':predictPrice, 
        'arrowCode':arrowCode, 'sign':sign, 'diff':diff, 'company':company}
        return render(request,'predict.html',arg)

    return render(request, 'predict.html')
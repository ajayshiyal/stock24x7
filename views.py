from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from myweb.models import *
import random
from myweb.aapleww import get_weekly_stock_data
from myweb.aaplem import get_monthly_stock_data
from myweb.aapley import get_20_year_stock_data

from myweb.aaplelive import get_live_stock_data
from myweb.relw import get_weekly_stock_data
from myweb.relm import get_monthly_stock_data
from myweb.rely import get_20_year_stock_data
from myweb.rellive import get_live_stock_data
import yfinance as yf
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())
def candidateRegistrationForm(request):
    res=render(request,'registration_form.html')
    return res
def candidateRegistration(request):
    if request.method=='POST':
        email=request.POST.get('email')
        #Check if the user already exists
        if(len(Candidate.objects.filter(email=email))):
            userStatus=1
        else:
            candidate=Candidate()
            candidate.email=email
            candidate.password=request.POST['password']
            candidate.mobile=request.POST.get('mobile')
            candidate.name=request.POST['name']
            candidate.email=request.POST['email']
            candidate.save()
            userStatus=2
    else:
        userStatus=3 #Request method is not POST
    context={
        'userStatus':userStatus
    }
    res=render(request,'registration.html',context)
    return res

def loginView(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        candidate=Candidate.objects.filter(email=email,password=password)
        if len(candidate)==0:
            loginError="Invalid Username or Password"
            res=render(request,'login.html',{'loginError':loginError})
        else:
            #login Success
            request.session['mobile']=candidate[0].mobile
            request.session['name']=candidate[0].name
            request.session['email']=candidate[0].email
            res=HttpResponseRedirect("home")
    else:
        res=render(request,'login.html')
    return res


def candidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    else:
        res=render(request,'home1.html')
    return res
def logoutView(request):
    if 'name' in request.session.keys():
        del request.session['email']
        del request.session['name']
    return HttpResponseRedirect("login")


def home2(request):

     res=render(request,'home1.html')
     return res

def aaple(request):

     res=render(request,'aaple.html')
     return res

from django.shortcuts import render
from myweb.aapleww import get_weekly_stock_data

def aaplew(request):
    symbol = "AAPL"  # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'aaplew.html', {'stock_data': stock_data_with_dates})

     

     


def aaplem(request):
    symbol = "AAPL"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'aaplem.html', {'stock_data': stock_data_with_dates})
     
     
def aapley(request):
    symbol = "AAPL"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'aapley.html', {'stock_data': stock_data_with_dates})


def abc(request):
    symbol = "AAPL"  # Symbol for Apple (Replace with the stock symbol you want to fetch)
    stock_data = get_live_stock_data(symbol)

    live_price2 = stock_data["Close"].iloc[-1]
    close_price2 = stock_data["Close"].iloc[-1]

    return render(request, 'home1.html', {'live_price2': live_price2, 'close_price2': close_price2})




#stockchart
def applechart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('AAPL', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'applechart.html', {'chart_data': chart_data})




#relance stock data
def rel(request):

     res=render(request,'rel.html')
     return res
def relw(request):
    symbol = "RELIANCE.NS" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'relw.html', {'stock_data': stock_data_with_dates})



def relm(request):
    symbol = "RELIANCE.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'relm.html', {'stock_data': stock_data_with_dates})
     


def rely(request):
    symbol = "RELIANCE.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'rely.html', {'stock_data': stock_data_with_dates})



def relchart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('RELIANCE.NS', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'relchart.html', {'chart_data': chart_data})

    


# HDFCBANK DATA


def hdfc(request):
     res=render(request,'hdfc.html')
     return res



def hdfcw(request):
    symbol = "HDFCBANK.BO" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'hdfcw.html', {'stock_data': stock_data_with_dates})


def hdfcm(request):
    symbol = "HDFCBANK.BO"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'hdfcm.html', {'stock_data': stock_data_with_dates})



def hdfcy(request):
    symbol = "HDFCBANK.BO"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'hdfcy.html', {'stock_data': stock_data_with_dates})


def hdfcchart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('HDFCBANK.BO', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'relchart.html', {'chart_data': chart_data})




#ICICIBANK
def icici(request):
     res=render(request,'icici.html')
     return res



def iciciw(request):
    symbol = "ICICIBANK.BO" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'iciciw.html', {'stock_data': stock_data_with_dates})


def icicim(request):
    symbol = "ICICIBANK.BO"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'icicim.html', {'stock_data': stock_data_with_dates})



def iciciy(request):
    symbol = "ICICIBANK.BO"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'iciciy.html', {'stock_data': stock_data_with_dates})


def icicichart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('ICICIBANK.BO', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'relchart.html', {'chart_data': chart_data})




   #TCS.NS
def tcs(request):
     res=render(request,'tcs.html')
     return res

def tcsw(request):
    symbol = "TCS.NS" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'tcsw.html', {'stock_data': stock_data_with_dates})






def tcsm(request):
    symbol = "TCS.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'tcsm.html', {'stock_data': stock_data_with_dates})



def tcsy(request):
    symbol = "TCS.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'tcsy.html', {'stock_data': stock_data_with_dates})

def tcschart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('TCS.NS', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'tcschart.html', {'chart_data': chart_data})





   #ITC
def itc(request):
     res=render(request,'itc.html')
     return res

def itcw(request):
    symbol = "ITC.NS" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'itcw.html', {'stock_data': stock_data_with_dates})






def itcm(request):
    symbol = "ITC.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'itcm.html', {'stock_data': stock_data_with_dates})



def itcy(request):
    symbol = "ITC.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'itcy.html', {'stock_data': stock_data_with_dates})

def itcchart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('itc.NS', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'itchart.html', {'chart_data': chart_data})




#BHARTI AITEL

def airtel(request):
     res=render(request,'airtel.html')
     return res

def airtelw(request):
    symbol = "BHARTIARTL.NS" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'airtelw.html', {'stock_data': stock_data_with_dates})


def airtelm(request):
    symbol = "BHARTIARTL.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'airtelm.html', {'stock_data': stock_data_with_dates})



def airtely(request):
    symbol = "BHARTIARTL.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'airtely.html', {'stock_data': stock_data_with_dates})

def aitlchart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('BHARTIARTL.NS', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'airtlchart.html', {'chart_data': chart_data})



#TATAMOTERS

def tata(request):
     res=render(request,'tata.html')
     return res

def tataw(request):
    symbol = "TATAMOTORS.NS" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'tataw.html', {'stock_data': stock_data_with_dates})


def tatam(request):
    symbol = "TATAMOTORS.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'tatam.html', {'stock_data': stock_data_with_dates})



def tatay(request):
    symbol = "TATAMOTORS.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'tatay.html', {'stock_data': stock_data_with_dates})





def tatastock(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("TATAMOTORS.NS", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)


def tatachart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('TATAMOTORS.NS', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'tatachart.html', {'chart_data': chart_data})






 #BPCL

def bpcl(request):
     res=render(request,'bpcl.html')
     return res

def bpclw(request):
    symbol = "BPCL.NS" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'bpclw.html', {'stock_data': stock_data_with_dates})


def bpclm(request):
    symbol = "BPCL.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'bpclm.html', {'stock_data': stock_data_with_dates})



def bpcly(request):
    symbol = "BPCL.NS"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'bpcly.html', {'stock_data': stock_data_with_dates})


def bpclstock(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("BPCL.NS", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)




def bpclchart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('BPCL.NS', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'bpclchart.html', {'chart_data': chart_data})













#sbi

def sbi(request):
     res=render(request,'sbi.html')
     return res

def sbiw(request):
    symbol = "SBIN.BO" # Replace with the stock symbol you want to fetch
    stock_data = get_weekly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'sbiw.html', {'stock_data': stock_data_with_dates})


def sbim(request):
    symbol = "SBIN.BO"  # Replace with the stock symbol you want to fetch
    stock_data = get_monthly_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'sbim.html', {'stock_data': stock_data_with_dates})



def sbiy(request):
    symbol = "SBIN.BO"  # Replace with the stock symbol you want to fetch
    stock_data = get_20_year_stock_data(symbol)

    # Extract dates, open, close, low, high, and volume data
    dates = stock_data.index.strftime("%Y-%m-%d")
    open_prices = stock_data["Open"].tolist()
    close_prices = stock_data["Close"].tolist()
    low_prices = stock_data["Low"].tolist()
    high_prices = stock_data["High"].tolist()
    volumes = stock_data["Volume"].tolist()

    stock_data_with_dates = list(zip(dates, open_prices, close_prices, low_prices, high_prices, volumes))

    return render(request, 'sbiy.html', {'stock_data': stock_data_with_dates})

def sibstock(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("SBIN.BO", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)


def sbichart(request):
    # Fetch live Apple stock data
    apple_data = yf.download('TATAMOTORS.NS', period='1d', interval='1m')
    # Extract relevant data (e.g., close prices)
    chart_data = apple_data['Close'].tolist()
    return render(request, 'sbichart.html', {'chart_data': chart_data})













def candidateHome(request):
    symbol = "RELIANCE.NS"  # Symbol for Apple (Replace with the stock symbol you want to fetch)
    stock_data = get_live_stock_data(symbol)

    live_price1 = stock_data["Close"].iloc[-1]
    close_price1 = stock_data["Close"].iloc[-1]


    

    symbol = "ICICIBANK.BO"  # Symbol for Apple (Replace with the stock symbol you want to fetch)
    stock_data = get_live_stock_data(symbol)
    live_price4 = stock_data["Close"].iloc[-1]
    close_price4 = stock_data["Close"].iloc[-1]

    symbol = "TCS.NS"  # Symbol for Apple (Replace with the stock symbol you want to fetch)
    stock_data = get_live_stock_data(symbol)
    live_price5 = stock_data["Close"].iloc[-1]
    close_price5 = stock_data["Close"].iloc[-1]

    symbol = "ITC.NS"  # Symbol for Apple (Replace with
    stock_data = get_live_stock_data(symbol)
    live_price6 = stock_data["Close"].iloc[-1]
    close_price6 = stock_data["Close"].iloc[-1]

    
    symbol = "BHARTIARTL.NS"  # Symbol for Apple (Replace with
    stock_data = get_live_stock_data(symbol)
    live_price7 = stock_data["Close"].iloc[-1]
    close_price7 = stock_data["Close"].iloc[-1]


    symbol = "TATAMOTORS.NS"  # Symbol for Apple (Replace with
    stock_data = get_live_stock_data(symbol)
    live_price8 = stock_data["Close"].iloc[-1]
    close_price8 = stock_data["Close"].iloc[-1]

    symbol = "BPCL.NS"  # Symbol for Apple (Replace with 
    stock_data = get_live_stock_data(symbol)
    live_price9 = stock_data["Close"].iloc[-1]
    close_price9 = stock_data["Close"].iloc[-1]

    symbol = "SBIN.BO"  # Symbol for Apple (Replace with the stock symbol you want to fetch)
    stock_data = get_live_stock_data(symbol)
    live_price10 = stock_data["Close"].iloc[-1]
    close_price10 = stock_data["Close"].iloc[-1]
            
    
        
    return render(request, 'home1.html', {'live_price1': live_price1, 'close_price1': close_price1,'live_price4': live_price4, 'close_price4': close_price4,'live_price5': live_price5, 'close_price5': close_price5,'live_price6': live_price6, 'close_price6': close_price6,'live_price7': live_price7, 'close_price7': close_price7,'live_price8': live_price8, 'close_price8': close_price8,'live_price9': live_price9, 'close_price9': close_price9,'live_price10': live_price10, 'close_price10': close_price10})
















# Create your views here.





from django.http import JsonResponse
from .py import get_data_from_api

def get_data(request):
    try:
        data = get_data_from_api()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




#stock info


def stock_info(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("BHARTIARTL.NS", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)




def applestockinfo(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("AAPL", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)





def relaince(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("RELIANCE.NS", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)

#icicibank
def icicistock(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("ICICIBANK.BO", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)


#Hdfc stock info

def hdfcstock(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("HDFCBANK.BO", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)




def tcsstock(request):
    try:
        # Retry strategy for HTTP requests
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))

        # Fetch stock data for Bharati Airtel
        ticker = yf.Ticker("TCS.NS", session=session)
        info = ticker.info

        # Extract required information
        day_range = info.get('dayLow', 'N/A'), info.get('dayHigh', 'N/A')
        fifty_two_week_range = info.get('fiftyTwoWeekLow', 'N/A'), info.get('fiftyTwoWeekHigh', 'N/A')
        bid = info.get('bid', 'N/A')
        ask = info.get('ask', 'N/A')
        volume = info.get('volume', 'N/A')
        pe_ratio = info.get('forwardPE', 'N/A')


        context = {
            'day_range': day_range,
            'fifty_two_week_range': fifty_two_week_range,
            'bid': bid,
            'ask': ask,
            'volume': volume,
             'pe_ratio': pe_ratio


        }
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        error_message = f"Connection Error: {str(e)}"
        context = {
            'error_message': error_message
        }
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        context = {
            'error_message': error_message
        }

    return render(request, 'top.html', context)

from django.urls import path
from myweb.views import *
import yfinance as yf

app_name='myweb'

urlpatterns = [
    path('',welcome),
    path('new-candidate',candidateRegistrationForm,name='registrationForm'),
    path('store-candidate',candidateRegistration,name='storeCandidate'),
    path('login',loginView,name='login'),
    path('home',candidateHome, name='home'),
    path('logout',logoutView,name='logout'),
    path('home2',home2,name='home2'),
    path('aaple',aaple,name='aaple'),
    path('weekly_stock_data/', aaplew, name='aaplew'),
      
    
    path('monthly_stock_data/', aaplem, name='aaplem'),
    path('applechar/', applechart,name='applechart'),

    path('aapley',aapley,name='aapley'),
    path('twenty_year_stock_data/', aapley, name='aapley'),
    path('twenty_year_stock_data/', aapley, name='aapley'),
    path('aaplestockinfo/', applestockinfo, name='applestockinfo'),
      
      #relaince data
    path('rel',rel,name='rel'),
    path('relianceweek/', relw, name='relw'),      
    path('reliancemonth/', relm, name='relm'),
    path('relianceyear/', rely, name='rely'),
    path('reliance/', abc, name='abc'),
    path('reliancestockinfo/',relaince , name='relsstockinfo'),
     path('relchart/',relchart , name='relchat'),
       #HDFCBANK PATH
    path('HFCBANK/',hdfc,name='hdfc'),
    path('HDFCweek/', hdfcw, name='hdfcw'),
    path('HDFCmonth/', hdfcm, name='hdfcm'),
    path('HDFCyear/', hdfcy, name='hdfcy'),
    path('hdfc/', hdfcstock, name='hdfcstock'),
     path('hdfcchar/',hdfcchart , name='hdfcchart'),
     #ICICI BANK
    path('ICICIBANK/',icici,name='icici'),
    path('ICICIweek/', iciciw, name='iciciw'),
    path('ICICImonth/', icicim, name='icicim'),
    path('ICICIyear/', iciciy, name='iciciy'),
    path('icici/', icicistock, name='icicistock'),

    path('icicichart/',icicichart , name='icicichar'),
     #TCS.NS
    path('TCS/',tcs,name='tcs'),
    path('TCSweek/', tcsw, name='tcsw'),
    path('TCSmonth/', tcsm, name='tcsm'),
    path('TCSyear/', tcsy, name='tcsy'),
    path('tcs/', tcsstock, name='tcsstock'),
    path('tcschat/', tcschart, name='tcschart'),

    #ITC
    path('ITC/',itc,name='itc'),
    path('ITCweek/', itcw, name='itcw'),
    path('ITCmonth/', itcm, name='itcm'),
    path('ITCyear/', itcy, name='itcy'),
    path('itcchart/', itcchart, name='itcchart'),
    #airtel
    path('AIRTEL/',airtel,name='airtel'), 
    path('AIRTELweek/', airtelw, name='airtelw'),
    path('AIRTELmonth/', airtelm, name='airtelm'),
    path('AIRTELyear/', airtely, name='airtely'),
    path('bhartiaitelstock/',stock_info , name='airtel'), 
    path('aitlchart/', aitlchart, name='aitlchart'),
    #TATAMOTORS

    path('TATA/',tata,name='tata'), 
    path('TATAweek/', tataw, name='tataw'),
    path('TATAmonth/', tatam, name='tatam'),
    path('TATAyear/', tatay, name='tatay'), 
     path('tatastock/', tatastock, name='tatastock'),   
    path('tatachart/', tatachart, name='tatachart'),
    #bcpl
    path('BCPL/',bpcl,name='bpcl'),
    path('BPCLweek/', bpclw, name='bpclw'),
    path('BPCLmonth/', bpclm, name='bpclm'),
    path('BPCLyear/', bpcly, name='bpcly'), 
    path('bpclstock/', bpclstock, name='bpclstock'), 
    path('bpclchart/', bpclchart, name='bpclchart'),
    
    #sbi
    path('SBI/',sbi,name='sbi'),
    path('SBIweek/', sbiw, name='sbiw'),
    path('SBImonth/', sbim, name='sbim'),
    path('SBIyear/', sbiy, name='sbiy'), 
    path('sbistock/', sibstock, name='sbistock'), 
    path('sbichart/', sbichart, name='sbichart'),


    path('lose/',get_data , name='lose'), 




    #stock info bharti airtel

    


              
    
    
    
    

]
      
    
      


import yfinance as yf
border="==============================================" 
stockoption=['1. Choose New Stock','2. Continue with Stock', '3. Exit']
stockactivities=['1. History', '2. Actions', '3. Dividends', '4. Splits', '5. Quarterly Financials', '6. Major Holders', '7. Institutional Holders', '8. Quarterly Balance Sheet', '9. Quarterly Cashflow', '10. Quarterly Earnings', '11. Sustainability', '12. Recommendations', '13. Is In', '14. Options', '15. News', '16. Calendar', '17. Exit']
stockchoice=input("Enter the stock symbol you would like to review: ")
cycle=2
while (cycle<10):
     
     stock = yf.Ticker(stockchoice)
     print("You have chosen: ", stockchoice)
     print("Here is some basic information about", stockchoice)
     info=stock.info
     print("Long Business Summary: ", info['longBusinessSummary'])
     print(border)
     print('\n')
     print("Which of the following would you like to do:")
     for i in stockoption:
         print(i)
 
     optionchoice=int(input("Please choose a number: \n"))
     
     if optionchoice==1:
        stockchoice=input("Enter the stock symbol you would like to review: ")
        cycle=cycle+1
     elif optionchoice==2:
         while (cycle <10):
             print(f'\n{border}')
             print("Please choose what information you would like to see: ")
             print(border)
             for x in stockactivities:
                 print(x)
             optioninput=int(input("Enter the number of your choice: "))
             if optioninput == 1:
                 hist=stock.history(period="Max")
                 print(hist)
             elif optioninput==2:
                 action=stock.actions
                 print(action)
             elif optioninput==3:
                 div=stock.dividends
                 print(div)
             elif optioninput==4:
                 spl=stock.splits
                 print(spl)
             elif optioninput==5:
                 qf=stock.quarterly_financials
                 print(qf)
             elif optioninput==6:
                 mh=stock.major_holders
                 print(mh)
             elif optioninput==7:
                 ih=stock.institutional_holders
                 print(ih)
             elif optioninput==8:
                 qbs = stock.quarterly_balance_sheet
                 print(qbs)
             elif optioninput==9:
                 qcf = stock.quarterly_cashflow
                 print(qcf)
             elif optioninput==10:
                 qe = stock.quarterly_earnings
                 print(qe)
             elif optioninput==11:
                 sus=stock.sustainability
                 print(sus)
             elif optioninput==12:
                 rec = stock.recommendations
                 print(rec)
             elif optioninput==13:
                 tisin=stock.isin
                 print(tisin)
             elif optioninput==14:
                 op=stock.options
                 print(op)
             elif optioninput==15:
                 nw=stock.news
                 for x in range(len(nw)):
                     print(border)
                     print('Title: ',nw[x]['title'])
                     print('Publisher; ', nw[x]['publisher'])
                     print('Link: ', nw[x]['link'])
                     print(border)
  
                ## print(nw)
             elif optioninput==16:
                 cal=stock.calendar
                 print(cal)
             elif optioninput==17:
                 print(border)
                 print("What would you like to do next: ")
                 # print(border)
                 # for x in activities:
                 #     print(x)
                 break
             ##choice=int(input("Enter the number of your choice here: "))
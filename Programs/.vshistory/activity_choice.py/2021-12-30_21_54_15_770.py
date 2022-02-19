
import University.globals as globals
import json
import yfinance as yf
import Programs.plots as plots
import datetime as dt
import Programs.activity_choice

#============================================
#Host Program Options
#============================================
def host_start(userrecognized):
    if userrecognized==True:
        print(f'Its Ya Boy Atom....as usual\nYou know what time it is')
        print(globals.border)
    elif userrecognized==False:
        print(globals.border)
        print(f"\nMy Name is {globals.cname}")
        print("\nLet's play a game! ")
        print(globals.border)
    else:
        print('You have not been authenticated')

#============================================
#Stock Program Options
#============================================
def activity_start(jsonfile):
    print(globals.border)
    print("What would you like to do: ")
    print(globals.border)
    with open(jsonfile) as open_user_file:
            username_check=json.load(open_user_file)
    for x in username_check['start']:
        print(x)
    choice=int(input("Enter the number of your choice here: "))
    return(choice)

#============================================
#Stock Program Options
#============================================

def stock_activity_start(jsonfile):
    print(globals.border)
    print("What would you like to do: ")
    print(globals.border)
    with open(jsonfile) as open_user_file:
        username_check = json.load(open_user_file)
    for x in username_check['stockoption']:
        print(x)
    choice = int(input("Enter the number of your choice here: "))
    return(choice)

def get_stock_symbol(pname):
    stockchoice = input(f"\nEnter the stock symbol you would like to review {pname}: ")
    stockchoice = stockchoice.upper()
    return(stockchoice)

def get_basic_stock_info(stockchoice):
    stock = yf.Ticker(stockchoice)
    print("You have chosen: ", stockchoice)
    print("Here is some basic information about", stockchoice)
    info = stock.info
    print("Long Business Summary: ", info['longBusinessSummary'])
    print(globals.border)
    print('\n')


def stock_option_input(jsonfile,pname):
    print(globals.border)
    print("What would you like to do: ")
    print(globals.border)
    with open(jsonfile) as open_user_file:
        username_check = json.load(open_user_file)
    for x in username_check['stock_activities']:
        print(x)
    choice = int(input(f"Enter the number of your choice here, {pname}:\n{globals.prompt} "))

    return(choice)

def stock_info_get(optioninput,stockchoice,pname):
    stock = yf.Ticker(stockchoice)
    if optioninput == 1:
        hist = stock.history(period="Max")
        print(f'\nStock History:\n{hist}')
    elif optioninput == 2:
        action = stock.actions
        print(f'\nStock Action:\n{action}')
    elif optioninput == 3:
        div = stock.dividends
        print(f'\nStock Dividends: \n{div}')
    elif optioninput == 4:
        spl = stock.splits
        print(f'\nStock Splits: \n{spl}')
    elif optioninput == 5:
        qf = stock.quarterly_financials
        print(f'\nStock Quarterly Financials: \n{qf}')
    elif optioninput == 6:
        mh = stock.major_holders
        print(f'\nStock Major Holders: \n{mh}')
    elif optioninput == 7:
        ih = stock.institutional_holders
        print(f'\nStock Institutional Holders: \n{ih}')
    elif optioninput == 8:
        qbs = stock.quarterly_balance_sheet
        print(f'\nStock Quarterly Balance Sheet: \n{qbs}')
    elif optioninput == 9:
        qcf = stock.quarterly_cashflow
        print(f'\nStock Quarterly Cashflow: \n{qcf}')
    elif optioninput == 10:
        qe = stock.quarterly_earnings
        print(f'\nStock Quarterly Earnings: \n{qe}')
    elif optioninput == 11:
        sus = stock.sustainability
        print(f'\nStock Sustainability: \n{sus}')
    elif optioninput == 12:
        rec = stock.recommendations
        print(f'\nStock Recommendations: \n{rec}')
    elif optioninput == 13:
        tisin = stock.isin
        print(f'\nStock Is In: \n{tisin}')
    elif optioninput == 14:
        op = stock.options
        for x in range(len(op)):
            print(globals.border)
            print('Option Years: ', op[x])
    elif optioninput == 15:
        nw = stock.news
        for x in range(len(nw)):
            print(globals.border)
            print('Title: ', nw[x]['title'])
            print('Publisher: ', nw[x]['publisher'])
            print('Link: ', nw[x]['link'])
            print(globals.border)
    elif optioninput == 16:
        cal = stock.calendar
        print(f'\nStock Calendar: \n{cal}')
    elif optioninput == 17:
        print(globals.border)
        # print("What would you like to do next: ")

def compare_get(stockchoice,pname):
    comp = '1'
    stocks = []
    start=''
    end = dt.datetime.today()
    while comp == '1':
        co = int(input(f"Enter the number of stocks you would like to compare, {pname}: "))
        plots.stock_plot1(co,stocks,pname)
        print("What would you like todo next:")
        stocks,comp = compare_exit(stocks, comp)
    return (stocks,comp)

def compare_exit(stocks,comp):
    compare = input(f'1. Add Stocks\n2. Start New Stock List\n3. Exit \n{globals.prompt}')
    if compare == '1':
        comp == '1'
    elif compare == '2':
        del stocks[0]
        comp = 2

    elif compare == '3':
        del stocks[0]
        stocks = []
        print(globals.border)
        comp=3
    return(stocks,comp)

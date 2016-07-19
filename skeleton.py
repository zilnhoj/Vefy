import json
from piwikapi.analytics import PiwikAnalytics

# you may need to add more parameters
def doSomething(dateRange, period, token):
    # you don't need to change any of these
    pa = PiwikAnalytics()
    pa.set_api_url('https://analytics.ida.digital.cabinet-office.gov.uk/index.php')
    pa.set_id_site(1) # 1 is the side ID you want to log to
    pa.set_format('json')
    pa.set_period(period)
    pa.set_date(dateRange)
    pa.set_parameter('module', 'API')
    pa.set_parameter('token_auth', token)

    # the default is 100. For all results, set to -1. Using 1 when you're building
    # script is helpful for debugging when you're writing your script.
    pa.set_parameter('filter_limit', '1')

    # change these to the method and segment you need
    pa.set_method('Actions.getPageTitles')
    pa.set_segment('referrerName=@universal-credit')



    visits = json.loads(pa.send_request())
    # print the json to see the labels of the fields you need to retrieve
    print json.dumps(visits, indent=4)

    # extract the data from the json. You'll need to put it in a loop when
    # you have more than one item in visits
    pageTitle = visits[0]['label']
    uniques = visits[0]['sum_daily_nb_uniq_visitors']
    print pageTitle, uniques

# sets default values so you don't need to keep inputting dates while you're
# writing the script
dateRange = raw_input('Enter date(s)')
if len(dateRange)<1 : dateRange='yesterday'
period = raw_input('Enter period')
if len(period)<1 : period ='week'

# the file needs to be in the same directory as the script

with open("token.txt") as ft:
    token = ft.read()
print token

doSomething(dateRange, period, token)

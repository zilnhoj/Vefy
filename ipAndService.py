
import json
from piwikapi.analytics import PiwikAnalytics




def getVisitDetails(dateRange, period):
    pa = PiwikAnalytics()
    pa.set_api_url('https://analytics.ida.digital.cabinet-office.gov.uk/index.php')
    pa.set_id_site(1) # 1 is the side ID for live
    pa.set_format('json')
    pa.set_period(period)
    pa.set_date(dateRange)
    pa.set_method('Live.getLastVisitsDetails')
    pa.set_parameter('module', 'API')
    pa.set_parameter('expanded', '1')
    pa.set_segment('customVariableValue2=@XXX;pageTitle=@Success - REGISTER_WITH_IDP')
    # custom variable 2 is IDP
    pa.set_parameter('countVisitorsToFetch', '-1')
    # -1 is 'get all of them'
    pa.set_parameter('token_auth', 'XXX')

    IDP = json.loads(pa.send_request())
    #print json.dumps(fails, indent=4)

    print len(IDP)

    for item in IDP:
        try:
            details = list()
            visitorIP = item["visitIp"]
            details.insert(0, visitorIP)
            cv1 = item["customVariables"]["1"]["customVariableValue1"]
            details.insert(0,cv1)
            opSys = item["operatingSystem"]
            details.append(opSys)
            visits = item["visitCount"]
            details.append(visits)
            days = item["daysSinceFirstVisit"]
            details.append(days)

            print details
        except:
            print 'Ooops!'





dateRange = raw_input('Enter date(s)')
if len(dateRange)<1 : dateRange='2016-06-07,2016-06-08'
period = raw_input('Enter period')
if len(period)<1 : period ='range'



getVisitDetails(dateRange, period)

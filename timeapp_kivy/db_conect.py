import requests
from requests.auth import HTTPBasicAuth
cred = []
DOMAIN = 'http://3.65.19.203'

def get_login(username, password):
    login = requests.get(f'{DOMAIN}/time/', auth=HTTPBasicAuth(username, password))
    credentials = {"PASWORD": password, "USERNAME": username, "login": login}
    if login.status_code == 200:
        cred.append(credentials)
    return credentials

def get_time():
    ''' Request GET '''
    x = cred[0]
    get_request = requests.get(f'{DOMAIN}/time/', auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"])).json()
    return get_request

def put_time(widget_id, ora):
    ''' Request Put '''
    x = cred[0]
    put_request = requests.put(f'{DOMAIN}/time/{str(widget_id)}/', data={'ore_lavorative': ora}, auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"]) )
    return put_request

def delete_time(tempo_id):
    ''' Request DELETE '''
    x = cred[0]
    delete_request = requests.delete(f'{DOMAIN}/time/{str(tempo_id)}/', auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"]))
    return delete_request


def search_time(date):
    """ Return time data select"""
    x = cred[0]
    search = requests.get(f'{DOMAIN}/time/?search={date}',  auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"])).json() # get request date
    return search

def get_totale():
    ''' Request GET '''
    x = cred[0]
    get_request = requests.get(f'{DOMAIN}/totale/', auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"])).json()
    return get_request

def delete_totale(month_id):
    """ Request delete. """
    x = cred[0]
    delete = requests.delete(f'{DOMAIN}/totale/{str(month_id)}/', auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"]))


def post_time(totale, date):
    """ Request POST """
    x = cred[0]
    post = requests.post(f'{DOMAIN}/time/', json={'ore_lavorative': totale, 'datetime_add': str(date)}, auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"]))
    return post

def sum_total_time():
    """ Return total from month """
    x=cred[0]
    total = requests.get(f'{DOMAIN}/sum-time/',  auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"])).json()
    return total

def post_totale(totale):
    """ Request POST """
    x = cred[0]
    post = requests.post(f'{DOMAIN}/totale/', json={'total_ore': totale}, auth=HTTPBasicAuth(x["USERNAME"], x["PASWORD"]))
    return post

def check_day_add_month():
    """ Request GET """
    get_request = requests.get(f'{DOMAIN}/chack-day/').json()
    return get_request


   
 

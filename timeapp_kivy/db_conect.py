import requests

DOMAIN = 'https://timeappstt.herokuapp.com'

def get_time():
    ''' Request GET '''
    get_request = requests.get(f'{DOMAIN}/time').json()
    return get_request

def put_time(widget_id, ora):
    ''' Request Put '''
    put_request = requests.put(f'{DOMAIN}/time-detail/{str(widget_id)}', data={'ore_lavorative': ora})
    return put_request

def delete_time(tempo_id):
    ''' Request DELETE '''
    delete_request = requests.delete(f'{DOMAIN}/time-detail/{str(tempo_id)}')
    return delete_request


def search_time(date):
    """ Return time data select"""
    search = requests.get(f'{DOMAIN}/time-add/?search={date}').json() # get request date
    return search

def get_totale():
    ''' Request GET '''
    get_request = requests.get(f'{DOMAIN}/totale').json()
    return get_request

def delete_totale(month_id):
    """ Request delete. """
    delete = requests.delete(f'{DOMAIN}/totale-detail/{str(month_id)}')


def post_time(totale, date):
    """ Request POST """
    post = requests.post(f'{DOMAIN}/time', json={'ore_lavorative': totale, 'datetime_add': str(date)})
    return post

def sum_total_time():
    """ Return total from month """
    total = requests.get(f'{DOMAIN}/sum-time').json()
    return total

def post_totale(totale):
    """ Request POST """
    post = requests.post(f'{DOMAIN}/totale', json={'total_ore': totale})
    return post

def check_day_add_month():
    """ Request GET """
    get_request = requests.get(f'{DOMAIN}/chack-day/').json()
    return get_request


   
 

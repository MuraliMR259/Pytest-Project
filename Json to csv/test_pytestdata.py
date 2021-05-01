import pytest
import pandas as pd
import datatest as dt
import json
@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def json_file():
    with open('orders_data.json') as json_file:
        data = json.load(json_file)
        df = pd.json_normalize(data)
        return df

def test_1(json_file):
    #checked the data in json file

    dt.validate(json_file['total_count'], int)             #testing with datatest
    assert "total_count" in json_file                      #pytesting with assert method

def test_2(json_file):

    # checked the data in inside items

    dt.validate(json_file["items"][0][0]["base_grand_total"], float)
    dt.validate(json_file["items"][0][0]["base_total_invoiced"], float)

def test_3(json_file):

    #testing with customer column in check amount_refunded and base_price_incl_tax

    dt.validate(json_file['items'][0][0]['customer'][0]["amount_refunded"], int)
    dt.validate(json_file['items'][0][0]['customer'][0]["base_price_incl_tax"], float)

def test_4(json_file):

    #testing with billing_address column in check city and region_id

    dt.validate(json_file['items'][0][0]['billing_address']["city"], str)
    dt.validate(json_file['items'][0][0]['billing_address']["region_id"], int)

def test_5(json_file):

    # testing with payment column in check amount_authorized and cc_tpye

    dt.validate(json_file['items'][0][0]['payment']["amount_authorized"], float)
    dt.validate(json_file['items'][0][0]['payment']["cc_type"], str)

def test_6(json_file):

    # testing with "status_histories" column in check comment and status

    dt.validate(json_file['items'][0][0]['status_histories'][0]["comment"], str)
    dt.validate(json_file['items'][0][0]['status_histories'][0]["status"], str)



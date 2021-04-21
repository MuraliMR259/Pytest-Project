import pytest
import pandas as pd
import datatest as dt

@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def test_1():
    return pd.read_csv('Customers.csv')

def test_c1(test_1):

    dt.validate(test_1['CustomerID'], int)
    dt.validate(test_1['First Name'],str)
    dt.validate(test_1['Last Name'], str)
    dt.validate(test_1['Customer Email'], str)

#test case 1 is end

@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def test_2():
    return pd.read_csv('Customer Address.csv')

def test_c2(test_2):

    dt.validate(test_2['Street Address'], str)
    dt.validate(test_2['City'],str)

#test case 2 is end

@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def test_3():
    return pd.read_csv('customer order details.csv')

def test_c3(test_3):

    dt.validate(test_3['OrderId'], int)
    dt.validate(test_3['ProductId'],int)

#test case 3 is end

@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def test_4():
    return pd.read_csv('customer order master.csv')

def test_c4(test_4):

    dt.validate(test_4['PaymentId'], int)
    dt.validate(test_4['OrderStatus'],str)

#test case 4 is end


@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def test_5():
    return pd.read_csv('payment details.csv')

def test_c5(test_5):

    dt.validate(test_5['Method of Payment'], str)
    dt.validate(test_5['Card last 4 digits'],int)

#test case 5 is end


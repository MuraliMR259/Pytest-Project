
import pytest
import pandas as pd
import datatest as dt
import json
@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def json_to_csv():
    with open('orders_data.json') as json_file:
        data = json.load(json_file)
        df = pd.json_normalize(data)
        return df


def test_1(json_to_csv):

    dt.validate(json_to_csv['total_count'], int)
    # dt.validate(json_to_csv['page_size'], int)


#  unique_index = pd.Index(list('abc'))


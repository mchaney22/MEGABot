# pytest test suite for pyanswers.py

from pyanswers import PyAnswers
import pytest

@pytest.fixture
def pa():
    return PyAnswers()
    

def test_upload_jsonl(pa):
    result = pa.upload_jsonl('test_upload_jsonl.jsonl')
    id = result['id']
    assert id != None

def test_query_autoroll(pa):
    result = pa.query_autoroll("I want a number one Victory Royale")
    assert result['answers'][0] == 'That would be a legendary task. You can use the Drive Land Vehichle to drive the car, and the acrobatics skill to jump out. You need to beat a DV of 29'



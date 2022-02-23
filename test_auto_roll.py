# pytest test suite for auto_roll.py
from auto_roll import *
import pytest

def test_query__autoroll_examples():
    ar = AutoRoll()
    examples = ar.examples
    # a list of the first element of each example using list comprehension
    queries = [example[0] for example in examples]
    expected = [example[1] for example in examples]
    for i in range(len(queries)):
        answer = ar.query(queries[i])
        # print answer and expected
        print("Query: " + queries[i])
        print("Answer: " + answer)
        print("Expected: " + expected[i])
        assert answer == expected[i]
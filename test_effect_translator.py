# pytest test suite for effectTranslator.py
from effect_translator import *
import pytest

def test_query_DVEffects():
    dve = DVEffect()
    test_questions = [  "beat a DV of 5", 
                        "beat a DV of 9", 
                        "beat a DV of 17", 
                        "That seems extremely easy!! beat a DV of 1", 
                        "That would be an legendary task. You can use the Drive Land Vehichle to drive the car, and the acrobatics skill to jump out. You need to beat a DV of 29"
                        ]

    expected_answers = [  "roll STAT and a d10 to beat a DV of 5",
                            "roll STAT and a d10 to beat a DV of 9",
                            "roll STAT and a d10 to beat a DV of 17",
                            "roll STAT and a d10 to beat a DV of 1",
                            "roll STAT and a d10 to beat a DV of 29"]
    for i in range(len(test_questions)):
        assert dve.query(test_questions[i]) == expected_answers[i]

if __name__ == '__main__':
    test_query_DVEffects()

    




from pyanswers import PyAnswers

class DVEffect(object):
    def __init__(self):
        self.pa = PyAnswers()
        # A list of tuples containing python calls equivilent to outcome effects
        self.examples = [
            ("That would be an everyday task. You can use the Art skill to do it, you need to beat a DV of 17", "dv(17)"),
            ("beat a DV of 9", "dv(9)"),
            ("beat a DV of 5", "dv(5)")
        ]
        self.examples_context = "In order to succeed, you need to roll better then the DV value."
        self.documents = []
    
    def query(self, question):
        # get the answer
        answer = self.pa.query_examples(self.examples_context, self.examples, self.documents, question)
        # execute the DV function
        exec_string = 'DVEffect.' + answer['answers'][0]
        return eval(exec_string)

    def dv(value):
            return "roll STAT and a d10 to beat a DV of " + str(value)

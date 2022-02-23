from pyanswers import PyAnswers
from simple_effect import SimpleEffect

class SimpleMove(SimpleEffect):
    def __init__(self) -> None:
        super().__init__()
        self.examples = [
            ("", "left"),
            ("I want to move to the right", "right"),
            ("I want to move up", "up"),
            ("I want to move down", "down")
        ]
        self.examples_context = "In order to succeed, you need to roll better then the DV value."
        self.documents = []

    def effect_chain(self, ctx, msg):
        intent_answer = self.Intent
        
class SucsessEffect(SimpleEffect):
    def __init__(self):
        super().__init__()
        self.exampels = []

class FailureEffect(SimpleEffect):
    pass

class CauseEffect(SimpleEffect):
    pass



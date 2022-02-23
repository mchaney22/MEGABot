from pyanswers import PyAnswers
from simple_effect import SimpleEffect

class AutoRoll(SimpleEffect):
    def __init__(self):
        super().__init__()
        examples=[["I want to impress the crowd with an Olympic Dive", "That would be a tremendous feat. You can use the Athletics skill to do it, you need to beat a DV of 24"],
                  ["I want to bribe a prison warden who I don't really know", "It would be very difficult to bribe a prison warden, and it'll be tougher because you don't know them. You can use the Bribary skill to do it, you need to beat a DV of 26"],
                  ["I want to make some cool graffiti", "That would take some talant. You can use the Art skill to do it, you need to beat a DV of 15"],
                  ["I want to make a really deadly robot", "That would be a proffesional task. You can use the Robot skill to do it, you need to beat a DV of 17"],
                  ["I want to trap the car", "That would be a proffesional task. You can use the Land Vehichle Tech skill to do it, you need to beat a DV of 17"],
                  ["I want to lie to a bouncer", "You would roll against the bouncer. You can use the Pursiasion skill to do it, the bouncer can use the Streetwise skill against you."],
                  ["I want to flip the car and jump out midair", "That would be legendary. You can use the Drive Land Vehichle to flip the car, and the acrobatics skill to jump out. You need to beat a DV of 29"],
                  ["I want to make a viral meme", "That would be an everyday task. You can use the Art skill to do it, you need to beat a DV of 13"],
                  ["I want to open a jar of mayo", "That would be an everyday task. You can use the Science skill to do it, you need to beat a DV of 9"]]
        examples_context= "The base DV for an Incredible task is 24"
        self.require_file("autoroll.jsonl")

    def query(self, question):
        answer = self.query_from_file(question)
        return answer
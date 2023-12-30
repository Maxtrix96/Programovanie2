class Person():
    def __init__(self, body_parts:list[str], intial_sanity, *activities) -> None:
        self.body_parts = body_parts
        self.sanity = intial_sanity
        self.activities = {item: 0 for item in activities}
    
    def increase_insanity_level(self, increase):
        for item in self.activities:
            self.activities[item] += increase
        self.sanity += sum(list(map(int, list(self.activities.values()))))
        if self.sanity > 69:
            self.body_parts.remove("head")
            print("Insanity levels have reached critical levels!\nHead popped!\nPerson died, lmao\nL+Ratio, Idiot\n")

human_body_parts = "left arm  right arm  head  torso  left leg  right leg  neck".split("  ")
shadow = Person(human_body_parts, 0, "Botany", "rizzing nour")
shadow.increase_insanity_level(70)

dog_body_parts = "head  front right leg  front left leg  hind right leg  hind left leg  tail  torso  neck".split("  ")
maxtrick = Person(dog_body_parts, 5, "learning game development", "owning an amogus plushie", "malding due to loss of 5050")
maxtrick.increase_insanity_level(65)
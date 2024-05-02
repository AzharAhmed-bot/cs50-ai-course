from logic import *

rain=Symbol("rain")
hagrid=Symbol("hagrid")
dumbledore=Symbol("dumbledore")

# KB
knowledge=And(
    Implication(Not(rain),hagrid),
    Or(hagrid,dumbledore),
    Not(And(hagrid,dumbledore)),
    dumbledore
    )

print(model_check(knowledge,rain))

# print(knowledge.formula())

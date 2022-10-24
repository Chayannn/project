from sample_madlibs import hp, code1, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code1, zombie, hungergames])
    m.madlib()

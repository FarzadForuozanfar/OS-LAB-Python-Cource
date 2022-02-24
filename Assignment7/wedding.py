import random
WEDDING_LIST = []
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

while True:
    boy = random.randint(0, len(boys) - 1)
    girl = random.randint(0, len(girls) - 1)
    temp = [boys[boy],"💌",girls[girl]]
    WEDDING_LIST.append(temp)
    boys.remove(boys[boy])
    girls.remove(girls[girl])
    if len(WEDDING_LIST) == 8:
        for couple in WEDDING_LIST:
            print(couple)
        break
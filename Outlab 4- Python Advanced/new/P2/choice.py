import random
import string, sys
import pickle
import os.path


class ValueNotInRange(Exception):
    pass


n_dict = dict()


def fill_choice():
    for i in range(1, 101):
        n_dict[i] = random.randint(1, 5000), ''.join([random.choice(string.ascii_uppercase) for _ in range(4)])
        n_list = n_dict.values()
        outfile = open('new_int.p', 'wb')
        pickle.dump(list(n_list), outfile)
        outfile.close()


if len(sys.argv) < 2:
    fill_choice()
else:
    file = sys.argv[1]
    list = pickle.load(open(file, "rb"))


    def ask_choice():
        while True:
            try:
                n = int(input("Enter Number: "))
                if n < 5000 or n > 7000:
                    raise ValueNotInRange
                    break
                else:
                    found = 0
                    Notfound = 0
                    p = 0
                    for i in range(100):
                        pair = int(n) - list[i][0]
                        for j in range(100):
                            if i != j and list[j][0] == pair:
                                print(list[i][1], list[i][0], list[j][1], list[j][0])
                                p += 1
                                found = True
                                Notfound = True
                                break
                        if p > 0:
                            break
                    if found == False:
                        for i in range(100):
                            pair = n - list[i][0]
                            for j in range(100):
                                if i != j and list[j][0] < pair:
                                    print(list[i][1], list[i][0], list[j][1], list[j][0])
                                    p += 1
                                    Notfound = True
                                    break
                            if p > 0:
                                break
                    if Notfound == False:
                        print("Not Possible")

                    break
            except ValueNotInRange:
                print("Please Enter number between 5000 to 7000")
                continue


    ask_choice()

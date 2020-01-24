import time

div1 = ['A', 'B', 'C', 'D', 'E', 'F']
div2 = ["Whales", "Sharks", "Piranhas", "Alligators"]
div3 = ["Cubs", "Kittens", "Puppies", "Calfs"]

def create_schedule(list):
    """ Create a schedule for the teams in the list and return it"""
    s = []

    if len(list) % 2 == 1: list = list + ["BYE"]

    for i in range(len(list)-1):

        mid = int(len(list) / 2)
        l1 = list[:mid]
        l2 = list[mid:]
        l2.reverse()    

        # Switch sides after each round
        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]

        list.insert(1, list.pop())

    return s


def main():
    number = 1
    week_count = int(len(div1) / 2)
    for first_round in create_schedule(div1):
        for first_match in first_round:
            if week_count > 0:
                week_count = week_count - 1
            else:
                number += 1
                week_count = int(len(div1) / 2) - 1
                # time.sleep(1)
                print()
            
            print("Week ", number, " ==> ", first_match[0], " - ", first_match[1], flush=False)

    print()
    for second_round in create_schedule(div1):        
        for second_match in second_round:
            if week_count > 0:
                week_count = week_count - 1
            else:
                number += 1
                week_count = int(len(div1) / 2) - 1
                # time.sleep(1)
                print()
            
            print("Week ", number, " ==> ", second_match[1], " - ", second_match[0], flush=False)

if __name__ == "__main__":
    main()
import random as rnd
number = rnd.randint(1,10)
def main():
    try:
        inpt = int(input("Number: "))
        if inpt == number:
            print("Done.")
        else:
            if inpt > number:
                print("Give lower int")
                main()
            else:
                print("Give higher int")
                main()
    except:        
        print("Please give int as input.")
        main()
main()


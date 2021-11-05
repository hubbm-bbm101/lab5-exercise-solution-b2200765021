def Odd_Sum_Finder(number):
    return sum([x for x in range(1,number+1) if x % 2 != 0])    
def Even_Average_Finder(number):
    even = [x for x in range(1,number+1) if x % 2 == 0]
    return sum(even) / len(even)
def main():
    try:
        inpt = int(input("Number: "))
        print("Odd number sum: {}\nEven Numbers Average: {}".format(Odd_Sum_Finder(inpt),Even_Average_Finder(inpt)))
    except:
        print("Please give number.")
        main()
main()


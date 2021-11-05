def Validation(string):
    try:
        if string.index("@") and string.index("."):
            return True
    except:
        return False
def main():
    try:
        inpt = input("Mail: ")
        if Validation(inpt):
            print("Valid")
        else:
            print("Invalid")            
    except:
        print("Please give an email")
        main()
main()

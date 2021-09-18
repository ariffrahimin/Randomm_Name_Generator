import random

firstname = ['Ariff', 'Luqman', 'Azizul', 'Haikal', 'Syabil', 'Haziq']
lastname = ['Rahimin', 'Hakim', 'Naim', 'Jalal', 'Zaman', 'Iman']


def main():
    print('Choose your options')
    print('1. Generate a name')
    print('2. Insert new Firstname')
    print('3. Insert new Lastname')
    print('4. Quit')
    k = input()
    if(k == '1'):
        genname()
        main()
    elif(k == '2'):
        newfirstname()
        main()
    elif(k == '3'):
        newlastname()
        main()
    elif(k == '4'):
        print('goodbye :)')


def newfirstname():
    print('Insert a new name')
    x = input()
    if(isinstance(x, str) == True):
        firstname.append(x)
        print(firstname)
    else:
        print('The name is not allowed')
        newfirstname()


def newlastname():
    print('Insert a new name')
    x = input()
    if(isinstance(x, str) == True):
        lastname.append(x)
        print(lastname)
    else:
        print('The name is not allowed')
        newlastname()


def genname():
    j = random.randint(0, len(firstname) - 1)
    i = random.randint(0, len(lastname) - 1)
    print(firstname[j]+" "+lastname[i])


if __name__ == "__main__":
    main()

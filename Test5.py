import os
# Test 5

PATH = "C:/Users/Admin/Desktop/test"
text = '@'


def task1():

    lst = []
    for root, dirs, files in os.walk("C:/Users/Admin/Desktop/test", topdown=True):
        for name in files:
            if name[:9] == 'filenames':
                count = os.path.join(name)
                lst.append(count)

    for i in lst:
        if ')' in i:
            i = i.replace(')', '')
        if '(' in i:
            i = i.replace('(', '')
        # if ' ' in i:
        #     i = i.replace(' ', '')
            print(i)
    print(len(lst))


def task2():
    PATH = "C:/Users/Admin/Desktop/test"
    result = [os.path.join(root, files) for root, file_names, filenames in os.walk(PATH)
              for files in filenames if os.path.splitext(files)[1] == '.txt']
    lst_email = []
    for i in result:
        with open(i) as file:
            data = file.read().split()
            for email in data:
                if '@' in email:
                    lst_email.append(email)
    print(lst_email)


def main():
    task1()
    task2()


if __name__ == '__main__':
    main()
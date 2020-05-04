# Vlad Petreaca


def main():

    list = [1, 2, 2, 3, 4]

    for i in list:
        if i == 2:
            list.remove(i);
            i = 28
            list.append(i)

    print(list)


if __name__ == "__main__":
    main()
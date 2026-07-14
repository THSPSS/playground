
def loop_with_list(list):
    new_list = []
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    print(new_list)
    print("this is functon loop with list")


def remove_duplicate_with_set(list):
    new_set = set(list)
    print(new_set)

if __name__ == "__main__":
    print("main")
    list = [1, 1, 2, 4, 20, 53, 20]
    loop_with_list(list)
    remove_duplicate_with_set(list)


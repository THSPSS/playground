
def loop_with_list(list):
    print("this is functon loop with list")


def remove_duplicate_with_set(list):
    new_set = set(list)
    print(new_set)

if __name__ == "__main__":
    print("main")
    list = [1, 1, 2, 20, 53]
    loop_with_list(list)
    remove_duplicate_with_set(list)


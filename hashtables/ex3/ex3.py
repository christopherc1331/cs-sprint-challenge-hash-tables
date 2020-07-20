def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    arrays_count = len(arrays)
    my_dict = {}
    my_list = []


    for index, list in enumerate(arrays):
        for item in list:
            if item in my_dict:
                # if my_dict[item] == index:
                my_dict[item] += 1
                if my_dict[item] == arrays_count:
                    my_list.append(item)
                    
            else:
                if index == 0:
                    my_dict[item] = 1

    return my_list




if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(0, 10)) + [1, 2, 3])
    # arrays.append(list(range(0, 10)) + [1, 2, 3])
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

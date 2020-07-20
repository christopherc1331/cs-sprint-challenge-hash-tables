def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    arrays_count = len(arrays)
    my_dict = {}
    my_list = []


    for list in arrays:
        for item in list:
            if item in my_dict:
                my_dict[item] += 1
            else:
                my_dict[item] = 1
    
    my_dict_list = my_dict.items()

    for i in my_dict_list:
        if i[1] == arrays_count:
            my_list.append(i[0])

    return my_list




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

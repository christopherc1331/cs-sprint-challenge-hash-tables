def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    matched_weights = ()
    idx_1 = None
    idx_2 = None

    my_dict = {}

    for i in range(length):
        # print("hello")
        # print(weights[i])
        if weights[i] not in my_dict:
            my_dict[weights[i]] = [i]
        else:
            my_dict[weights[i]].append(i)
        

    # print(my_dict)
    for i in range(len(weights) - 1):
        weight_1 = weights[i]
        if limit - weight_1 in my_dict:
            idx_1 = my_dict[weight_1]
            idx_2 = my_dict[limit - weight_1]

            if idx_1 == idx_2:
                idx_1 = my_dict[weight_1][0]
                idx_2 = my_dict[weight_1][1]
            else:
                idx_1 = my_dict[weight_1][0]
                idx_2 = my_dict[limit - weight_1][0]
            

    if idx_1 == None or idx_2 == None:
        return None
    else:
        if idx_1 < idx_2:
            idx_1, idx_2 = idx_2, idx_1
        return (idx_1, idx_2)
        

print(get_indices_of_item_weights([4, 4], 2, 8))
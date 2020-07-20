def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    my_dict = {}
    my_list = []

    for i in range(0,len(a)):
        my_dict[a[i]] = i
        

    for i in range(0,len(a)):
        if a[i] > 0:
            # print("neg value here |",a[i] * -1)
            # print("my_dict which will be checked against |",my_dict)
            if (a[i] * -1) in my_dict:
                # print("appending now")
                my_list.append(a[i])


    return my_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

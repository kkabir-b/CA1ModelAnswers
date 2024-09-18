def bubbleSort(array):
    n = len(array) - 1
    for i in range(len(array)):  # Outer loop iterates n times
        for q in range(n):  # Inner loop iterats n - 1 times
            curr = array[q]  # Current phone
            next = array[q + 1]  # Next phone
            # Extract phone type from the current and next elements
            phone1 = curr.split('(')[1][:-1].upper()
            phone2 = next.split('(')[1][:-1].upper()
            # Compare phone types and swap if necessary
            if phone1 > phone2:
                temp = next
                array[q + 1] = curr
                array[q] = temp
        n -= 1
    return array  # Return the sorted array


def conv_to_dict(array):
    dict_data = dict()  # Defines dictionary
    for phone in array:  # Iterate through each phone
        case = phone.split(' - ')[0][:-1]  # Extract the case
        color_and_type = phone.split(' - ')[1]  # Extracts color + type
        color = color_and_type.split('(')[0]  # Extract color
        type = color_and_type.split('(')[1][:-1]  # Extract type
        dict_data[case] = [color, type]  # Store the case as key and [color, type] as value
    return dict_data  # Return the dict

def sort_keys(array):
    n = len(array) - 1  # Get the last index of the array
    for i in range(len(array)):  # Outer loop iterating through the array
        for j in range(n):  # Inner loop
            curr = array[j]  # Current key
            next = array[j + 1]  # Next key
            if curr < next:  # If current key is less than next key, swap
                temp = next
                array[j + 1] = curr
                array[j] = temp
        n = n - 1 #decrements loop by 1
    return array  # Return sorted keys in descending order


def binary_search(array, case):
    data_in_dict = conv_to_dict(array)  # Convert the array to a dictionary
    keys_of_data = list(data_in_dict.keys())  # Get keys
    min_ind = 0  # sets min index
    max_ind = len(keys_of_data)  # Sets max index
    keys_of_data = sort_keys(keys_of_data)  # Sort the keys using sort_keys function
    found = False  # Flag to indicate if case is found

    # Perform binary search
    while not found:
        curr_check = (min_ind + max_ind) // 2  # Get the middle index
        if curr_check < 0 or curr_check > len(keys_of_data) - 1:  # Check if valid index
            print('Case not found')  # If not valid, print error
            found = True
            break
        curr_data = keys_of_data[curr_check]  # Get the current case at middle index
        if curr_data == case:  # If case matches, print details
            print(f'Case is found. It is {curr_data} '
                  f'case with {data_in_dict[curr_data][0]} color '
                  f'and {data_in_dict[curr_data][1]} type')
            found = True
            break
        elif curr_data > case:  # If the current case is larger, search in the lower half
            min_ind = curr_check + 1
        else:  # If the current case is smaller, search in the upper half
            max_ind = curr_check - 1

queue = []
back_pointer = -1
def enque(queue,back_pointer):
    name = input('Please enter your name -- > ') # asks name
    queue.append(name) #adds name to queue
    back_pointer += 1
    return queue,back_pointer # returns updated queue and pointer
queue,back_pointer = enque(queue,back_pointer)
print(queue,back_pointer)

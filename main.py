phone_case_options = [
    "Leather Wallet Case - Burgundy (iPhone 13)",
    "Silicone Soft Case - Lime Green (Samsung Galaxy S21)",
    "Rugged Armor Case - Gunmetal Gray (Google Pixel 6)",
    "Clear Shockproof Case - Transparent (iPhone 12 Pro Max)",
    "Slim Fit Case - Navy Blue (OnePlus 9 Pro)",
    "Marble Pattern Case - White & Gold Swirl (Samsung Galaxy Note 20)",
    "Flip Cover Case - Lavender (iPhone SE 2020)",
    "Glitter Bling Case - Rose Gold (Google Pixel 5)",
    "Fabric Case - Charcoal (Samsung Galaxy A52)",
    "Hybrid Armor Case - Midnight Blue (iPhone 11)",
    "Magnetic Leather Case - Olive Green (Samsung Galaxy S20)",
    "Waterproof Case - Light Blue (iPhone 8)",
    "Heavy Duty Case - Red (Google Pixel 4a)",
    "Wooden Grain Case - Maple (iPhone 14)",
    "Neon Matte Case - Hot Pink (Samsung Galaxy Z Fold 3)",
    "Frosted Matte Case - Sky Blue (OnePlus 8T)",
    "Soft Touch Silicone Case - Canary Yellow (iPhone XR)",
    "Carbon Fiber Case - Jet Black (Samsung Galaxy S10)",
    "Vintage Leather Case - Tan Brown (Google Pixel 7)",
    "Crystal Clear Case - Transparent (iPhone 12 Mini)",
    "Armor Kickstand Case - Dark Green (Samsung Galaxy A72)",
    "Ultra Slim Case - Light Gray (iPhone X)",
    "Quilted Leather Case - Deep Red (Samsung Galaxy S22)",
    "Gradient Case - Purple to Pink Fade (Google Pixel 6a)",
    "Bumper Case - Teal (OnePlus Nord 2)",
    "3D Printed Case - Floral Pattern (iPhone 11 Pro)",
    "Canvas Fabric Case - Moss Green (Samsung Galaxy S9)",
    "Soft TPU Case - Coral Pink (Google Pixel 5a)",
    "Rhinestone Case - Diamond Silver (iPhone 7 Plus)",
    "Holographic Case - Iridescent (Samsung Galaxy Z Flip 4)",
    "Rubberized Case - Cobalt Blue (iPhone 13 Pro)",
    "Cork Eco-Friendly Case - Natural (Google Pixel 4 XL)",
    "Leather Flip Wallet Case - Coffee Brown (OnePlus 7T)",
    "Matte Soft Case - Plum Purple (iPhone 14 Pro)",
    "Metallic Case - Steel Gray (Samsung Galaxy S8)",
    "Shockproof Armor Case - Orange (Google Pixel 3a)",
    "Transparent Gel Case - Crystal Clear (iPhone 12)",
    "Patterned Silicone Case - Camo Green (Samsung Galaxy A50)",
    "Shimmer Sparkle Case - Silver Glitter (Google Pixel 2 XL)"
]




def bubbleSort(array):
    n = len(array) - 1
    for i in range(len(array)):
        for q in range(n):
            curr = array[q]
            next = array[q + 1]
            phone1 = curr.split('(')[1][:-1].upper()
            phone2 = next.split('(')[1][:-1].upper()
            if phone1 > phone2:
                temp = next
                array[q + 1] = curr
                array[q] = temp
    return array
sorted_lst = bubbleSort(phone_case_options)

def conv_to_dict(array):
    dict_data = dict() #dict because {} cld also represent set
    for phone in array:
        case = phone.split(' - ')[0]
        color_and_type = phone.split(' - ')[1]
        color = color_and_type.split('(')[0]
        type = color_and_type.split('(')[1][:-1]
        dict_data[case] = [color,type]
    return dict_data

def sort_keys(array):
    n = len(array) - 1
    for i in range(len(array)):
        for j in range(n):
            curr = array[j]
            next = array[j + 1]
            if curr > next:
                temp = next
                array[j + 1] = curr
                array[j] = next
    return array
def binary_search(array,case):
    data_in_dict = conv_to_dict(array)
    keys_of_data = list(data_in_dict.keys())
    min_ind = 0
    max_ind = len(keys_of_data)
    keys_of_data = sort_keys(keys_of_data)
    found = False
    while not found:
        curr_check = (min_ind + max_ind)//2
        if curr_check < 0 or curr_check > len(keys_of_data) - 1:
            print('Case not found')
            found = True
            break
        curr_data = keys_of_data[curr_check]
        if curr_data == case:
            print(f'Case is found. It is {curr_data} '
                  f' with {data_in_dict[curr_data][0]} color '
                  f'and {data_in_dict[curr_data][1]} type')
            found = True
            break
        elif curr_data < case:
            min_ind = curr_check + 1
        else:
            max_ind = curr_check - 1

binary_search(phone_case_options,'Patterned Silicone Case')

queue = []
back_pointer = -1
def enque(queue,back_pointer):
    name = input('Please enter your name -- > ')
    queue.append(name)
    back_pointer += 1
    return queue,back_pointer
queue,back_pointer = enque(queue,back_pointer)
print(queue,back_pointer)

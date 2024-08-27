new_list = [2, 3, 4, 'Dhaka']

for element in new_list:
    try:
        print(element/2)
    except:
        print('Not a number')

list = [10, 14, 19, 21, 22, 24, 25, 26, 31, 33, 38, 47, 49, 53, 64, 65, 68, 69, 96, 101, 107, 108, 109, 110, 119, 130, 139, 147, 148, 149, 150, 161, 166, 177, 179, 183, 185, 188, 192, 200, 206, 218, 238, 251, 274, 275, 282, 290]
list2 = [12, 13, 14, 15, 18, 21, 26, 35, 43, 44, 45, 48, 58, 60, 62, 63, 67, 69, 84, 86, 89, 95, 99, 100, 101, 103, 105, 126, 161, 164, 178, 179, 183, 222, 225, 253, 258, 276, 279, 284]
list3 = [15, 19, 54, 58, 88, 99, 101, 108, 115, 119, 123, 135, 166, 170, 184, 217, 219, 224, 231, 240, 253, 254, 255, 264, 276, 281, 286]


def count_duplicates():
    for item in list:
        if item in list2:
            print(item)
        if item in list3:
            print(item)
    for item in list2:
        if item in list3:
            print(item)


count_duplicates()

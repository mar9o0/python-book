favnum = {
    'Mila' : [1,2],
    'Kolia' : [3,6,5],
    'Kate' : [7,9,8],
    'Sofa' : [11,22,33],
    'Petia' : [12,45],
}

for name, nums in favnum.items():
    print("\n" + name.title() + "'s a favourite numbers are:")
    for num in nums:
        print("\t" + str(num))
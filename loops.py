nums = [1,3,4,5,6,7,8,9,56,3,45,56,3,23,45,56]

for index, num in enumerate(nums, start=1):
    # print(index,num)
    if num == 3:
        print('Found it')
        # break
        continue
    print(index,num)

for num in nums:
    for letter in 'abc':
        print(num,letter)


# range
        for i in range(1,10): # 1 = start 10 = end
            print(i)

# while loop
x = 0
while True:
    if x == 3:
        break
    print(x)
    x += 1

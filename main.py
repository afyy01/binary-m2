#method 2 - iterative

numbers = [1,2,3,4,5,6,7,8]

finding_element = 6

start = 0
end = len(numbers) - 1

flag = False

while start <=end:
    mid = (start + end) //2

    if numbers[mid] == finding_element:
        print("We got it! ")
        flag = True
        break
    elif numbers[mid] > finding_element: #first half of list
        end = mid - 1
    else:
        start = mid+1

if flag == False:
    print("We dont have this number")
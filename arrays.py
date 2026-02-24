elements = [1,2,3,4,5]

largest = elements[0]
for element in elements:
    if element > largest:
        largest = element

print(largest)


smallest = elements[0]

for element in elements:
    if element < smallest:
        smallest = element
print(smallest)

sumArray = 0
for element in elements:
    sumArray += element
print(sumArray)

largest = secondLargest = float("-inf")
for element in elements:
    if largest < element:
        secondLargest = largest
        largest = element
    elif secondLargest < element and not element == largest:
        secondLargest = element

print(secondLargest)


x = 3
count=0
for element in elements:
    if element < x:
        count+=1

print(count)


# subarray sum

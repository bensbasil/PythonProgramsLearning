my_list =[]
num_elements=int(input("Enter the number of elements: "))
for i in range(num_elements):
    elements=input(f"Element {i+1}: ")
    my_list.append(elements)
print("The list is:", my_list)
elementr=input("Enter the element to be removed: ")
if elementr in my_list:
    my_list.remove(elementr)
    print("The list after removing the element is:", my_list)
else:
    print("Element not found in the list.")   
slice1=my_list[1:5]
print("The sliced list from index 1 to 3 is:", slice1)
my_list[0]='100'
print("The modified list is:", my_list)
my_tuple = (2,5,7,9,11)
print("The tuple is:", my_tuple)
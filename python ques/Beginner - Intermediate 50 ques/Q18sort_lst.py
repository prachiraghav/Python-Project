# 18. Sort a list without using the built-in sort() function.

# This code implements a custom selection sort algorithm that sorts a list of numbers in ascending order.
# It repeatedly finds the smallest element from the unsorted portion of the list and appends it to a new sorted list.
def custom_sort(lst):
    sorted_list = []
    
    while lst:
        # Find the smallest number in the remaining list
        smallest = lst[0]
        for item in lst:
            if item < smallest:
                smallest = item

        # Add it to the new sorted list
        sorted_list.append(smallest)
        # Remove it from the original list
        lst.remove(smallest)

    return sorted_list

a = list(map(int, input("Enter list items: ").split()))
sorted_a = custom_sort(a.copy())  # use .copy() to preserve original list
print("Sorted list:", sorted_a)

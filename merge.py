# Input two lists from user
list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

# Merge the lists
merged_list = list1 + list2

# Sort the merged list
merged_list.sort()

# Output result
print("Merged and sorted list:", merged_list)
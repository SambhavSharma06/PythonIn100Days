#List Methods in Python!!

l = [1, 2, 3, 4, 6] 
print(l)
# l.append(7) #Add element at the end
# l.sort(reverse=True) #Sort the list in descending order
# l.reverse() #Reverse the list
# print(l.index(1)) #Find the index of an element
# print(l.count(1))     \\Count occurrences of an element
# l.remove(3) #Remove an element
# m = l.copy()//Copy
# m[0] = 0
# l.insert(1,899)

m = [900,1000,1100]
k = l + m #Concatenate two lists
l.extend(m)#Open m and add elements to l
print(l)
print(k)

l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# Access individual items in lists and tuples using the index.

print(l[0])
print(t[0])
# print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.

l[0] = "Smith"
# t[0] = "Smith"  # This gives an error because tuples are "immutable".

print(l)
print(t)

# Extend lists by using `.extend`

l.extend("Jen")
print(l)
# Tuples cannot be 'extended' because they are immutable.

# Add to sets by using `.add`

s.add("Jen")
print(s)

# Sets can't have the same element twice.

s.add("Bob")
print(s)

locations = ['cancun', 'mazatlan', 'puerto vallarta', 'yucantan', 'puerto escondido']
print("\nOriginal order List")
print(locations)

print("\nSorted List")
print(sorted(locations))

print("\nNo changes were made to the original list")
print(locations)

print("\nReverse list temporarily")
print(sorted(locations, reverse=True))

print("\nNo changes were made to the original")
print(locations)

print("\nReverse list temporarily")
locations.reverse()
print(locations)

print("\nOriginal order list")
locations.reverse()
print(locations)

print("\nListed sorted in aphabetical order")
locations.sort()
print(locations)

print("\nReverse list")
locations.sort(reverse=True)
print(locations)

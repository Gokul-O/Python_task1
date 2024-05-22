from itertools import combinations
def findTriplets(lst, key):
    def valid(val):
        return sum(val) == key
    return list(filter(valid, list(combinations(lst, 3))))
lst = [10,20,30,9]
print(findTriplets(lst, 59))
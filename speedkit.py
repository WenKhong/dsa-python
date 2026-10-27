from collections import Counter
from collections import defaultdict
from collections import deque
import heapq


def count_words(words):
    count = Counter()
    for word in words:
        count[word] += 1
    return count

def colour_with_numbers ():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for colour, number in s:
        d[colour].append(number)
    return sorted(d.items())

def deque_instead_of_list (): #uses deque instead of list for faster appends and pops from both ends
    q = deque()
    q.append("order1") #append add to last
    q.append("order2")
    q.appendleft("urgent") #append add to first
    
    return list(q)

def heapq_example():
    h = []
    heapq.heappush(h, 3)
    heapq.heappush(h, 1)
    heapq.heappush(h, 2)

    print(h) #will print [1,3,2] not fully sorted but the smallest element is at the first index
    heapq.heappop(h) #remove smallest element
    print(h) #will print [2,3] 
    heapq.heappop(h) #remove smallest element after the first pop
    return h #will print [3]

    #if wanted to remove the largest element instead of the smallest, can just add negative values in front

def sort_examples_tuple_reverse():
    scores = [("mei", 3), ("ali", 5), ("abu", 3)]
    return sorted(scores, key=lambda s: (-s[1], s[0])) # - will sort in descending order, which means ali,5 will come first

def sort_examples_strings():
    print(sorted(["kiwi", "fig", "banana"], key=len))   # ['fig', 'kiwi', 'banana']
    print(sorted("dcba"))                               # ['a', 'b', 'c', 'd']
    print("".join(sorted("dcba")))   
    
    return (sorted(["kiwi", "fig", "banana"], key=len))      # 'abcd'    

def enumerate_example():
    for i, item in enumerate(["shoes", "bag", "cap"]):
        print(i, item)
    # 0 shoes
    # 1 bag
    # 2 cap

    for i, item in enumerate(["shoes", "bag"], start=1):
        print(i, item)
    # 1 shoes
    # 2 bag

    return (list(enumerate("hi")))   # [(0, 'h'), (1, 'i')]   

assert count_words(["apple", "banana", "apple"]) == Counter({'apple': 2, 'banana': 1}), "count_words failed"
assert colour_with_numbers() == [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])], "colour_with_numbers failed"
assert deque_instead_of_list() == ['urgent', 'order1', 'order2'], "deque_instead_of_list failed"
assert heapq_example() == [3], "heapq_example failed"
assert sort_examples_tuple_reverse() == [('ali', 5), ('abu', 3), ('mei', 3)], "sort_examples_tuple_reverse failed"
assert sort_examples_strings() == ['fig', 'kiwi', 'banana'], "sort_examples_strings failed"
assert enumerate_example() == [(0, 'h'), (1, 'i')], "enumerate_example failed"

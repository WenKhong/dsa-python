def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1 #.get(number, defaault value)


    buckets = [[] for _ in range(len(nums) + 1)] #_ = no variable needed
    for num, freq in count.items(): #.itmes() return key and value pair
        buckets[freq].append(num)


    res = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            res.append(num)
            if len(res) == k:
                return res
    return res


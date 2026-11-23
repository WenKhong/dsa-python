def minEatingSpeed(self, piles, h):
    """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
    left = 1
    right = max(piles)
    answer = right

    while left <= right:
        k = (left + right) // 2

        hours = 0
        for p in piles:
            hours += (p + k - 1) // k 

        if hours <= h:
            answer = k
            right = k - 1
        else:
            left = k + 1

    return answer

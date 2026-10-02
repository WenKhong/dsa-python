def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = sorted(list(s))
        t_list = sorted(list(t))

        if s_list == t_list:
            return True
        return False

print(isAnagram("list", "silent"))
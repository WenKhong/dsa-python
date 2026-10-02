def isAnagram( s, t):
        s_list = sorted(list(s))
        t_list = sorted(list(t))

        if s_list == t_list:
            return True
        return False

print(isAnagram("listen", "silent"))


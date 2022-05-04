example = "3523014"

def find_10substring(string: str):

    # Iteration
    iter = 0

    # Count of how many 10-substrings are in string
    count = 0

    # Index of the first element to start on in string
    idx = 0

    def find(i_from, mem, i_to = False):
        idx = i_from
        while idx < len(string):
            """ Sum of the memory string """
            current = 0
            for i in mem:
                current += int(i)

            """ End loop """
            if current >= 10:
                checker = True
                if i_to:
                    checker = i_to <= idx
                if current == 10 and checker:
                    return True
                break
            mem += string[idx]
            idx += 1
        return False
    last_mem = ""
    while True:
        # Memory of sum
        mem = ""
        if len(last_mem) == len(string)-1:
                idx += 1
                iter = 0
        if idx == len(string) - 1:
            break
        if iter == 0:
            count += find(idx, mem)
        else:
            count += find(idx, mem, len(last_mem)+1)
        last_mem = mem
        iter += 1
    return count

result = find_10substring(example)

print(result)
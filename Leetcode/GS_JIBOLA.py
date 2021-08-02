
# optimal solution
def segment(x, space):
    length = len(space)

    deq = deque()
    result = []
    idx = 0
    while idx < length:
        if deq and deq[0] == idx - x:
            deq.popleft()
        while deq and space[deq[-1]] > space[idx]:
            deq.pop()
        deq.append(idx)

        if idx + 1 >= x:
            result.append(space[deq[0]])
        idx += 1

    return max(result)

# my solution
def segment(x, space):
    # Write your code here
    start = 0
    maxi = float('-inf')
    dq = deque()

    for end in range(len(space)):
        dq.append(space[end])

        if end >= x - 1:
            mini = min(dq)
            maxi = max(maxi, mini)

            # update start
            dq.popleft()
    return maxi

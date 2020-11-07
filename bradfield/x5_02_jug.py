


def minimum_pours(A, B, target):
    # values denote volume in A, B, action counter and queue
    queue = [(0, 0, 0, [])]

    while queue:
        a, b, pours, actions = queue.pop(0)
        if a == target or b == target:
            print actions
            return True, pours
        if pours > 10:
            return False, -1
        pours += 1
        # fill actions
        if b < B:
            queue.append((a, B, pours, list(actions) + ["fill b>B"]))
        if a < A:
            queue.append((A, b, pours, list(actions) + ["fill a>A"]))        
        # empty and pour actions
        if a > 0:
            queue.append((0, b, pours, list(actions) + ["empty a"]))
            queue.append((max(a-(B-b), 0), min(B, a+b), pours, list(actions) + ["pour a>b"]))
        if b > 0:
            queue.append((a, 0, pours, list(actions) + ["empty b"]))
            queue.append((min(a+b, A), max(0, b-(A-a)), pours, list(actions) + ["pour b>a"]))
        

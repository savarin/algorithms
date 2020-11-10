

def climb_stairs(stairs):
    #
    """You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can
    you climb to the top?

    Example:
        Input: 2
        Output: 2

    3
        1 1 1
        1 2
        2 1

    """
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2

    return climb_stairs(stairs - 1) + climb_stairs(stairs - 2)


def main():
    print(climb_stairs(3))
    print(climb_stairs(4))


if __name__ == "__main__":
    main()

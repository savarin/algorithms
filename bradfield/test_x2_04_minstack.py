from x2_04_minstack import MinStack



def test_MinStack():
    minstack = MinStack()
    minstack.push(-2)
    minstack.push(0)
    minstack.push(-3)
    assert minstack.get_min() == -3
    minstack.pop()
    assert minstack.top() == 0
    assert minstack.get_min() == -2

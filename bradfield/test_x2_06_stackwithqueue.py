from x2_06_stackwithqueue import StackWithQueue



def test_StackWithQueue():
    stack = StackWithQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    item = stack.pop()
    assert item == 3
    assert stack.top() == 2

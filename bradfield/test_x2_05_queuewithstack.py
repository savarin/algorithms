from x2_05_queuewithstack import QueueWithStack



def test_QueueWithStack():
    queue = QueueWithStack()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    item = queue.pop()
    assert item == 1
    assert queue.peek() == 2

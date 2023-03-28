from src.node import Node


def test_node_init():
    """Проверяем, что объект Node ининциализируется правильно"""
    data = {'id': 40}
    node = Node(data)
    assert node.data == data
    assert node.left is None
    assert node.right is None

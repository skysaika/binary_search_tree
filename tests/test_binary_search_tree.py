from src.binary_search_tree import BinarySearchTree

def test_bst_empty():
    """Пустое дерево поиска содержит пустую вершину"""
    bst = BinarySearchTree()
    assert bst.root is None

def test_bst_root():
    """Добавляем данные в вершину BST."""
    bst = BinarySearchTree()
    data = {'id': 40}
    bst.insert(data)
    assert bst.root.data == data

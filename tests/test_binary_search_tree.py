import pytest

from src.binary_search_tree import BinarySearchTree


@pytest.fixture
def bst_root():
    """Создаем BST с одним узлом в вершине."""
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    return bst


def test_bst_empty():
    """Пустое дерево поиска содержит пустую вершину"""
    bst = BinarySearchTree()
    assert bst.root is None


def test_bst_root(bst_root):
    """Добавляем данные в вершину BST."""
    assert bst_root.root.data == {'id': 40}


def test_bst_insert_left(bst_root):
    """Добавляем данные влево от вершины"""
    bst_root.insert({'id': 30})
    assert bst_root.root.left.data['id'] == 30


def test_bst_insert_right(bst_root):
    """Добавляем данные вправо от вершины"""
    bst_root.insert({'id': 50})
    assert bst_root.root.right.data['id'] == 50

def test_bst_insert_left_left(bst_root):
    """Добавляем данные влево от вершины 2 раза"""
    bst_root.insert({'id': 30})
    bst_root.insert({'id': 25})
    assert bst_root.root.left.left.data['id'] == 25

def test_bst_insert_right(bst_root):
    """Добавляем данные вправо от вершины"""
    bst_root.insert({'id': 50})
    bst_root.insert({'id': 60})
    assert bst_root.root.right.right.data['id'] == 60

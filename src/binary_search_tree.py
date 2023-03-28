from src.node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        """Инициализируем всегда пустое бинарное дерево поиска."""
        self.__root = None

    @property
    def root(self) -> Node | None:
        """Возвращает ссылку на вершину BST."""
        return self.__root

    def insert(self, data: dict) -> None:
        """Добавляем данные в структуру согласно правилам BST."""
        if self.__root is None:
            self.__root = Node(data)
        else:
            self._insert_recursively(self.__root, data)

    def _insert_recursively(self, node: Node, data: dict) -> None:
        """Рекурсивно ищет место для вставки новых данных"""
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left, data)

        if data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)

    def search(self, post_id: int) -> dict:
        """Ищем и возвращаем словарь с данными о посте по его id."""
        if self.__root is None:
            return None
        else:
            return self._search_recursively(self.__root, post_id)

    def _search_recursively(self, node: Node, post_id: int) -> dict | None:
        """Рекурсивно ищем данные по id"""
        if post_id == node.data['id']:
            return node.data

        if post_id < node.data['id']:
            if node.left is None:
                return None
            else:
                return self._search_recursively(node.left, post_id)

        if post_id > node.data['id']:
            if node.right is None:
                return None
            else:
                return self._search_recursively(node.right, post_id)
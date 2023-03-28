from src.node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        """Инициализируем всегда пустое бинарное дерево поиска."""
        self.__root = None

    @property
    def root(self):
        """Возвращает ссылку на вершину BST."""
        return self.__root

    def insert(self, data: dict) -> None:
        """Добавляем данные в структуру согласно правилам BST."""
        if self.__root is None:
            self.__root = Node(data)

    def search(self, post_id: int) -> dict:
        """Ищем и возвращаем словарь с данными о посте по его id."""

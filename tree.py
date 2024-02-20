from dataclasses import dataclass, field
from typing import Optional, TypeVar, Generic, List


T = TypeVar('T')
InputText = str
OutputText = str


@dataclass
class BaseNode(Generic[T]):
    text: str
    children: List[T] = field(default_factory=list)
    parent: Optional['BaseNode'] = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.text!r}, {len(self.children)} children)'

    def set_parent(self, parent: 'BaseNode') -> None:
        self.parent = parent

    def get_parent(self) -> Optional['BaseNode']:
        return self.parent

    def add_child(self, child: T) -> None:
        self.children.append(child)
        child.set_parent(self)

    def add_children(self, children: List[T]) -> None:
        for child in children:
            self.add_child(child)

    def get_child(self, index: int) -> T:
        return self.children[index]

    def get_children(self) -> List[T]:
        return self.children

    def get_child_count(self) -> int:
        return len(self.children)

    def get_text(self) -> str:
        return self.text

    def get_coordinates(self) -> str:
        if self.parent is None:
            return '0'
        else:
            index = self.parent.children.index(self)
            parent_coords = self.parent.get_coordinates()
            return f'{parent_coords}.{index}'
    
    def print_tree(self, depth: int = 0) -> None:
        indent = '  ' * depth
        print(f'{indent}{self.get_coordinates()} - {self.text}')
        for child in self.get_children():
            child.print_tree(depth + 1)


class OutputNode(BaseNode['InputNode']):
    text: OutputText


class InputNode(BaseNode['OutputNode']):
    text: InputText


class Tree:
    def __init__(self, root: InputNode) -> None:
        self.root = root

    def get_node_by_coordinates(self, path: str) -> BaseNode:
        indices = [int(index) for index in path.split('.') if index.isdigit()]
        current_node = self.root
        for index in indices[1:]:
            try:
                current_node = current_node.children[index]
            except IndexError:
                raise IndexError(f'Index {index} out of bounds for node {current_node}')
        return current_node

    def print_tree(self) -> None:
        self.root.print_tree()


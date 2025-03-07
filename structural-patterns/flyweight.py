from dataclasses import dataclass


@dataclass
class TreeType:
    name: str
    color: str
    texture: str

    def draw(self, x, y) -> None: ...


class TreeFactory:
    tree_types: list[TreeType] = []

    @staticmethod
    def get_tree_type(name: str, color: str, texture: str) -> TreeType:
        tree_type = TreeType(name, color, texture)

        for created_tree_type in TreeFactory.tree_types:
            if tree_type == created_tree_type:
                return created_tree_type

        TreeFactory.tree_types.append(tree_type)

        return tree_type


@dataclass
class Tree:
    x: int
    y: int
    type: TreeType

    def draw(self) -> None:
        self.type.draw(self.x, self.y)


@dataclass
class Forest:
    trees: list[Tree]

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()

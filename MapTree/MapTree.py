from DataStructures.Map.MapBase import MapBase
from DataStructures.Tree import LinkedBinaryTree


class MapTree(MapBase, LinkedBinaryTree):
    def __setitem__(self, key, value):
        
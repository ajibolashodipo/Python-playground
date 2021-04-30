def max_depth(node, currentDepth=1):
    if node is None:
        return currentDepth

    currentDepth += 1

    return max(max_depth(node.left, currentDepth), max_depth(node.right, currentDepth))

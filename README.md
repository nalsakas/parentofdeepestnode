# parentofdeepestnode
Find first lefmost parent of deepest nodes of a binary tree

# Problem Statement:
For a given tree, find first parent of the deepest node. Priority of deepest nodes are from left to right
```
Input:
            3
        |       |    
       5        1
    |    |    |    |        
    6    2    0    8
        |  |         |
        7  4         9

Output: 2
Although 9 is also reside in deepest level, priority is given to leftmost nodes.
```
# Solution:
- bfs algorithm is chosed to explore tree structure.
- Nodes are put in arrays based on their levels. array[[level1 nodes], [level 2 nodes], etc.]
- Priority to put into array belongs to leftmost nodes.
- Deepest nodes reside in array[-1]
- Parent of deepest nodes reside in res[-2] 
- First (leftmost) parent of the deepest nodes is the answer.
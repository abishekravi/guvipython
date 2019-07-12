#a
class Node:
  def __init__(self,A):
    self.value=A
    self.right=None
    self.left=None

def insert(root,A):
  if root is None:
    root=Node(data)
  elif root.value > A:
    if root.left is None:
      root.left=Node(A)
    else:
      insert(root.left,A)
  elif root.value < A:
    if root.right is None:
      root.right=Node(A)
    else:
      insert(root.right,A)

def LCA(root,L_val,R_val):
  if root is None:
    return None
  elif L_val > root.value and R_val > root.value:
    return(LCA(root.right,L_val,R_val))
  elif L_val < root.value and R_val < root.value:
    return (LCA(root.left,L_val,R_val))
  else:
    return root.value

nn=int(input())
val=list(map(eval,input().split()))
u,v=map(eval,input().split())
R=Node(val[0])
for i in range(1,nn):
  insert(R,val[i])
print(LCA(R,u,v))

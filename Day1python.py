class Node:
    def __init__(self,val=0,next=None):
        self.val=val 
        self.next=None 

def LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    
    return head

class Solution:
    def deleteMiddleNode(self, head: Node)->Node:
        if not head or not head.next:
            return None 
        
        slow=head 
        fast=head 
        prev=None 

        while fast and fast.next:
            prev=slow 
            slow=slow.next 
            fast=fast.next.next 

        prev.next=slow.next 

        return head  

def printLL(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print("None")

arr=[1,2,3,4,5]
head=LL(arr)
print(head)
    
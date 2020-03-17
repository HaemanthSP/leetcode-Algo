# Define linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode,) -> ListNode:
        res = []
        carry = 0
        while True:
            # Sum the respective digits with carry
            value = l1.val + l2.val + carry

            # Get the carry to carry forward
            carry, digit = divmod(value, 10)
            res.append(digit)

            # Is next iteration valid?
            if not (l1.next or l2.next):
                break
                
            # Prepare for next iteration
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            
        # Add the final carry to the result sequence
        if carry:
            res.append(carry)
        
        # Convert the integer sequence into a linked list
        total = None
        for x in res[::-1]:
            temp = ListNode(x)

            # Chain the previous with the current instance
            temp.next = total if total else None
            total = temp 
        return total
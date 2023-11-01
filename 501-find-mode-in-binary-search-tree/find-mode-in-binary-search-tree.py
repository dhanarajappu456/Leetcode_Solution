'''
inorder 
________________

if we ke have sortede order of the elements, then we can find the top occuring elements easily , since they are adjacent 
that is if prev element same as current element , then we increase the count , and when the count becomes same as max so far  we add this element to the ans list , 
if the count exceed the max sofar ,we got new max and all elements added to list is cleared and add current element


for getting  sorted order of elements , we use inorder 
'''
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        count = 0
        max_ = 0
        prev = 10**5 + 1

        def rec(root):
            if root is None:
                return
            nonlocal count, max_, prev, ans 
            rec(root.left)
            #finding count of current element 
            if prev == root.val:
                count += 1
            #if current element is ocurring for first time  count stated from 1
            else:
                count = 1

            #if count becomes == max ,then current element added to ans list
            if count == max_:
                ans.append(root.val)
            #if is more than  max_ , then this is the only top icccuring element , so clear all 
            #prev elemetn 
            elif count > max_:
                ans = [root.val]
                max_ = count
            #updating prev = current elemetn
            prev = root.val
            rec(root.right)

        rec(root)
        return ans
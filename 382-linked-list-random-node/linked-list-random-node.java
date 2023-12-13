/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
**/

class Solution {
    private List<Integer> list;
    private Random random;

    public Solution(ListNode head) {
        ListNode temp = head;
        list = new ArrayList<>();
        random = new Random();

        while (temp != null) {
            list.add(temp.val);
            temp = temp.next;
        }

   
    }

    public int getRandom() {
        int index = random.nextInt(list.size());
        return list.get(index);
    }
}


/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
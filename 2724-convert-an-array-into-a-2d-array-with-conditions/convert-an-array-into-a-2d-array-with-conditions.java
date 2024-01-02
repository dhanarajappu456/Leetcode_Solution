import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


class Solution {
   
        





    public List<List<Integer>> findMatrix(int[] nums) {
        Map<Integer, Integer> mp = new HashMap<>();
        for (int num : nums) {
            mp.put(num, mp.getOrDefault(num, 0) + 1);
        }
        
        List<List<Integer>> ans = new ArrayList<>();
        while (!mp.isEmpty()) {
            List<Integer> li = new ArrayList<>();
            
            // iterating on copy to avoid getting ConcurrentModificationException
            Map<Integer, Integer> mpCopy = new HashMap<>(mp);
            for (int num : mpCopy.keySet()) {
                li.add(num);
                mp.put(num, mp.get(num) - 1);
                if (mp.get(num) == 0) {
                    mp.remove(num);
                }
            }
            
            ans.add(li);
        }
        
        return ans;
    }
}

 
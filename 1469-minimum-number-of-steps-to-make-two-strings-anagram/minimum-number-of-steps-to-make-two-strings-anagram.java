class Solution {
    public int minSteps(String s, String t) {
        Map<Character, Integer> tmap = new HashMap<>();
        Map<Character, Integer> smap = new HashMap<>();
        
        for (char c : t.toCharArray()) {
            tmap.put(c, tmap.getOrDefault(c, 0) + 1);
        }
        
        int ans = 0;
        
        for (char c : s.toCharArray()) {
            smap.put(c, smap.getOrDefault(c, 0) + 1);
            if (smap.get(c) > tmap.getOrDefault(c, 0)) {
                ans++;
            }
        }
        
        return ans;

        
    }
}
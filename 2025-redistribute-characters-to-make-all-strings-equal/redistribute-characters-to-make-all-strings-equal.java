class Solution {
    public boolean makeEqual(String[] words) {
       


        HashMap<Character,Integer> mp = new HashMap<>();
        int n  = words.length;
        for(String word: words){
            for(Character c : word.toCharArray())
               mp.put(c, mp.getOrDefault(c,0)+1 );
        }
        for(Integer count: mp.values())
            if(count%n!=0)
                return false;
        return true ;
    }
}
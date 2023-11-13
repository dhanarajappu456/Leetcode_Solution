class Solution {
    public String sortVowels(String s) {
        HashSet<Character> vowSet = new HashSet<>(Arrays.asList(new Character[]{'a','e','i','o','u','A','E','I','O','U'}));
        List<Character> vowList = new ArrayList<>();
        for(Character c : s.toCharArray()){
            if(vowSet.contains(c))
                vowList.add(c);
        }

        vowList.sort(null);
        // System.out.println(vowList);
        StringBuilder res = new StringBuilder();
        int  p= 0; 
        for(Character c: s.toCharArray()){
            if (!vowSet.contains(c))
                res.append(c);
            else{
                Character vow = vowList.get(p);
                p+=1;
                res.append(vow);

            }
           
        }


        return res.toString();


    }
}
class Solution {
    public boolean backspaceCompare(String s, String t) {
        

        
        return (build(s).equals(build(t)));

    }


    private Stack<Character> build(String str ){

        

        Stack<Character> stk = new Stack();

        for(char c : str.toCharArray()){


            if (c!= '#'){
                stk.push(c);
            }
            else if(!stk.empty()){

                stk.pop();
            }


        }
        return stk;

    }
}
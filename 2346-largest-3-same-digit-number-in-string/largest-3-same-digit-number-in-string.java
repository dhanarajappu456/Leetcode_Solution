class Solution {
    public String largestGoodInteger(String num) {
        int ans = -1;
        String res = "";
        int n = num.length();
        int i = 0;

        while (i < n) {
            if (1 <= i && i <= n - 2 && num.charAt(i - 1) == num.charAt(i) && num.charAt(i) == num.charAt(i + 1)) {
                int currentNum = Integer.parseInt(num.substring(i - 1, i + 2));
                if (ans < currentNum) {
                    ans = currentNum;
                    res = num.substring(i - 1, i + 2);
                }
            }
            i++;
        }

        return res;
    }
}
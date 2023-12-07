class Solution {
    public String largestOddNumber(String num) {
        int oddRightmostInd = -1;
        int n = num.length();
        for (int i = n - 1; i >= 0; i--) {
            if (Integer.valueOf(num.charAt(i)) % 2 != 0) {
                oddRightmostInd = i;
                break;
            }
        }
        return num.substring(0, oddRightmostInd + 1);
    }
}


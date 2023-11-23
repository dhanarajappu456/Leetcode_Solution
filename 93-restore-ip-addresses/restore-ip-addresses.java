class Solution {
    public List<String> restoreIpAddresses(String s) {
            List<String> res  = new ArrayList<>();
            rec(0, new ArrayList<>(), 0 , s, res);
            return res;
    }
    
    private void rec(int i, List<String> ans, int partition, String s, List<String> res) {
        if (partition == 4) {
            if (i == s.length()) {
                res.add(String.join(".", ans));
            }
            return;
        }

        for (int j = i; j < Math.min(i + 3, s.length()); j++) {
            String sub = s.substring(i, j + 1);
            int val = Integer.parseInt(sub);

            if (val <= 255 && !(j != i && s.charAt(i) == '0')) {
                ans.add(sub);
                rec(j + 1, ans, partition + 1, s, res);
                ans.remove(ans.size() - 1);
            } else {
                break;
            }
        }
    }
}





class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int n = people.length;
        int i = 0, j = n - 1;
        int cnt = 0;
        while (i <= j) {
            if (people[i] + people[j] > limit) {
                j--;
            } else {
                i++;
                j--;
            }
            cnt++;
        }
        return cnt;
    }
}
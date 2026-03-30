class Solution {
    public int longestConsecutive(int[] nums) {
        Map<Integer, Integer> mp = new HashMap<Integer, Integer>();
        int answer = 0;
        
        for(int num : nums) {
            if (!mp.containsKey(num)) {
                int left = mp.getOrDefault(num - 1, 0);
                int right = mp.getOrDefault(num + 1, 0);
                int consecutiveLength = 1 + left + right;
                
                mp.put(num, consecutiveLength);
                mp.put(num - left, consecutiveLength);
                mp.put(num + right, consecutiveLength);
                
                if (consecutiveLength > answer) {
                    answer = consecutiveLength;
                }
            }
        }
        return answer;
    }
}
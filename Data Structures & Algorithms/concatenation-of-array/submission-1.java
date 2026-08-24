class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[nums.length * 2];
    int x = 0;
    int y = 0;
    while (x != ans.length){
        ans[x] = nums[y];
        x++;
        y++;
        if (y == nums.length){
            y -= nums.length;
        }
    }
    return ans;
}
}
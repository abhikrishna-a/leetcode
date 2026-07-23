class Solution {
  int minimumOperations(List<int> nums) {
    return nums.where((num) => num % 3 != 0).length;
  }
}
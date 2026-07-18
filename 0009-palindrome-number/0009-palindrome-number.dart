class Solution {
  bool isPalindrome(int x) {
    String s = x.toString();
    return s == s.split('').reversed.join('');
  }
}
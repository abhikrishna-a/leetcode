class Solution {
  double average(List<int> salary) {
    salary.sort();

    int sum = 0;
    for (int i = 1; i < salary.length - 1; i++) {
      sum += salary[i];
    }

    return sum / (salary.length - 2);
  }
}
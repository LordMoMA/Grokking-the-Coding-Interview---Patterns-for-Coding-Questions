'use strict';

// 643. Maximum Average Subarray I

// Input: nums = [1,12,-5,-6,50,3], k = 4
// Output: 12.75000
// Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

// Input: nums = [5], k = 1
// Output: 5.00000

// Time Complexity #
// The time complexity of the above algorithm will be O(N).

// Space Complexity #
// The algorithm runs in constant space O(1).

const findMaxAverage = function (nums, k) {
  let arr = [];
  let start = 0;
  let sum = 0;
  for (let end = 0; end < nums.length; end++) {
    sum += nums[end];
    if (end >= k - 1) {
      arr.push(sum / k);
      sum -= nums[start];
      start++;
    }
  }
  return Math.max(...arr);
};

console.log(findMaxAverage([1, 12, -5, -6, 50, 3], 4));

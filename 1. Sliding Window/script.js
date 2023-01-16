"use strict";

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

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

// 1918. Smallest Subarray with a given sum

// Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

// Input: [2, 1, 5, 2, 3, 2], S=7
// Output: 2
// Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

const smallest = function (s, arr) {
  let list = [];
  let sum = 0;
  let start = 0;
  for (let end = 0; end < arr.length; end++) {
    sum += arr[end];
    while (sum >= s) {
      list.push(end - start + 1);
      sum -= arr[start];
      start++;
    }
  }
  return Math.min(...list);
};

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

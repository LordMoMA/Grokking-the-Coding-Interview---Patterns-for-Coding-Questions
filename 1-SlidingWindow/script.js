"use strict";

// 643. Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

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
///////////////////////////////////////////////////////////////

// 159 Longest Substring with K Distinct Characters
// similar to // 904. Fruit Into Baskets, in 904, k = 2

// Given a string, find the length of the longest substring in it with no more than K distinct characters.

// Input: String="araaci", K=2
// Output: 4
// Explanation: The longest substring with no more than '2' distinct characters is "araa".

// Input: String="araaci", K=1
// Output: 2
// Explanation: The longest substring with no more than '1' distinct characters is "aa".

// Input: String="cbbebi", K=3
// Output: 5
// Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

const subString = function (str, k) {
  let map = {},
    start = 0,
    max = 0;

  for (let end = 0; end < str.length; end++) {
    const rightChar = str[end];
    if (!map[rightChar]) map[rightChar] = 0;
    map[rightChar]++;

    while (Object.keys(map).length > k) {
      const leftChar = str[start];
      map[leftChar]--;
      if (map[leftChar] === 0) delete map[leftChar];
      start++;
    }
    max = Math.max(max, end - start + 1);
  }
  return max;
};

console.log(subString("araaci", 2));
console.log(subString("araaci", 1));
console.log(subString("cbbebi", 3));

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.

const lengthOfLongestSubstring = function (s) {
  let map = {};
  let start = 0;
  let max = 0;

  for (let end = 0; end < s.length; end++) {
    if (s[end] in map) start = Math.max(start, map[s[end]] + 1);
    map[s[end]] = end;
    max = Math.max(max, end - start + 1);
  }
  return max;
};

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

// 904. Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

// Input: fruits = [1,2,1]
// Output: 3
// Explanation: We can pick from all 3 trees.

// Input: fruits = [0,1,2,2]
// Output: 3
// Explanation: We can pick from trees [1,2,2].
// If we had started at the first tree, we would only pick from trees [0,1].

// beware of the while loop and everything inside, esp length and [start]

const totalFruit = function (fruits) {
  let map = {},
    start = 0,
    max = 0;

  for (let end = 0; end < fruits.length; end++) {
    if (!map[fruits[end]]) map[fruits[end]] = 0;
    map[fruits[end]]++;

    while (Object.keys(map).length > 2) {
      map[fruits[start]]--;
      if (map[fruits[start]] === 0) delete map[fruits[start]];
      start++;
    }

    max = Math.max(max, end - start + 1);
  }
  return max;
};

console.log(totalFruit(["A", "B", "C", "B", "B", "C"]));

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////

// Given an integer array nums, a reducer function fn, and an initial value init, return the final result obtained by
// executing the fn function on each element of the array, sequentially, passing in the return value from the calculation
// on the preceding element.
//
// This result is achieved through the following operations: val = fn(init, nums[0]), val = fn(val, nums[1]),
// val = fn(val, nums[2]), ... until every element in the array has been processed. The ultimate value of val is then
// returned.
//
// If the length of the array is 0, the function should return init.
//
// Please solve it without using the built-in Array.reduce method.

type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
  let result = init;

  for (const num of nums) {
    result = fn(result, num);
  }

  return result;
}
// Given an array arr and a function fn, return a sorted array sortedArr. You can assume fn only returns numbers and
// those numbers determine the sort order of sortedArr. sortedArr must be sorted in ascending order by fn output.
//
// You may assume that fn will never duplicate numbers for a given array.

type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };

type Fn = (value: JSONValue) => number;

function sortBy(arr: JSONValue[], fn: Fn): JSONValue[] {
  return arr.sort((a, b) => fn(a) - fn(b));
}
// Given an array arr and a chunk size size, return a chunked array.
//
// A chunked array contains the original elements in arr, but consists of subarrays each of length size. The length of the
// last subarray may be less than size if arr.length is not evenly divisible by size.
//
// Please solve it without using lodash's _.chunk function.

type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };

type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
  const result: Obj[][] = [];

  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }

  return result;
}
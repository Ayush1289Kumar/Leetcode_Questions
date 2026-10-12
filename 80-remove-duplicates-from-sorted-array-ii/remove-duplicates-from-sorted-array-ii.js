/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let start = 1;
    let curr = 2;

    while (curr < nums.length){

        if (nums[curr] != nums[start-1]){
            start++;
            nums[start] = nums[curr];
        }
        curr++;
    }
    return start+1;
};
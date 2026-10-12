/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let first =0;
    let second = 1;
    let n = nums.length;
    let k = 1;
    while (second<n){
        if (nums[second]!= nums[first]){
            nums[first+1] = nums[second];
            first++;
            k++;
        }
        second++;
    }
    return k;
};
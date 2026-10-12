/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */

var removeElement = function(nums, val) {
    let left = 0;
    let right = nums.length -1;

    while(left<= right){
        if (nums[left]===val){
            let temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            right--;
        }else{
            left++;
        }
    }

    return right+1;
};
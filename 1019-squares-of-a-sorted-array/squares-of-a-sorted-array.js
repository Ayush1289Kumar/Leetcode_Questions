/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let left = 0;
    let right = nums.length -1;
    let index = nums.length -1;

    let ans = new Array(nums.length);

    while (left <= right){
        let leftSq = nums[left]*nums[left];
        let rightSq = nums[right]*nums[right];

        if (leftSq>rightSq){
            ans[index] = leftSq;
            left++;
        }
        else{
            ans[index] = rightSq;
            right--;
        }
        index--;
    }

    return ans;
};
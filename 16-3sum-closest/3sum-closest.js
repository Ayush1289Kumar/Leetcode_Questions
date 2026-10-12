/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
    let max_diff = Infinity;
    let res_sum = 0;
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length - 2; i++) {
        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            let sum = nums[i] + nums[left] + nums[right];
            let diff = Math.abs(sum - target);

            if (diff < max_diff) {
                max_diff = diff;
                res_sum = sum;
            }
            if (sum === target) {
                return target;
            }
            else if (sum < target) {
                left++;
            }
            else {
                right--;
            }
        }
    }
    return res_sum;
};
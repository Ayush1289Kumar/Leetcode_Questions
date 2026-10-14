/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let curr_sum = 0;

    for (let i=0;i<k;i++){
        curr_sum+=nums[i];
    }
    max_sum = curr_sum;
    low = 0;
    high = k;

    while (high < nums.length){
        curr_sum = curr_sum - nums[low] + nums[high];

        max_sum = Math.max(max_sum, curr_sum);
        low++;
        high++;
    }
    return max_sum/k;

};
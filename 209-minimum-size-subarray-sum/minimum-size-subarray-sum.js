/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let min_val = Infinity
    let low = high = window_sum = 0;

    for(let high=0;high<nums.length;high++){
        window_sum += nums[high];

        while (window_sum>=target){
            win_len = high - low +1;
            min_val = Math.min(min_val,win_len);
            window_sum -= nums[low];
            low++;
        }
        
    }

    if (min_val === Infinity){
        return 0;
    }else{
        return min_val;
    }
};
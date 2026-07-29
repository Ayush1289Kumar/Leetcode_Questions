class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = max(salary)
        min_salary = min(salary)
        sum_salary = 0
        n = len(salary)

        for value in salary:
            if value == max_salary or value == min_salary:
                continue
            sum_salary+=value
        
        avg_salary = sum_salary/(n-2)

        return avg_salary

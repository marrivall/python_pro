import random
from concurrent.futures import ThreadPoolExecutor

def random_numbers(n):
    nums = []
    for _ in range(n):
        nums.append(random.randint(1, 50))
    return nums

def elements_sum(nums):
    result = 0
    for num in nums:
        result += num
    print(f"Elements sum = {result}")
    return result, nums

def arithmetic_mean(data):
    result, nums = data
    mean_result  = result /len(nums)
    print(f"Arithmetic mean = {mean_result}")
    return mean_result

def main():
    n = 10_000

    with ThreadPoolExecutor(max_workers=3) as executor:
        t1 = executor.submit(random_numbers, n)
        t1_result = t1.result()
        t2 = executor.submit(elements_sum, t1_result)
        t2_result = t2.result()
        t3 = executor.submit(arithmetic_mean, t2_result)
        t3_result = t3.result()
    print(f"Numbers list: {t1_result}, Arithmetic mean = {t3_result}")

if __name__ == "__main__":
    main()
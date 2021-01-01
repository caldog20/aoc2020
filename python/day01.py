# Part 1
nums = []

with open("/workspace/aoc2020/input/day01_input") as f:
    for i in f:
        nums.append(int(i)) # Append each line of number in the file to the list

nums_len = len(nums)
for n in nums:
    for m in nums:
        res = m + n
        if res == 2020:
            print(n,m)
            print(n * m)
            break

# Part 2

answer = False
for i in range(nums_len):
    for j in range(nums_len):
        for k in range(nums_len):
            if nums[i] + nums[j] + nums[k] == 2020:
                answer = True
                print(nums[i],nums[j],nums[k])
                p = nums[i] * nums[j] * nums[k]
                print(f"Part 2 product is {p}")


    if answer: break
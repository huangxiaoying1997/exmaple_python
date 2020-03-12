from stage1 import get_result, gen_mapping

if __name__ == '__main__':
    nums = input("请输入一个[0-99]的数字：")
    if int(nums) < 0 or int(nums) > 99:
        print('超出范围')
        exit(1)

    nums = [int(nums[i]) for i in nums  if int(nums[i]) > 1 and int(nums[i]) < 10]
    mapping = gen_mapping()
    res = get_result(nums, mapping)
    print(' '.join(res))








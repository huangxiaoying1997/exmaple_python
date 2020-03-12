"""
[2,3,4] --> 2 [3,4] --> 2 3 [4] --> 2 [34] --> [234]
"""
import string


def gen_mapping():
    mapping = {}
    idx = 0
    # string.ascii_lowercase=26个小写字母
    alphabet = string.ascii_lowercase
    for i in range(2, 10):
        if i == 7 or i == 9:
            mapping.setdefault(i, alphabet[idx : idx + 4])
            idx += 4
        else:
            mapping.setdefault(i, alphabet[idx: idx + 3])
            idx += 3

    return  mapping

def get_result(nums, mapping):
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [c for c in mapping.get(nums[0], [])]

    # 递归求解
    t = get_result(nums[1:], mapping)
    a = mapping.get(nums[0], [])

    res = []
    for x in a:
        res.extend([ x + tt for tt in t])
    return res


if __name__ == '__main__':
    nums = input('请输入数字列表（如：[2,3]),且每个数字必须从[0-9]取值：')
    nums = nums.replace("[", "").replace("]", "").replace(",", " ")
    nums = [int(i) for i in nums.split()]

    for i in range(len(nums)):
        if nums[i] < 0 or nums[i] > 9:
            print('存在异常数字')
            exit(1)

    nums = [nums[i] for i in range(len(nums)) if nums[i] > 1 and nums[i] < 10]
    mapping = gen_mapping()
    res = get_result(nums, mapping)
    # 将列表中的字符串打印出来，空格隔开
    print(' '.join(res))

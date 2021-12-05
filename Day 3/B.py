def create_bin_num(nums, total):
    fnums = []
    for x in nums:
        if x >= total/2:
            fnums.append("1")
        else:
            fnums.append("0")
    return fnums

def calculate_number(nums, bin, i):
    ret = []
    for x in nums:
        if x[i] == bin[i]:
            ret.append(x)
    return ret

def calculate_totals(nums):
    totals = [0 for x in range(12)]
    for x in nums:
        for i, y in enumerate(x):
            if y == "1":
                totals[i] += 1
    return totals


if __name__ == "__main__":
    nums = []
    for x in open("./diagnostic.txt").readlines():
        nums.append(x.strip("\n"))
    
    fnums = nums
    ogr = ''
    for i in range(12):
        fnums = calculate_number(fnums, create_bin_num(calculate_totals(fnums), len(fnums)), i)
        if len(fnums) == 1:
            ogr = ''.join(fnums)
            break

    csr = ''
    fnums = nums
    for i in range(12):
        bin = ["0" if x == "1" else "1" for x in create_bin_num(calculate_totals(fnums), len(fnums))]
        fnums = calculate_number(fnums, bin, i)
        if len(fnums) == 1:
            csr = ''.join(fnums)
            break


    print(int(csr,2) * int(ogr,2))

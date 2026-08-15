class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # 🗂️ Our memory bank: {number: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Did we already see the number we need?
            if complement in seen:
                # Yes! Return its stored index and our current index
                return [seen[complement], i]
            
            # No? Save the current number and its index for later
            seen[num] = i


solution = Solution()

nums = []
target = 0

def main():
    print("\n" + "=" * 50)
    print("=" * 12 + " Two Sum leetcode problem " + "=" * 12)
    print("=" * 50)

    try:
        qtdNums = int(input("\nType the ammount of numbers that you've want: "))
    except ValueError:
        print("\nType a number please, no letters or float numbers allowed.")

    for _ in range(qtdNums):
        try:
            number = int(input("\nNumber: "))
            nums.append(number)
        except ValueError:
            print("\nType a number please, no letters or float numbers allowed.")

    try:
        target = int(input("\nType the target value: "))
    except ValueError:
        print("\nType a number please, no letters or float numbers allowed.")

    result = solution.twoSum(nums, target)

    fim = print(f"\nThe solution is: {result}")

    print("\n\n" + "=" * 50)
    print("=" * 16 + " End of system " + "=" * 16)
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
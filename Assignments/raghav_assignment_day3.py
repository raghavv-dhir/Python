def remove_duplicates(nums):
    seen = set()
    unique = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            unique.append(num)
    return unique


def digit_sum(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def get_even_numbers(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


def get_odd_numbers(nums):
    return list(filter(lambda x: x % 2 != 0, nums))


def replace_with_digit_sum(nums):
    return list(map(digit_sum, nums))


def process_numbers(nums):
    unique_nums = remove_duplicates(nums) #[12,7,34]

    evens = get_even_numbers(unique_nums)
    odds = get_odd_numbers(unique_nums)
    #print(evens) = [12,34]
    #print(odds) = [7]

    evens_digit_sum = replace_with_digit_sum(evens) #[3,7]
    odds_digit_sum = replace_with_digit_sum(odds)  #[7]

    return evens_digit_sum, odds_digit_sum #


nums = [12, 7, 12, 34, 7]
print("After removing duplicates: ",remove_duplicates(nums))
print("Even nums: ",get_even_numbers(nums))
print("Odd nums: ",get_odd_numbers(nums))
print("Unique-Even and Unique-Odd digit sum: ",process_numbers(nums))

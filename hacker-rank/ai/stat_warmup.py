import math
from collections import Counter

if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().split()[:n]))

    # Mean
    mean = sum(nums) / n
    print(f"{mean:.1f}")

    # Median
    nums_sorted = sorted(nums)
    mid = n // 2
    if n % 2 == 0:
        median = (nums_sorted[mid - 1] + nums_sorted[mid]) / 2
    else:
        median = nums_sorted[mid]
    print(f"{median:.1f}")

    # Mode
    counts = Counter(nums)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    mode = min(modes)  # numerically smallest if multiple
    print(mode)

    # Standard Deviation
    variance = sum((x - mean) ** 2 for x in nums) / n
    std_dev = math.sqrt(variance)
    print(f"{std_dev:.1f}")

    # 95% Confidence Interval
    margin = 1.96 * (std_dev / math.sqrt(n))
    lower = mean - margin
    upper = mean + margin
    print(f"{lower:.1f} {upper:.1f}")

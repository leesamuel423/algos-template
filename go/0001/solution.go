package solution

func twoSum(nums []int, target int) []int {
	cache := make(map[int]int)
	for i, num := range nums {
		remainder := target - num
		if val, ok := cache[remainder]; ok {
			return []int{val, i}
		}
		cache[num] = i
	}
	return nil
}

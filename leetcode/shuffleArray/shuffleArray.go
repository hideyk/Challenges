package shufflearray

func removeIndex(nums []int, i int) []int {
	return append(nums[:i], nums[i+1:]...)
}

func insertIndex(nums []int, i int, v int) []int {
	nums = append(nums, 0)
	copy(nums[i+1:], nums[i:])
	nums[i] = v
	return nums
}

func shuffle(nums []int, n int) []int {
	for i := 0; i < n; i++ {
		v := nums[n+i]
		nums = removeIndex(nums, n+i)
		nums = insertIndex(nums, 2*i + 1, v)
	}
	return nums
}
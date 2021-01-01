package sumzero

func sumZero(n int) []int {
	res := make([]int, n)
	for i := 0; i < n; i++ {
		val := 1 - n + 2 * i
		res[i] = val
	}
	return res
}
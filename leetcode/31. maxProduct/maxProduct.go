package maxproduct

func maxProduct(nums []int) int {
	a, b := 0, 0
	for _, v := range nums {
		if v > a {
			a, b = v, a
		} else if v > b {
			b = v
		}
	}
	return (a - 1) * (b - 1)
}
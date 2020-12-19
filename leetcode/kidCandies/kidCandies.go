package kidcandies

func maxOfList(arr []int) int {
	m := 0
    for i, v := range arr {
        if i == 0 || v > m {
			m = v
		}
	}
	return m
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
    result := make([]bool, len(candies))
	max := maxOfList(candies)
	for i, v := range(candies) {
		result[i] = v + extraCandies >= max
	}
	return result
}
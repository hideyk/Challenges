package main

import (
	"fmt"
	"strconv"
)

func findNumbers(nums []int) int {
	res := 0
	for i := range nums {
		// if len(fmt.Sprintf("%d", nums[i])) % 2 == 0
		if len(strconv.Itoa(nums[i]))%2 == 0 {
			res++
		}
	}
	return res
}

func main() {
	abc := []int{12, 345, 2, 6, 7896}
	res := findNumbers(abc)
	fmt.Println(res)
}

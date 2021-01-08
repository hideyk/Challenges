package main

import "fmt"

func selfDividingNumbers(left int, right int) []int {
	res := make([]int, 0)
	for i := left; i < right + 1; i++ {
		j := i
		if i < 10 {
			res = append(res, i)
			continue
		}
		
		selfdivisor := true
		for i != 0 {
			cur := i % 10
			i /= 10
			if cur == 0 {
				selfdivisor = false
				break
			}
			if j % cur != 0 {
				selfdivisor = false
				break
			}
		}
		if selfdivisor {
			res = append(res, i)
		}
	}
	return res
}

func main() {
	res := selfDividingNumbers(1, 2)
	fmt.Println(res)
}
package countgoodtriplets

import (
	"math"
)

func countGoodTriplets(arr []int, a int, b int, c int) int {
	n := len(arr)
	res := 0
	for i := 0; i < n-2; i++ {
		for j := 0; j < n-1; j++ {
			for k := 0; k < n; k++ {
				va, vb, vc := arr[i], arr[j], arr[k]
				if int(math.Abs(float64(va-vb))) <= a && int(math.Abs(float64(vb-vc))) <= b && int(math.Abs(float64(va-vc))) <= c {
					res++
				}
			}
		}
	}
	return res
}

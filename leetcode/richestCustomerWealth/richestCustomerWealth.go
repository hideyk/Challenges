package richestcustomerwealth


func maximumWealth(accounts [][]int) int {
	wealth := 0
	for i := 0; i < len(accounts); i++ {
		v := 0
		for j := 0; j < len(accounts[i]); j++ {
			v += accounts[i][j]
		}
		if v > wealth {
			wealth = v
		}
	}
	return wealth
}
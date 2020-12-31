package main

import "fmt"

func destCity(paths [][]string) string {
	placesvisited := map[string]int{}
	res := ""
	for i := 0; i < len(paths); i++ {
		a, b := paths[i][0], paths[i][1]
		placesvisited[a]--
		placesvisited[b]++
	}
	for k, v := range placesvisited {
		if v == 1 {
			res = k
		}
	}
	return res
}

func main() {
	paths := make([][]string, 3)
	for i := range paths {
		paths[i] = make([]string, 2)
	}
	paths[0] = []string{"London","New York"}
	paths[1] = []string{"New York","Lima"}
	paths[2] = []string{"Lima","Sao Paulo"}

	destination := destCity(paths)
	fmt.Println(destination)
}
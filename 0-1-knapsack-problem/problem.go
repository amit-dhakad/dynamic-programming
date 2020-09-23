package main

import (
	"fmt"
)

/* You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it(0-1 property). */

func main() {
	val := []int{60, 100, 120}
	wt := []int{10, 20, 30}
	W := 50
	n := len(val)
	fmt.Println(knapSack(val, wt, W, n))
}

func knapSack(val []int, weight []int, c int, n int) int64 {
	if c == 0 || n == 0 {
		return 0
	}

	if weight[n-1] > c {
		return knapSack(val, weight, c, n-1)
	} else {
		temp1 := int64(val[n-1]) + knapSack(val, weight, c-weight[n-1], n-1)
		temp2 := knapSack(val, weight, c, n-1)
		return Max(temp1, temp2)
	}

}

// Max it return max value
func Max(x int64, y int64) int64 {
	if x < y {
		return y
	}
	return x
}

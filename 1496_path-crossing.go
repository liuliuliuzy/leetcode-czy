package solutions

import (
	"fmt"
	"goleetcode/mylibs"

	"github.com/emirpasic/gods/lists/arraylist"
)

// This is the real solution. it's private
func isPathCrossing(path string) bool {
	points := make([][2]int, 0)
	now := [2]int{0, 0}
	points = append(points, now)
	for _, chr := range path {
		switch chr {
		case 'W':
			now[0] -= 1
		case 'E':
			now[0] += 1
		case 'N':
			now[1] += 1
		case 'S':
			now[1] -= 1
		default:
			fmt.Println("wrong chr")
		}
		if _, res := mylibs.IsIn(points, now); res {
			return true
		} else {
			points = append(points, now)
		}
		fmt.Println(points)
	}
	return false
}

type Point struct {
	X int
	Y int
}

func isPathCrossingII(path string) bool {
	points := make(map[Point]bool)
	now := Point{0, 0}
	points[now] = true
	for _, chr := range path {
		switch chr {
		case 'W':
			now.X -= 1
		case 'E':
			now.X += 1
		case 'N':
			now.Y += 1
		case 'S':
			now.Y -= 1
		default:
			fmt.Println("wrong chr")
		}
		if _, res := points[now]; res {
			return true
		} else {
			points[now] = true
		}
		fmt.Println(points)
	}
	return false
}

func isPathCrossingIII(path string) bool {
	points := arraylist.New()
	now := [2]int{0, 0}
	points.Add(now)
	for _, chr := range path {
		switch chr {
		case 'W':
			now[0] -= 1
		case 'E':
			now[0] += 1
		case 'N':
			now[1] += 1
		case 'S':
			now[1] -= 1
		default:
			fmt.Println("wrong chr")
		}
		if res := points.Contains(now); res {
			return true
		} else {
			points.Add(now)
		}
		// fmt.Println(points)
	}
	return false
}

// This is a wrapper function, the first letter is capitaliazied to be public
func IsPathCrossing(path string) bool {
	// fmt.Println(isPathCrossingII(path))
	return isPathCrossingIII(path)
}

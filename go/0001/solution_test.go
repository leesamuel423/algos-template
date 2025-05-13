package solution

import (
	"reflect"
	"testing"
)

func TestSolution(t *testing.T) {
	testCases := []struct {
		name     string
		input1   []int
		input2   int
		expected []int
	}{
		{
			name:     "Test Case 1",
			input1:   []int{2, 7, 11, 15},
			input2:   9,
			expected: []int{0, 1},
		},
		{
			name:     "Test Case 2",
			input1:   []int{3, 2, 4},
			input2:   6,
			expected: []int{1, 2},
		},
		{
			name:     "Test Case 3",
			input1:   []int{3, 3},
			input2:   6,
			expected: []int{0, 1},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			if got := twoSum(tc.input1, tc.input2); !reflect.DeepEqual(tc.expected, got) {
				t.Errorf("Solution() = %v, want %v", got, tc.expected)
			}
		})
	}
}

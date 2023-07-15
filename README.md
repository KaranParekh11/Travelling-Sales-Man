# Traveling Salesman Problem with Dynamic Programming

This repository contains a Python implementation of the Traveling Salesman Problem (TSP) using dynamic programming. The TSP is a classic optimization problem that seeks to find the shortest possible route that visits a set of cities and returns to the starting city, while visiting each city exactly once.

## Problem Description

The TSP can be defined as follows:

- Given a list of cities and the distances between each pair of cities, find the shortest possible route that visits each city exactly once and returns to the starting city.

## Solution Overview

This implementation solves the TSP using dynamic programming. The approach involves breaking down the problem into smaller subproblems and solving them recursively. The main steps of the algorithm are as follows:

1. Calculate the distances between all pairs of cities and store them in a distance matrix.
2. Define a memoization table to store the optimal cost and path for each subproblem.
3. Implement a recursive helper function that computes the minimum cost and optimal path for a given set of cities.
4. Start from the starting city and recursively explore all possible paths, updating the minimum cost and optimal path along the way.
5. Return the minimum cost and optimal path for the complete TSP.

## Usage

1. Install Python (version X.X.X or higher) on your machine.
2. Clone this repository: `git@github.com:KaranParekh11/Travelling-Sales-Man.git`
3. Navigate to the project directory: `cd traveling-salesman-dp`
4. Run the script: `python tsp_dp.py`
5. The optimal tour, final result, and minimum cost will be displayed in the console.

## Customization

You can customize the input by modifying the `railway_stations` dictionary in the `tsp_dp.py` file. Add or remove cities and their corresponding coordinates as needed. The algorithm will calculate the optimal tour based on the provided cities.

## Dependencies

This implementation requires the following dependencies:

- Python (version 3.9.12 or higher)
- math module

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- The algorithmic approach used in this implementation is inspired by Serjeel Ranjan's contribution.

## References

- [Wikipedia - Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
- [GeeksforGeeks - Traveling Salesman Problem](https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/)
- [Dynamic Programming Approach to Traveling Salesman Problem](https://www.techiedelight.com/travelling-salesman-problem-using-branch-and-bound/)
- [Traveling Salesman Problem on Brilliant](https://brilliant.org/wiki/traveling-salesman-problem/)
- [Dynamic Programming - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)

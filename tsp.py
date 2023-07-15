import sys
import math

railway_stations = {
    "Ahmedabad": (23.0216, 72.5797),
    "Bharuch": (21.6989, 72.9971),
    "Surat": (21.1920, 72.8042),
    "Anand": (22.5641, 72.9606),
    "Vadodara": (22.3072, 73.1812),
    "Nadiad": (22.6928, 72.8615),
}

places = list(railway_stations.values())
print(places, len(places))


def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate the differences between coordinates
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = R * c
    return distance


def tsp_dp(graph, start):
    n = len(graph)
    all_sets = (1 << n) - 1
    memo = [[-1] * n for _ in range(all_sets)]
    print(graph)
    def tsp_helper(mask, current_city):
        if mask == all_sets:
            return 0, []

        if memo[mask][current_city] != -1:
            return memo[mask][current_city]

        min_cost = float('inf')
        min_path = []

        for next_city in range(n):
            if (mask >> next_city) & 1 == 0:
                cost, path = tsp_helper(mask | (1 << next_city), next_city)
                cost += graph[current_city][next_city]

                if cost < min_cost:
                    min_cost = cost
                    min_path = [current_city] + path

        # memo[mask][current_city] = min_cost, min_path
        return min_cost, min_path

    return tsp_helper(1 << start, start)

dist = [[0] * len(places) for _ in range(len(places))]
for i in range(len(places)):
    for j in range(len(places)):
        dist[i][j] = haversine_distance(places[i], places[j])

# for x in dist:
#     print(x)
min_cost, tour = tsp_dp(dist, 2)  # Start from index 0

# Generate the final tour places using the coordinates
tour_places = [places[i] for i in tour]  # Exclude the last place

# Generate the final result by mapping the tour places to their respective station names
final_result = [list(railway_stations.keys())[list(railway_stations.values()).index(place)] for place in tour_places]

print("Optimal Tour:", tour_places)
print("Final Result:", final_result)
print("Minimum Cost:", min_cost)

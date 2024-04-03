#Question 1

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_destination= our_routes.intersection(competitor_routes)
print(f"The destinations that both routes go to are: {same_destination}")

our_routes_unique= our_routes.difference(competitor_routes)
print(f"These are the locations where only our routes go to: {our_routes_unique}")

unique_destinations= our_routes.symmetric_difference(competitor_routes)
print(f"These are the routes that are not shared by the airlines: {unique_destinations}")
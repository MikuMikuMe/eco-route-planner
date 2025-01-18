Below is a complete Python program for an Eco-Route-Planner application. This simplified example assumes that the user provides a start and end location, and the program calculates a route that minimizes fuel consumption based on a predefined set of routes and their fuel efficiencies. For a more advanced application, you would integrate it with real-time data and possibly a mapping service API.

```python
import sys

# Mock Data: predefined routes with fuel efficiency (miles per gallon)
ROUTES = {
    ('LocationA', 'LocationB'): {'distance': 100, 'fuel_efficiency': 25},
    ('LocationA', 'LocationC'): {'distance': 150, 'fuel_efficiency': 30},
    ('LocationB', 'LocationC'): {'distance': 200, 'fuel_efficiency': 20},
    ('LocationA', 'LocationD'): {'distance': 300, 'fuel_efficiency': 28},
    ('LocationB', 'LocationD'): {'distance': 120, 'fuel_efficiency': 22},
    ('LocationC', 'LocationD'): {'distance': 80, 'fuel_efficiency': 35},
}

def calculate_fuel_usage(distance, fuel_efficiency):
    """Calculate fuel usage given distance and fuel efficiency."""
    try:
        return distance / fuel_efficiency
    except ZeroDivisionError:
        print("Error: Fuel efficiency cannot be zero.")
        return float('inf')

def find_most_efficient_route(start_location, end_location):
    """Find the most fuel-efficient route given a start and end location."""
    if start_location == end_location:
        print("Start and end locations are the same; no route needed.")
        return None

    feasible_routes = {route: data for route, data in ROUTES.items() 
                       if (start_location in route and end_location in route)}

    if not feasible_routes:
        print(f"No direct routes available between {start_location} and {end_location}.")
        return None

    most_efficient_route = None
    smallest_fuel_usage = float('inf')

    for route, data in feasible_routes.items():
        fuel_usage = calculate_fuel_usage(data['distance'], data['fuel_efficiency'])
        if fuel_usage < smallest_fuel_usage:
            smallest_fuel_usage = fuel_usage
            most_efficient_route = route

    return most_efficient_route, smallest_fuel_usage

def main():
    print("Welcome to the Eco-Route-Planner")

    try:
        start_location = input("Enter start location: ").strip()
        end_location = input("Enter end location: ").strip()

        most_efficient_route = find_most_efficient_route(start_location, end_location)

        if most_efficient_route:
            route, fuel_usage = most_efficient_route
            route_distance = ROUTES[route]['distance']
            print(f"The most fuel-efficient route is from {route[0]} to {route[1]}.")
            print(f"Distance: {route_distance} miles, Fuel Usage: {fuel_usage:.2f} gallons")
        else:
            print("Could not calculate a route.")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Program Overview

1. **Data Model**: We define a mock dictionary of routes where each entry contains a tuple of locations and their corresponding distance and fuel efficiency.
   
2. **Core Functions**:
   - `calculate_fuel_usage`: Calculates how much fuel will be used for a given distance and fuel efficiency.
   - `find_most_efficient_route`: Determines the most fuel-efficient route between two points based on predefined routes.
   
3. **Error Handling**:
   - Checks for zero fuel efficiency which would raise a division error.
   - Handles direct case where start and end locations are the same.
   - Checks for routes that do not exist between the chosen locations.
   
4. **User Interaction**:
   - The program prompts for starting and ending locations, then processes and outputs the most fuel-efficient route based on the mock data.

This program is a basic implementation providing insight into the logic of route selection while considering fuel efficiency. For a real-world application, integration with external mapping and traffic services would be necessary to dynamically calculate routes and efficiencies.
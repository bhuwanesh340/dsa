direction = "SNNNEWE"

def shortest_route(direction):
    coordinates = {"x":0, "y":0}

    for d in direction:
        if d == "N":
            coordinates["y"] += 1
        elif d == "S":
            coordinates["y"] -= 1
        elif d == "E":
            coordinates["x"] += 1
        elif d == "W":
            coordinates["x"] -= 1


    # print the route
    final_shortest_route = ""

    if coordinates["x"] >= 0 and coordinates["y"] >= 0:
        print("You are at the 1st Quadrant")
        while coordinates["x"] > 0:
            final_shortest_route += "E"
            coordinates["x"] -= 1
        while coordinates["y"] > 0:
            final_shortest_route += "N"
            coordinates["y"] -= 1


    elif coordinates["x"] < 0 and coordinates["y"] >= 0:
        print("You are at the 2nd Quadrant")
        while coordinates["x"] < 0:
            final_shortest_route += "W"
            coordinates["x"] += 1

        while coordinates["y"] > 0:
            final_shortest_route += "N"
            coordinates["y"] -= 1

    elif coordinates["x"] < 0 and coordinates["y"] < 0:
        print("You are at the 3rd Quadrant")
        while coordinates["x"] < 0:
            final_shortest_route += "W"
            coordinates["x"] += 1
        while coordinates["y"] < 0:
            final_shortest_route += "S"
            coordinates["y"] += 1

    else:
        print("You are at the 4th Quadrant")
        while coordinates["x"] > 0:
            final_shortest_route += "E"
            coordinates["x"] -= 1
        while coordinates["y"] < 0:
            final_shortest_route += "S"
            coordinates["y"] += 1

    return coordinates, final_shortest_route


final_coordinate, shortest_path = shortest_route(direction)
print(f"Shortest route coordinates: X = {final_coordinate['x']}, Y = {final_coordinate['y']}")
print(f"Shortest route: {shortest_path}")
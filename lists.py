if __name__ == '__main__':
    # Create a List of numbers

    lst1 = [3, 4, 2, 0, 1, 0, 8]
    print(lst1)
    # Order with sort built-in function
    lst1.sort(key=None, reverse=False)
    print(lst1)

    #Create a list of planets

    planets = [('Earth', 3), ('Jupiter', 5), ('Mercury', 1), ('Mars', 4)
        , ('Neptune', 8), ('Saturn', 6), ('Uranus', 7), ('Venus', 2)]

    print(planets)

    newplanets = sorted(planets, key=lambda x: x[1], reverse=False)

    print(newplanets)


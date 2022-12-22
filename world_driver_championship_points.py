def get_race_points_from_position(position: str) -> int:
    """
    Los puntos a otorgar se reparten según la siguiente tabla:

    | Posición  | Puntos |
    |-----------|--------|
    | "1"       | 25     |
    | "2"       | 18     |
    | "3"       | 15     |
    | "4"       | 12     |
    | "5"       | 10     |
    | "6"       | 8      |
    | "7"       | 6      |
    | "8"       | 4      |
    | "9"       | 2      |
    | "10"      | 1      |
    | otro caso | 0      |

    Nota: Aparte de las posición "11", "12" y sucesivas, cuando un piloto se retira su posición será "R"
    """

    if position == "1":
        return 25
    elif position == "2":
        return 18
    elif position == "3":
        return 15
    elif position == "4":
        return 12
    elif position == "5":
        return 10
    elif position == "6":
        return 8
    elif position == "7":
        return 6
    elif position == "8":
        return 4
    elif position == "9":
        return 2
    elif position == "10":
        return 1
    else:
        return 0


def get_race_points_from_position_and_fastest_lap(position: str, has_fastest_lap) -> int:
    if position == 'R':
        return get_race_points_from_position(position)
    elif has_fastest_lap and int(position) <= 10:
        return get_race_points_from_position(position) + 1
    return get_race_points_from_position(position)


def get_driver_season_points(driver_season_data: {}) -> int:
    points_accumulated = 0
    for race, race_data in driver_season_data.items():
        points_accumulated += get_race_points_from_position_and_fastest_lap(race_data["position"], race_data["is_fastestlap"])
    return points_accumulated

import json
import logging
import os

import ergast_py

logger = logging.getLogger()


def populate_races_by_driver(year: int) -> [ergast_py.Race]:
    ergast = ergast_py.Ergast()
    races_by_driver = {}
    races = ergast.season(year).get_races()
    for race in races:
        logger.info(f"Getting data from race: {race}")
        round_number = race.round_no
        race_results = ergast.season(year).round(round_number).get_result()
        for driver_race_result in race_results.results:
            driver_id = driver_race_result.driver.driver_id
            if driver_id not in races_by_driver:
                races_by_driver[driver_id] = {}

            races_by_driver[driver_id][race.race_name] = {
                'position': driver_race_result.position_text,
                'is_fastestlap': driver_race_result.fastest_lap.rank == 1,
            }
            if driver_race_result.fastest_lap.time is not None:
                races_by_driver[driver_id][race.race_name]["bestlap"] = driver_race_result.fastest_lap.time.isoformat()

    output_filename = os.path.join(os.getcwd(), "data", f"{year}_races.json")
    with open(output_filename, 'w') as json_file:
        logger.info(f"Writing the data at {output_filename}")
        json.dump(races_by_driver, json_file, indent=4, ensure_ascii=False)


def load_data(year: int) -> {str: {}}:
    """
    Read from a file the json data and transforms it to a dict. The only parameter will indicate the year to load

    :param year:
    :return:
    """

    data_filename = os.path.join(os.path.dirname(__file__), "data", f"{year}_races.json")
    with open(data_filename, 'r') as data_file:
        return json.load(data_file)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    populate_races_by_driver(int(input("Which season you want to get the data from? ")))

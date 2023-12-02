import re

FILEPATH = 'input.in'
TEST_FILEPATH = 'test.in'
GAME_ID_REGEX = r'Game (\d+):'
COLOR_CUBES_DRAWN_REGEX = r'\s*(\d+) (red|green|blue)'


def get_game_id(game_report: str) -> int:
    expression = re.compile(GAME_ID_REGEX)

    game_header = expression.match(game_report)
    game_id = int(game_header.group(1))

    return game_id


def process_game_report(game_report: str) -> [[str]]:
    game = re.sub(GAME_ID_REGEX, '', game_report)
    game = game.replace("\n", "")
    game = game.split(";")
    game = [x.strip(" ") for x in game]
    game = [x.split(",") for x in game]

    return game


def calculate_colors(game_report: str) -> (int, int, int):
    max_red_cubes_drawn, max_green_cubes_drawn, max_blue_cubes_drawn = 0, 0, 0

    game = process_game_report(game_report)

    for drawn_set in game:
        for elem in drawn_set:
            match = re.match(COLOR_CUBES_DRAWN_REGEX, elem)
            number_drawn = int(match.group(1))
            color_drawn = match.group(2)

            if color_drawn == 'red' and max_red_cubes_drawn < number_drawn:
                max_red_cubes_drawn = number_drawn
            elif color_drawn == 'green' and max_green_cubes_drawn < number_drawn:
                max_green_cubes_drawn = number_drawn
            elif color_drawn == 'blue' and max_blue_cubes_drawn < number_drawn:
                max_blue_cubes_drawn = number_drawn

    return max_red_cubes_drawn, max_green_cubes_drawn, max_blue_cubes_drawn


def is_useful_set(colors: dict) -> bool:
    return colors['red'] <= 12 and colors['green'] <= 13 and colors['blue'] <= 14


def filter_useful_games(games: dict) -> [dict]:
    useful_games = [key for key, value in games.items() if is_useful_set(value)]

    return useful_games


def calculate_games_results(file) -> dict:
    games_results = {}

    for game_report in file:
        game_id = get_game_id(game_report)
        games_results[game_id] = {}

        red_cubes, green_cubes, blue_cubes = calculate_colors(game_report)
        games_results[game_id]['red'] = red_cubes
        games_results[game_id]['green'] = green_cubes
        games_results[game_id]['blue'] = blue_cubes

    return games_results


def main():
    with open(FILEPATH, 'r') as file:
        games_results = calculate_games_results(file)

    useful_games = filter_useful_games(games_results)
    sum_of_ids = sum(useful_games)

    print(sum_of_ids)


if __name__ == '__main__':
    main()

from typing import List
from src.infrastructure.services.scraper_services import ScraperServices
from src.infrastructure.queue.publisher import Publisher
import json
from src.dto.console_game_domain_dto import ConsoleGamesListDto, ConsoleGamesDtoSchema


class GameApplication:
    @staticmethod
    def get_details_games(data) -> bool:
        schema = ConsoleGamesDtoSchema()
        schema_validated = schema.load(json.loads(data))
        if schema_validated.errors:
            raise Exception('Dados de entrada inválidos', schema_validated.errors)
        games: ConsoleGamesListDto = schema_validated.data
        sc = ScraperServices()
        g_data_list = []
        for g in games.data:
            g_data = sc.game_details(g.link, g.reference_id, g.console_code)
            g_data_list.append(g_data)

        Publisher.publish('game.details', json.dumps(g_data_list))


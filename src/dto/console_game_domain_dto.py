from datetime import datetime
from typing import List

from marshmallow import Schema, fields, post_load
from src.dto.common.base_dto import BaseDto


class ConsoleGamesListDto(BaseDto):
    def __init__(self, console_code: str = None,
                 reference_id: str = None,
                 title: str = None,
                 link: str = None):
        self.console_code = console_code
        self.reference_id = reference_id
        self.title = title
        self.link = link

    @staticmethod
    def mapper(data):
        return ConsoleGamesListDto(**data)


class ConsoleGamesListDtoSchema(Schema):
    console_code = fields.Str()
    reference_id = fields.Str()
    title = fields.Str()
    link = fields.Str()

    @post_load
    def make_dto(self, data):
        return ConsoleGamesListDto(**data)


class ConsoleGamesDto(BaseDto):
    def __init__(self, data: List[ConsoleGamesListDto] = None):

        self.data = data


    @staticmethod
    def mapper(data):
        return ConsoleGamesDto(**data)


class ConsoleGamesDtoSchema(Schema):

    data = fields.List(fields.Nested(ConsoleGamesListDtoSchema))
    code_transfer = fields.Int()

    @post_load
    def make_model(self, data):
        return ConsoleGamesDto.mapper(data)
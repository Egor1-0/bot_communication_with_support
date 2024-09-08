from aiogram.filters.callback_data import CallbackData


class ContComm(CallbackData, prefix='cont'):
    action: str
    us_id: int
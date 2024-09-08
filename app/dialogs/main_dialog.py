from operator import itemgetter

from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select

from app.states.states import Scroll, Communication
from app.google_sheet import *
from app.database.queries import push_pair


async def user_group(**kwargs):
    output = [] 
    clients_db = load_data_from_google_sheets()
    for user_id in clients_db[1:]:
        output.append((user_id[0], user_id[0]))
    return {
        "products": output,
    }


async def push_pair_from_dialog(callback: CallbackQuery, widget,
                            dialog_manager: DialogManager, item_id: int):
    await push_pair(callback.from_user.id, int(item_id))
    await callback.message.answer("Диалог начат")
    await dialog_manager.done()


scroll_default = Window(
    Const('qwerty'),
    ScrollingGroup(
        Select(
            Format("{item[0]}"),
            id="multiselect",
            items = "products",
            item_id_getter=itemgetter(1),
            on_click=push_pair_from_dialog
        ),
        id='def_scrolling_group',
        width=1,
        height=5,
    ),
    getter=user_group,
    preview_data=user_group,
    state=Scroll.main_menu_scroll
)


scroll_dialog = Dialog(
    scroll_default
)
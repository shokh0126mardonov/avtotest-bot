import asyncio
import httpx

from telegram import Update
from telegram.ext import ContextTypes

from ..service import get_questions,map_question

BASE_URL = "http://testapi.sammkk.uz/"



async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = await get_questions(context.user_data['lang'])

    context.user_data["questions"] = data["items"]
    context.user_data["q_index"] = 0
    context.user_data["score"] = 0

    await send_question(update, context)


async def send_question(update, context):
    data = context.user_data
    q_index = data["q_index"]

    item = data["questions"][q_index]
    q = map_question(item)

    chat_id = update.effective_chat.id

    if q["media"]:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=BASE_URL + q["media"]
        )

    msg = await context.bot.send_poll(
        chat_id=chat_id,
        question=q["question"],
        options=q["options"],
        type="quiz",
        correct_option_id=q["correct_index"],
        explanation=q["explanation"],
        is_anonymous=False,
        open_period=90
    )

    context.bot_data[msg.poll.id] = {
        "chat_id": chat_id,
        "q_index": q_index
    }

    asyncio.create_task(timeout_next(context, chat_id, q_index, 90))


async def timeout_next(context, chat_id, index, delay):
    await asyncio.sleep(delay)

    data = context.application.user_data.get(chat_id)
    if not data:
        return

    if data["q_index"] != index:
        return

    data["q_index"] += 1

    if data["q_index"] < len(data["questions"]):
        fake_update = Update(update_id=0)
        fake_update._effective_chat = type("Chat", (), {"id": chat_id})()
        await send_question(fake_update, context)
    else:
        await context.bot.send_message(
            chat_id,
            f"Test tugadi ✅\nScore: {data['score']}"
        )


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = update.poll_answer
    poll_id = answer.poll_id
    selected = answer.option_ids[0]

    poll_data = context.bot_data.get(poll_id)
    if not poll_data:
        return

    chat_id = poll_data["chat_id"]
    q_index = poll_data["q_index"]

    data = context.application.user_data.get(chat_id)
    if not data:
        return

    if data["q_index"] != q_index:
        return

    item = data["questions"][q_index]
    q = map_question(item)

    # score
    if selected == q["correct_index"]:
        data["score"] += 1

    data["q_index"] += 1

    if data["q_index"] < len(data["questions"]):
        fake_update = Update(update_id=0)
        fake_update._effective_chat = type("Chat", (), {"id": chat_id})()
        await send_question(fake_update, context)
    else:
        await context.bot.send_message(
            chat_id,
            f"Test tugadi ✅\nScore: {data['score']}"
        )
import httpx

async def get_questions(lang:str):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            "http://testapi.sammkk.uz/api/TestCase/GetAll",
            params={
                "language": lang,
                "isRandom": "true",
                "pageSize": 20,
            }
        )
        return res.json()["result"]


def map_question(item):
    options = []
    correct_index = None

    for i, ans in enumerate(item["testAnswers"]):
        text = ans["answerText"].strip()

        if len(text) > 100:
            text = text[:97] + "..."

        options.append(text)

        if ans["isCorrect"]:
            correct_index = i

    options = options[:10]

    if correct_index is None or correct_index >= len(options):
        correct_index = 0

    return {
        "question": item["question"][:300],
        "options": options,
        "correct_index": correct_index,
        "explanation": (item["explanation"] or "")[:200],
        "media": item["mediaUrl"],
    }
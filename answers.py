def get_answer(question):
    answer={"привет": "И тебе привет!", "как дела": "Лучше всех", 
    "пока": "Увидимся"}
    return answer.get(question).lower()
ans = get_answer(input())
print(ans)

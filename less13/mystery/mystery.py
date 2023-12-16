from random import random


class Question:

    def __init__(self, question, answer, list_wrong_choices, complexity=0):
        self.question = question
        self.answer = answer
        self.list_wrong_choices = sorted(list_wrong_choices, key=lambda *args: random())
        self.complexity = complexity
        self.points = 0

    def __str__(self):
        return f"{self.question}\n{self.answer}\n{self.list_wrong_choices}"

    def quiz(self):
        print(f"Question: {self.question}")

        for i, ans in enumerate(self.list_wrong_choices):
            print(f"   {i}.{ans}")
        user_ans = input("Your choice: ")
        if user_ans == "":
            return 0
        elif self.answer == self.list_wrong_choices[int(user_ans)]:
            return 3
        else:
            return -3


quest_d = ["Кто из этих персонажей не дружит с Гарри Поттером?",
           ["Рон Уизли", "Невилл Лонгботтом", "Драко Малфой", "Гермиона Грейнджер"],
           "Драко Малфой"]

q1 = Question(quest_d[0], quest_d[2], quest_d[1])

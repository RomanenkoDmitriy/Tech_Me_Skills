from datetime import datetime
import csv
import os


class User:
    users = []

    def __init__(self, name: str, last_name: str, email: str, password: str):

        User.users.append(self)
        self.id = len(User.users)
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = hash(password)
        self.created_date = datetime.now()
        self.updated_date = ""
        self.role = ""
        self.deleted_date = ""
        self.rating = 0
        self.add_to_csv()

    def add_to_csv(self):

        fime_name = "users.csv"
        path = os.path.join(os.getcwd(), "publication", "data", fime_name)

        with open(path, "w") as file:
            fieldnames = list(self.__dict__.keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in User.users:
                writer.writerow(user.__dict__)

    def update_user(self, name="", last_name="", email="", password=""):

        if name:
            self.name = name

        if last_name:
            self.last_name = last_name

        if email:
            self.email = email

        if password:
            self.password = hash(password)

        self.updated_date = datetime.now()
        self.add_to_csv()

    def del_user(self):

        fime_name = "users.csv"
        path_file = os.path.join(os.getcwd(), "publication", "data", fime_name)

        with open(path_file, "w") as csv_file:

            for index, user in enumerate(User.users):
                if user.id == self.id:
                    del User.users[index]

            fieldnames = list(self.__dict__.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for user in User.users:
                writer.writerow(user.__dict__)


class News:
    news = []

    def __init__(self, heading, body, author):
        News.news.append(self)
        self.id = len(News.news)
        self.heading = heading
        self.body = body
        self.author = author
        self.rating = 0
        self.permission = False
        self.creation_date = datetime.now()
        self.updated_date = ""
        self.deleted_date = ""

    def add_to_csv(self):

        fime_name = "news.csv"
        path = os.path.join(os.getcwd(), "publication", "data", fime_name)

        with open(path, "w") as file:
            fieldnames = list(self.__dict__.keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for n in News.news:
                writer.writerow(n.__dict__)

    def update_news(self, author_id, heading="", body=""):

        if author_id == self.author:
            if heading:
                self.heading = heading
            if body:
                self.body = body
            self.add_to_csv()
        else:
            return False

    def rating_news(self, change):

        if change == "+":
            self.rating += 1
        elif change == "-":
            self.rating -= 1


class Comment:
    comments = []

    def __init__(self, text, author, news):
        Comment.comments.append(self)
        self.id = len(Comment.comments)
        self.text = text
        self.author = author
        self.news = news
        self.creation_date = datetime.now()
        self.updated_date = ""
        self.deleted_date = ""

    def add_to_csv(self):
        fime_name = "comments.csv"
        path = os.path.join(os.getcwd(), "publication", "data", fime_name)

        with open(path, "w") as file:
            fieldnames = list(self.__dict__.keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for comment in Comment.comments:
                writer.writerow(comment.__dict__)

    def update_comment(self, text=""):
        if text:
            self.text = text


class Author(User):

    def __init__(self, name: str, last_name: str, email: str, password: str):

        super().__init__(name, last_name, email, password)

    def create_news(self, heading, body):

        news = News(heading, body, self.id)

    def update_news(self, id, heading="", body=""):

        for news in News.news:
            if news.id == id:
                news.update_news(self.id, heading, body)
                break

    def delete_news(self, id):

        for index, news in enumerate(News.news):
            if news.id == id:
                if self.id == news.id:
                    del News.news[index]
                else:
                    return False
            news.add_to_csv()
            break

    @staticmethod
    def change_rating_news(id, change):

        for news in News.news:
            if news.id == id:
                news.change_rating(change)


class Moder(User):

    def __init__(self, name: str, last_name: str, email: str, password: str):

        super().__init__(name, last_name, email, password)
        self.role = "Moderator"

    def premise_news(self, id_news):
        for news in News.news:
            if news.id == id_news:
                news.permission = True
                news.add_to_csv()
                break

class Administrator(User):

    def __init__(self, name: str, last_name: str, email: str, password: str):
        super().__init__(name, last_name, email, password)
        self.role = "admin"

    def creat_moderator(self):
        pass


user = User("Ivan", "Ivanov", "ivan@mail.ru", "12345")
user2 = User("Igor", "Pupkin", "pupkin@mail.ru", "11111")
user3 = User("Nik", "YYY", "Rjkfider@mail.ru", "22222")

# user2.del_user()
fime_name = "users.csv"
path = os.path.join(os.getcwd(), "publication", "data", fime_name)
with open(path, "r") as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)

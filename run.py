from user import User

user = {"name": "John Dou", "age": 30, "address": "New York"}
john_dou = User(user)
john_dou.save()
john_dou.update({"name": "John Dou", "age": 30, "address": "L A"})

uncle_sam = User(input())
uncle_sam.save()

john_dou.db.close()
uncle_sam.db.close()

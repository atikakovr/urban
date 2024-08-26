from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
	return "Главная страница"


@app.get("/user")
async def user_info(username: str = 'Alex', age: int = 54):
	return {"User": username, "age": age}


@app.get("/user/admin")
async def admin_panel():
	return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def users_id(user_id):
	return f"Вы вошли как пользователь № {user_id}"


@app.get("/hello/{name}")
async def say_hello(name: str):
	return {"message": f"Hello {name}"}

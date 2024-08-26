from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
	return "Главная страница"


@app.get("/user/admin")
async def admin_panel():
	return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def users_id(user_id):
	return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{user_id}")
async def news(
		username:
		Annotated[str, Path(min_length=3, max_length=15, description="Введите имя пользователя", example="Alex")],
		user_id: int = Path(le=1500, ge=0)):
	return {"message": f"Hello, {username}:{user_id}"}


@app.get("/user")
async def user_info(username: str = 'Alex', age: int = 54):
	return {"User": username, "age": age}

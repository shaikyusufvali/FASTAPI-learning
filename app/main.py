from fastapi import FastAPI

app = FastAPI()

# Temporary database
users = [
    {"id": 1, "name": "Yusuf", "age": 23},
    {"id": 2, "name": "Rahul", "age": 24}
]


# 1. GET - Read users
@app.get("/users")
def get_users():
    return users


# 2. POST - Create user
@app.post("/users")
def create_user(user: dict):

    users.append(user)

    return {
        "message": "User created successfully",
        "user": user
    }


# 3. PUT - Complete update
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):

    for user in users:

        if user["id"] == user_id:

            user.update(updated_user)

            return {
                "message": "User updated",
                "user": user
            }

    return {"message": "User not found"}


# 4. PATCH - Partial update
@app.patch("/users/{user_id}")
def partial_update(user_id: int, data: dict):

    for user in users:

        if user["id"] == user_id:

            user.update(data)

            return {
                "message": "Partial update successful",
                "user": user
            }

    return {"message": "User not found"}


# 5. DELETE - Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return {"message": "User deleted"}

    return {"message": "User not found"}
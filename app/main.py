from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Welcome to FastAPI",
        "developer": "Shaik Yusuf Vali",
        "status": "Success"
    }


@app.get("/about")
def about():

    return {
        "name": "Yusuf",
        "role": "AI ML Developer",
        "learning": "FastAPI"
    }
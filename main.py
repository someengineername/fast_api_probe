from fastapi import FastAPI
import random


def make_app():
    application = FastAPI()

    @application.get("/about")
    async def about():
        random_value = random.randint(1, 500)

        return {"Message": "Welcome!", "Value": f"{random_value}"}

    return application


if __name__ == '__main__':
    import uvicorn

    new_app = make_app()

    uvicorn.run(new_app, host='0.0.0.0', port=8888)

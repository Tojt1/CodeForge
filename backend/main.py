from fastapi import FastAPI, HTTPException
import services
from schemas import Register
import exceptions

app = FastAPI()

@app.get("/")
def say_hello():
    return {"information": "Hello World!"}


@app.post("/register")
def register_user(user:Register):
    try:
        services.register_user(user)
        return {"information":"Account have been successfully created"}
    except exceptions.EmailAdressInUseError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except exceptions.InvalidEmailError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except exceptions.AddusertoDBError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
from fastapi import FastAPI, HTTPException
import services
from schemas import Register, Login
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

@app.post("/login")
def login_user(user:Login):
    try:
        return services.sing_in(user)
    except exceptions.EmailDoesNotExistsError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except exceptions.InvalidEmailError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except exceptions.InvalidPasswordError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except exceptions.USerNotFoundError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
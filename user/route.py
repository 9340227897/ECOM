from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="user/templates")


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/registration/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


# @router.post('/users', response_model=User_Pydantic)
# async def create_user(user: UserIn_Pydantic):
#     user_obj = User(email= user.email, phone = user.phone, password_hash=bcrypt.hash(user.password_hash), Confirm_password=user.Confirm_password)
#     await user_obj.save()
#     return await User_Pydantic.from_tortoise_orm(user_obj)
#

@router.get("/login/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/profile/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})


@router.get("/orders/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("orders.html", {"request": request})



@router.get("/changepassword/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("changepassword.html", {"request": request})




@router.get("/address/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("address.html", {"request": request})


@router.get("/addtocart/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("addtocart.html", {"request": request})


@router.get("/buynow/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("buynow.html", {"request": request})
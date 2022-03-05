
from fastapi import Body, FastAPI
# from . import models
from sqlalchemy.orm import Session
# from .database import engine
from .routers import post, user, auth
from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"] #Here you basically allow the origins from which your API's can be called. 
#Its a list of origins. "*" means allow all domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#what we do is create different py files for various routes and then
#use the main route which is app to combine routes
app.include_router(post.router)
app.include_router(user.router)
#app.include_router(auth.router)



# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database="fastapi",user='postgres',
#         password='Password123',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DB connection was successfull")
#         break
#     except Exception as err:
#         print(f"Connecting to db failed with {err}")
#         time.sleep(2) 








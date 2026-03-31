from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    username:str
    hashed_password:str
    coins:int

class UserCreateDTO(BaseModel):
    username:str
    hashed_password:str

class UserByIdDTO(BaseModel):
    id:int

class UserByNameDTO(BaseModel):
    username:str

class UserCreateDTO(BaseModel):
    username:str
    hashed_password:str

class UserUpdateDTO(BaseModel):
    username:str
    coins:int

class UserUpdateUserNameDTO(BaseModel):
    id:int
    username:str

class UserUpdatePasswordDTO(BaseModel):
    id:id
    hashed_password:str
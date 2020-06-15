from dataclasses import dataclass

@dataclass
class user():
    id: int
    firstName: str
    lastName: str
    userName: str
    email: str
    admin: bool = False

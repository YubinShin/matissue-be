from enum import Enum, IntEnum
from pydantic import BaseModel, Field
from typing import List
from nanoid import generate


class Category(str, Enum):
    korean = "korean"
    chinese = "chinese"
    japanese = "japanese"
    western = "western"
    vegetarian = "vegetarian"
    other = "other"


class Ingredients(BaseModel):
    name: str
    amount: str


class LevelEnum(IntEnum):
    EASY = 0
    MEDIUM = 1
    HARD = 2


class Information(BaseModel):
    serving: int  # 인원
    time: int  # 조리시간
    level: LevelEnum  # 난이도


class SequenceItem(BaseModel):
    picture: str  # url 들어갈예정
    description: str


class RecipeBase(BaseModel):
    recipe_id: str = Field(default_factory=lambda: generate())
    recipe_title: str
    recipe_thumbnail: str
    recipe_video: str
    recipe_description: str
    recipe_category: List[Category]
    recipe_info: Information
    recipe_ingredients: List[Ingredients]
    recipe_sequence: List[SequenceItem]
    recipe_tip: str
    recipe_view: int = Field(default=0)
    recipe_like: int = Field(default=0)
    user_id: str

# class RecipeList(RecipeBase):
#     recipe_id: str = Field(default_factory=lambda: generate())
#     recipe_title: str
#     recipe_thumbnail: str
#     recipe_like: int = Field(default=0)
#     user_id: str


# class RecipeSearchByCategory(RecipeBase):
# class RecipeSearchByTime(RecipeBase):
# class RecipeSearchByIngredient(RecipeBase):
from dotenv import load_dotenv
import random
import string
import time
import os
import abc
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import httpx
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def random_string(n: int) -> str:
    return "".join((random.choice(string.ascii_letters) for _ in range(n)))


class GenerationService(abc.ABC):
    @abc.abstractmethod
    async def generate_random_article_idea(self):
        pass

    @abc.abstractmethod
    async def generate_technical_guide(self):
        pass

    @abc.abstractmethod
    async def generate_fiction(self):
        pass


class ArticleGenerationService(GenerationService):
    async def generate_random_article_idea(self) -> dict:
        async with httpx.AsyncClient() as client:
            await asyncio.sleep(2)
        return {
            "title": random_string(10),
            "idea": random_string(30),
        }

    async def generate_technical_guide(self) -> dict:
        async with httpx.AsyncClient() as client:
            await asyncio.sleep(2)
        return {
            "title": random_string(10),
            "idea": random_string(40),
        }

    async def generate_fiction(self) -> dict:
        async with httpx.AsyncClient() as client:
            await asyncio.sleep(2)
        return {
            "title": random_string(10),
            "idea": random_string(50),
        }


generation = ArticleGenerationService()

@app.get("/generate")
async def generate_inform(type: str):
    types = {'article':generation.generate_random_article_idea, 
             'guide': generation.generate_technical_guide, 
             'fiction': generation.generate_fiction
            }
    if type not in types:
        raise Exception("Invalid type")
    else:
        func = types[type]
        return await func()
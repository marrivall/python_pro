from dotenv import load_dotenv
import random
import string
import time
import os
import abc
from fastapi import FastAPI
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

@app.get("/article-ideas")
async def article_idea():
    return await generation.generate_random_article_idea()

@app.get("/technical-guide")
async def technical_guide():
    return await generation.generate_technical_guide()

@app.get("/fiction")
async def fiction():
    return await generation.generate_fiction()
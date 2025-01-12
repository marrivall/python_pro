import time
import random
import httpx
import asyncio
import requests
import argparse

BASE_URL = "https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

def http_request(url: str) -> str:
    print(f"requesting {url}")
    response = requests.get(url).json()
    return response["name"]

async def ahttp_request(url: str) -> str:
    print(f"requesting {url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()["name"]

def get_urls(n: int) -> list[str]:
    return [BASE_URL.format(pokemon_id=random.randint(1, 500)) for _ in range(n)]

def sync_pokemons():
    urls: list[str] = get_urls(n=50)
    results = [http_request(url) for url in urls]
    for result in results:
        print(result)
    return results

async def async_pokemons():
    urls: list[str] = get_urls(n=50)
    tasks = [ahttp_request(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
    return results

def main():
    parser = argparse.ArgumentParser(
        prog='Pokemon',
        description='Using httpx/request',
        epilog='Choose httpx/request')
    parser.add_argument('library',  help="Choose library")

    args = parser.parse_args()
    if args.library not in ["httpx", "requests"]:
        print("Invalid choice. Choose from httpx or requests")
        return

    start = time.perf_counter()
    if args.library == "httpx":
        data = asyncio.run(async_pokemons())
        print(data)
        print(f"the len of the collection: {len(data)}")
    elif args.library == "requests":
        sync_data = sync_pokemons()
        print(sync_data)
        print(f"the len of the collection: {len(sync_data)}")
    end = time.perf_counter()
    print(f"execution time: {end - start}")

if __name__ == "__main__":
    raise SystemExit(main())

# Repeat classwork async - example with httpx (or aiohttp) library instead of  to_thread
# The execution should be done in a single thread (just use external async library)
# As a user I would like to write python run.py httpx or  python run.py requests to specify the package
# from the CLI. Use argparse (or click as alternative) to parse CLI arguments in Python
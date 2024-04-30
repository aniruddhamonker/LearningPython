import asyncio
import requests
import time

def make_web_request(url):
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
    return (f"The response code for url: {url} is : {response.status_code}")

async def async_web_request(url):
    async_response = await asyncio.to_thread(make_web_request, url)
    return async_response

async def main():
    urls = [
        'https://www.wyze.com/',
        'https://www.apple.com/',
        'https://phptravels.com/',
        'https://www.amazon.com/'
    ]
    t1 = time.perf_counter()
    result = await asyncio.gather(*[async_web_request(url) for url in urls])
    t2 = time.perf_counter()
    total_time = t2 -t1
    print(f"Total time taken to fetch all urls:{total_time}")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
    # loop=asyncio.get_event_loop()
    # loop.run_until_complete(main())
    


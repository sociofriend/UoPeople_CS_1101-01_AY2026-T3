import asyncio
import python_weather
from datetime import datetime


def now_str_ms() -> str:
    # %f = microseconds (6 digits). Keep first 3 digits => milliseconds.
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


class WeatherClient:
    async def get_temperature(self, city: str) -> float:
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            print(f"[{now_str_ms()}] Real function implementation:")
            weather = await client.get(city)
            return float(weather.temperature)


class MockWeatherClient:
    async def get_temperature(self, city: str) -> float:
        print(f"[{now_str_ms()}] Mock function implementation:")
        return 25.0


async def main() -> None:
    city = "Armenia"

    # Pick ONE:
    client = MockWeatherClient()
    # client = WeatherClient()

    temp = await client.get_temperature(city)
    print(f"[{now_str_ms()}] Temperature in {city}: {temp}°C\n")


if __name__ == "__main__":
    asyncio.run(main())
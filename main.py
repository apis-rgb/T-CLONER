from utils.innit import *
from func.cloner import *
from func.guild_info import *
from func.token_checker import *

async def menu():
    while True:
        clear()
        logo()
        o = f"""
                {r}[{r}01{r}]{r} Clone Server
                {r}[{r}02{r}]{r} Server Info
                {r}[{r}03{r}]{r} Developer"""
        print(o)
        cs = input(f"                {r}[{r}T͇-͇L͇O͇A͇D͇{r}]{r} >> ")

        if cs == "1":
            await cloner()
        elif cs == "2":
            await guild_info()
        elif cs == "3":
            await token_checker()


if __name__ == "__main__":
    asyncio.run(menu())
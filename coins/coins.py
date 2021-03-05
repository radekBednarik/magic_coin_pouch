'''Generates coins :)
'''
from random import choice
from typing import Callable, Dict, Generator, Sequence

COINS: Sequence = [1, 2, 5, 10, 20, 50]


def create_coin(coins_seed: Sequence) -> int:
    """Takes random coin from coins seed and returns.

    Args:
        coins_seed (Sequence): coins frozen set

    Returns:
        int: coin
    """
    return choice(coins_seed)


def take_from_magic_pouch(how_many_times: int, coins_seed: Sequence) -> Generator:
    """Creates how many coins you want - from thin air! :)

    Args:
        how_many_times (int): how many times you want to
        pull the random coin from the pouch?
        coins_seed (Sequence): available coins (you do not want to get buttons!)

    Yields:
        Generator: magic generator
    """
    counter: int = 0
    while counter < how_many_times:
        yield create_coin(coins_seed)
        counter += 1


def put_coins_in_stash(
    take_the_coin: Callable, how_many_times: int, coins_seed: Sequence
) -> Dict[str, int]:
    """Returns stash full of coins and with coins stacked
    on columns according their value for your convenience!

    Args:
        take_the_coin (Callable): as long as you are taking, it keeps on giving
        how_many_times (int): how many times you want to pull the coin
        coins_seed (Sequence): available set of coins

    Returns:
        Dict[str, int]: your stash!
    """
    stash: Dict[str, int] = {}

    for coin in take_the_coin(how_many_times, coins_seed):
        if str(coin) not in list(stash.keys()):
            stash[str(coin)] = 1
            continue
        stash[str(coin)] += 1

    return dict(sorted(stash.items(), key=lambda items: int(items[0])))


def main() -> None:
    """Main func."""
    print(put_coins_in_stash(take_from_magic_pouch, 1000000, COINS))


if __name__ == "__main__":
    main()

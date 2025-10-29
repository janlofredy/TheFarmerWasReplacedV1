from helpers import *
def run():
    clear()
    while True:
        if num_items(Items.Hay) >= 100000000:
            break
        jobEverywhere(harvest)
if __name__ == "__main__":
    run()

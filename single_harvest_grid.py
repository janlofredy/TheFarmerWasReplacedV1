from helpers import *
def justHarvest():
    harvest()
def run():
    flyTo(0,0)
    jobEverywhere(justHarvest)
if __name__ == "__main__":
    run()

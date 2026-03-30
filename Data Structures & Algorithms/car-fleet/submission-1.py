class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # lets use up O(nlogn) constraint with sorting
        # I zip to keep things aligned
        cars = sorted(list(zip(position, speed)))
        # treat cars like a stack... I hope that's not cheating
        fleets = 0
        time = 0 # used to detect fleets
        while len(cars) > 0:
            head_car = cars[-1]
            # if the current car cannot reach the target <=
            # time than previous car, it's a different fleet
            # why < is fine? Faster cars get blocked by leading car
            if head_car[1]*time + head_car[0] < target:
                # new fleet -> will take a different time to reach
                fleets += 1
                # take the ceiling to round up floats
                time = (target-head_car[0]) / head_car[1]
            # regardless, pop it
            cars.pop(-1)
        return fleets

"""
Failed test case:
target=10; position=[8,3,7,45]
"""
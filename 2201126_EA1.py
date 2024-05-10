import heapq

# For initial assumption, I assumed that all the cannibals and missionaries are on left side bank
# Boat is also on the left side

class State:
        def __init__(self, missionaries, cannibals, boat, cost):

                self.missionaries = missionaries
                self.cannibals = cannibals
                self.boat = boat
                self.cost = cost

        def is_validate(self):
                if self.missionaries < 0 or self.missionaries > 3:
                        return False

                if self.cannibals < 0 or self.cannibals > 3:
                        return False

                if self.missionaries < self.cannibals and self.missionaries > 0:
                        return False

                if (3 - self.missionaries) < (3 - self.cannibals) and (3 - self.missionaries) > 0:
                        return False

                return True

        def is_goal(self):
                return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

        def get_transfer(self):
                transfers = []

                if self.boat == 1:
                        for m in range(3):
                                for c in range(3):
                                        if 1 <= m + c <= 2:
                                                new_state = State(self.missionaries - m, self.cannibals - c, 0, self.cost + 10 * m + 20 * c)
                                                print "No. of missionaries transfer to the right side bank : ",m
                                                print "No. of cannibals transfer to the right side bank    : ",c
                                                print
                                                if new_state.is_validate():
                                                        transfers.append(new_state)

                else:
                        for m in range(3):
                                for c in range(3):
                                        if 1 <= m + c <= 2:
                                                new_state = State(self.missionaries + m, self.cannibals + c, 1, self.cost + 10 * m + 20 * c)
                                                print "No. of missionaries transfer to the left side bank  : ",m
                                                print "No. of cannibals transfer to the left side bank     : ",c
                                                print
                                                if new_state.is_validate():
                                                        transfers.append(new_state)

                return transfers

        def __lt__(self, other):
                return self.cost < other.cost

def uniform_cost_search_algorithm():
        initial_state = State(3, 3, 1, 0 )
# Here State is no. of missionaries, no. of cannibals, no. of boat all on the left side and cost ( initial cost )
        open_list = []
        heapq.heappush(open_list, initial_state)

        while open_list:
                current_state = heapq.heappop(open_list)
                if current_state.is_goal():
                        return current_state
                for transfer in current_state.get_transfer():
                        heapq.heappush(open_list, transfer)

        return None

def printing_solution(solution):
        if solution is None:
                print "No solution found"
                return

        print "Minimum cost to transfer them without violation :", solution.cost
        print "Missionaries left on left side bank:", solution.missionaries
        print "Cannibals left  on left side bank:", solution.cannibals
        print "Boat on right side bank:", "Yes" if solution.boat == 0 else "No"

if __name__ == "__main__":
        solution = uniform_cost_search_algorithm()
        printing_solution(solution)
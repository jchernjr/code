from copy import deepcopy
from typing import List, DefaultDict, Tuple, Optional, Set
import pprint

# level 129
# INPUT = [  # these are in reverse order (top to bottom) as the Tube class wants
#     "skyblu/blue/org/green",
#     "ltgrn/ltgrn/ltgrn/skyblu",
#     "dkblu/mag/red/blue",
#     "blue/pink/dkblu/dkgrn",
#     "green/ltgrn/org/mag",
#     "dkgrn/dkgrn/green/yel",
#     "gray/pink/blue/yel",
#     "org/mag/red/dkblu",
#     "gray/red/pink/red",
#     "green/dkgrn/yel/org",
#     "skyblu/pink/mag/gray",
#     "yel/gray/dkblu/skyblu",
#     "",
#     "",
# ]
#
#
# INPUT = [
#     "yel/grn/yel/grn",
#     "grn/yel/grn/yel",
#     "",
# ]

# level 131
INPUT = [
    "red/grn/org/sky",
    "sky/sky/mag/ltgrn",
    "ltgrn/sky/pink/navy",
    "dkgrn/dkgrn/yel/org",
    "ltgrn/navy/gray/yel",
    "pink/yel/mag/blue",
    "org/gray/yel/gray",
    "blue/mag/grn/org",
    "mag/blue/pink/dkgrn",
    "grn/grn/gray/red",
    "red/dkgrn/navy/navy",
    "ltgrn/red/blue/pink",
    "",
    "",
    "",
]


class Tube:

    def __init__(self, max_qty: int, initial_colors: List[str]):
        """:param initial_colors: name of colors, in order from bottom to top"""
        self.max_qty = max_qty
        self.colors = list(initial_colors)

    def get_top_color(self) -> Tuple[str, int]:
        """:return: the name and amount of the top color in this tube, or ('', 0) if empty."""
        if len(self.colors) == 0:
            return '', 0

        top_color = self.colors[-1]
        num_found = 1
        for i in range(2, len(self.colors) + 1):
            if self.colors[-i] == top_color:
                num_found = i
            else:
                break
        return top_color, num_found

    def can_take_color(self, color: str) -> int:
        """:return: how many of the given color can be poured onto the top of this tube.
        if this tube is empty, returns the max qty.
        if the requested color is NOT the top color of this tube, returns 0.
        otherwise, returns the number of spaces remaining in this tube.
        """
        if len(self.colors) == 0:
            return self.max_qty
        last_color = self.colors[-1]
        if last_color == color:
            return self.max_qty - len(self.colors)
        return 0

    def add_color(self, color: str, amt: int) -> 'Tube':
        """Note: does not check if this color and amount can be poured correctly here. Use can_take_color to check.
        :return: a new Tube instance with the added color."""
        t = Tube(self.max_qty, self.colors)
        t.colors.extend([color] * amt)
        return t

    def remove_top_units(self, amt: int) -> 'Tube':
        """Note: does not check that this many units exist in this tube."""
        return Tube(self.max_qty, self.colors[: -amt])

    def is_empty(self) -> bool:
        return len(self.colors) == 0

    def is_complete(self) -> bool:
        """:return: True if this tube is either full of one color or empty."""
        num = len(self.colors)
        return num == 0 or (num == self.max_qty and self.is_all_one_color())

    def is_all_one_color(self) -> bool:
        return len(set(self.colors)) == 1

    def __str__(self) -> str:
        if len(self.colors) == 0:
            return ''
        return '/'.join(self.colors)


class SearchNode:

    counter = 0

    def __init__(self, prev_node: Optional['SearchNode'],
                 tubes: List[Tube],
                 allowable_pours: Optional[List[List[bool]]] = None,
                 incoming_pour_tube_indexes: Optional[Tuple[int, int]] = None,
                 recursions_left: int = 200,
                 seen_states: Set[str] = set()):
        """
        :param prev_node: previous search node, used to reconstruct the path back to the start for a winning node.
        :param tubes: list of color tubes at the beginning of this game position (search node).
            Note: Tube instances may be shared with other search nodes, as they are considered immutable;
            if we pour into a tube, we will make new instances.

        :param allowable_pours: matrix of allowable pours from tube_i to tube_j,
            to avoid pouring back into the same tube(s) again (back and forth to infinity).
            Note: it is possible to have an infinite cycle with two or more pairs of tubes, pouring back and forth,
            hence we need to remember which pours are not currently allowable.
            Rules:
              A tube which was just poured into loses eligibility to pour back into tube it came from
              (in addition to all the previous tubes that poured into it and lost eligibility).
              A tube which just poured out becomes eligible for every tube to pour into again (bc the top color
              may have changed), except the one it just poured into.

        :param incoming_pour_tube_indexes: track the pour that resulted in this node, for backtracking to the starting
            state from a winning state.

        :param recursions_left: limit the complexity of solution to a sane value (python's limit is 1000)

        :param seen_states: a set of string-representations of test-tube configurations, for cycle detection/debugging.
        """
        self.prev_node = prev_node
        self.tubes = tubes
        self.allowable_pours = allowable_pours if allowable_pours else [[True] * len(tubes) for _ in range(len(tubes))]
        self.incoming_pour_tube_indexes = incoming_pour_tube_indexes
        self.recursions_left = recursions_left
        self.seen_states = seen_states

        SearchNode.counter += 1
        self.count_id = SearchNode.counter

    def get_valid_pours(self) -> List[Tuple[int, int, str, int]]:
        """:returns: list of tuples of (source tube index, dest tube index, color name, color amount)
        of valid pours/moves from this game position (search node)."""
        move_tuples = []
        for source_i in range(len(self.tubes)):
            source_tube = self.tubes[source_i]
            if source_tube.is_empty() or source_tube.is_complete():
                continue  # don't needlessly pour from a completed tube (and cannot pour from an empty one)

            source_color, source_amt = source_tube.get_top_color()
            for dest_i in range(len(self.tubes)):
                if dest_i == source_i:
                    continue  # don't pour into yourself
                if not self.allowable_pours[source_i][dest_i]:
                    continue

                dest_tube = self.tubes[dest_i]
                if source_tube.is_all_one_color() and dest_tube.is_empty():
                    continue  # don't needlessly pour a tube of one color into another empty tube

                space_avail = dest_tube.can_take_color(source_color)
                if space_avail == 0:
                    continue  # can't pour, already full
                else:
                    # can pour the lesser of (amount of source we have, amount of space available in dest)
                    move_tuples.append((source_i, dest_i, source_color, min(space_avail, source_amt)))

        return move_tuples

    def get_allowable_pour_matrix(self, source_i: int, dest_i: int) -> List[List[bool]]:
        output = deepcopy(self.allowable_pours)

        # For the source tube, since it's changed, everyone can pour into it, except the destination
        for i in range(len(self.tubes)):
            if i != dest_i:
                output[i][source_i] = True

        # For the destination tube, it loses eligibility to pour into the source tube.
        # (it also retains any existing ineligibility from previous pours)
        output[dest_i][source_i] = False

        return output

    def is_complete(self) -> bool:
        return all([t.is_complete() for t in self.tubes])

    def get_pour_sequence(self) -> List[Tuple[int, int]]:
        if self.prev_node is not None:
            return self.prev_node.get_pour_sequence() + [self.incoming_pour_tube_indexes]
        return []

    def do_search(self) -> List[Tuple[int, int]]:
        if self.is_complete():
            return self.get_pour_sequence()

        if self.recursions_left == 0:
            return []  # didn't find a solution in this branch

        state_str = self.tubes_to_str()
        if state_str in self.seen_states:
            print("ALREADY SEEN: " + state_str)
            return self.get_pour_sequence()
        self.seen_states.add(state_str)

        pour_tuples = self.get_valid_pours()
        if not pour_tuples:
            print("DEAD END")
            # return self.get_pour_sequence()

        for source_i, dest_i, color, amt in pour_tuples:
            modified_tubes = list(self.tubes)
            modified_tubes[source_i] = self.tubes[source_i].remove_top_units(amt)
            modified_tubes[dest_i] = self.tubes[dest_i].add_color(color, amt)
            pour_sequence_step = (source_i, dest_i)
            allowable_pours = self.get_allowable_pour_matrix(source_i, dest_i)
            next_node = SearchNode(self, modified_tubes, allowable_pours, pour_sequence_step, self.recursions_left - 1)

            # print(f"From node {self.count_id} pouring {amt} {color} {source_i}->{dest_i} (rr {self.recursions_left -1})")
            # self.print_tf_matrix(allowable_pours)
            found_result = next_node.do_search()

            if found_result:
                return found_result

        # didn't find anything from this search position
        # remove this seen state, because we may reach it from a different branch of the tree when we backtrack
        self.seen_states.remove(state_str)
        return []

    def print_tf_matrix(self, tf_matrix: List[List[bool]]) -> None:
        lines = [''.join(['.' if elem else 'X' for elem in row]) for row in tf_matrix]
        print('\n'.join(lines))

    def tubes_to_str(self) -> str:
        tube_strs = [str(t) for t in self.tubes]
        return '|'.join(tube_strs)


if __name__ == "__main__":
    tubes = []
    for init_str in INPUT:
        colors = list(reversed(init_str.split("/")))
        if colors == ['']:
            colors = []
        tubes.append(Tube(4, colors))

    # sanity check that we have 4 units of each color
    color_count = DefaultDict[str, int](int)
    for t in tubes:
        for c in t.colors:
            color_count[c] += 1
    print(color_count)

    # set up initial search position
    search_node = SearchNode(None, tubes)

    result = search_node.do_search()

    print(f"Found solution with {len(result)} steps.  Note, this may not be the shortest.")
    print(result)




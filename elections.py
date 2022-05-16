# Jacqueline Unciano, jdu5sq
# HW Elections

state_winners = {}


def add_state(name, votes):
    """
    Takes in a state name and a dictionary of the specific state election results and updates the
    global dictionary of every state's winner
    :param name: state name
    :param votes: dictionary of the specific state election
    :return: updates the global dictionary of every state's winner
    """
    global state_winners
    highest_vote = 0
    for rank in votes.values():
        if rank > highest_vote:
            highest_vote = rank
    for candidate, rank in votes.items():
        if highest_vote == rank:
            winners = candidate
            state_winners[name] = winners
    return state_winners


def winner(college):
    """
    Takes in a dictionary of each states number of electoral votes and returns the winner of the
    election based off of the global dictionary's results
    :param college: A dictionary of each states number of electoral votes
    :return: Returns the winner of the election based off of the global dictionary's results
    """
    global state_winners
    sum_all = sum(college.values())
    for state in state_winners.keys():
        if state not in college.keys():
            college[state] = 0
    for current_state in college.keys():
        if current_state not in state_winners.keys():
            sum_all -= college[current_state]
    fifty_all = sum_all/2
    list_states = list(state_winners.keys())
    list_winners = list(state_winners.values())
    final_winner = ""
    for state in list_states:
        total_votes = 0
        position = 0
        for person in list_winners:
            if state_winners[state] == person:
                current_state = list_states[position]
                total_votes += college[current_state]
            position += 1
        if total_votes >= fifty_all:
            final_winner += state_winners[state]
            break
    if final_winner == "":
        final_winner = "No Winner"
        return final_winner
    else:
        return final_winner


def clear():
    """
    Resets the global dictionary
    :return: A cleared global dictionary
    """
    global state_winners
    state_winners = {}
    return state_winners

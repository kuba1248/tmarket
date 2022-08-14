from django import template
from transfer.actions import actions
from transfer.views import *
import random

register = template.Library()

@register.simple_tag
def update_var(value):
    '''updates existing vars in template'''
    return value

@register.simple_tag
def generateRandomEvent(action):
    event = ''
    if action == 'attack':
        weights = [0.15, 0.05, 0.1, 0.2, 0.5]
        event = random.choice(random.choices(actions['attack'], weights))
    elif action == 'defense':
        weights = [0.2, 0.05, 0.15, 0.2, 0.2, 0.3]
        event = random.choice(random.choices(actions['defense'], weights))

    return event

@register.simple_tag
def generateAction():
    action = ''
    randomNumber = random.randint(1, 2)
    if randomNumber == 1:
        action = 'attack'
    elif randomNumber == 2:
        action = 'defense'

    return action

@register.simple_tag
def generateRandomTeam(team1, team2):
    randomTeam = random.randint(1, 2)
    if randomTeam == 1:
        team = team1
    else:
        team = team2

    return team

@register.simple_tag
def cut_play_type(play_type):
    '''cuts the play type to determine a play subtype'''
    return play_type

@register.simple_tag
def find_player(player_list):
    '''returns a random player for the specific positions'''
    player = random.randint(0, len(player_list) - 1)
    return player_list[player]

@register.simple_tag
def pass_output(yards_gained):
    '''outputs a string based on yardage for passes'''
    if yards_gained == 'fumble':
        return 'fumbled by'
    elif yards_gained == 'interception':
        return 'intercepted, intended for'
    elif yards_gained == '0':
        return 'incomplete to'
    elif yards_gained == '1':
        return 'for 1 yard to'
    else:
        return 'for ' + str(yards_gained) + ' yards to'

@register.simple_tag
def run_output(yards_gained):
    '''outputs a string based on yardage for runs'''
    if yards_gained == 'fumble':
        return 'fumbled'
    elif yards_gained == '1':
        return 'for 1 yard'
    else:
        return 'for ' + str(yards_gained) + ' yards'

@register.simple_tag
def get_name(tup):
    '''gets the team name from a Team tuple'''
    return tup[0]


@register.simple_tag
def app():
    # print('teams: ', teams)  # teams: ['Barca', 'Chelsea']
    # print('team_names[0]', team_names[0])  # Barca
    # print('team_names[1]', team_names[1])  # Chelsea
    teams = []
    team_names = []
    for t in Team.objects.all():
        team_names.append(t.team_name)
        teams.append(t.team_name)
        t.delete()
    print('teams: ', teams)    # teams: ['Barca', 'Chelsea']
    print('team_names[0]', team_names[0])    # Barca
    print('team_names[1]', team_names[1])    # Chelsea

    team1 = team_names[0]
    print('team1: ', team1)

    team2 = team_names[1]
    print('team2: ', team2)

    if team1 == team2:
        team2 = random.choice(teams)

    # if team1:
    #     return render(request, 'simulate.html')

    player_team = input(f'Which team you choose? | {team1}, {team2}: ')

    if player_team == team1 or player_team == team2:

        score = {team1: 0, team2: 0}
        print(f'Match Start! {team1} vs {team2}')
        # time.sleep(0.5)
        i = 1
        while i < 91:
            action = generateAction()
            event = generateRandomEvent(action)
            # time.sleep(0.5)
            team = generateRandomTeam(team1, team2)
            if event == '':
                pass
            else:
                print(f'{i}.{team}: {event}')

            if event == "Foul":
                possibilities = ['Red Card', 'Yellow Card', 'Free Kick', 'Penalty', '']
                weights = [0.05, 0.3, 0.2, 0.05, 0.4]
                event = random.choice(random.choices(possibilities, weights))
                if event == '':
                    print('Referee starts game after foul')
                else:
                    print(f'Referee decide to: {event}')
                    # time.sleep(0.5)

            if event == "Goal":
                score[team] = score[team] + 1
                print(f'Score: {score}')

            if event == "Free Kick":
                randomNumber = random.randint(1, 10)
                if randomNumber == 10:
                    score[team] = score[team] + 1
                    print('Co za piekna bramka z rzutu wolnego!')
                    print(f'Score: {score}')
                else:
                    print('Niestety zmarnowali okazje na bramke z rzutu wolnego!')

            if event == "Penalty":
                sides = ['left', 'center', 'right']
                if team == player_team:

                    player_shoot = input('Where you want to shoot? (left, center, right) ')
                    goalkeeper = random.choice(sides)
                    if player_shoot == goalkeeper:
                        print('Goalkeeper defends the penalty!!')
                        print(f'Goalkeeper go to: {goalkeeper}')
                    else:
                        print('Goal!')
                        print(f'Goalkeeper go to: {goalkeeper}')
                        score[team] = score[team] + 1
                        print(f'Score: {score}')
                else:
                    playerGoalkeeper = input('Where you want to go with your goalkeeper? (left, center, right) ')
                    computerShoot = random.choice(sides)
                    if computerShoot == playerGoalkeeper:
                        print('Goalkeeper defends the penalty!!')
                        print(f'Shooter shoot to: {computerShoot}')
                    else:
                        print('Goal!')
                        print(f'Shooter shoot to: {computerShoot}')
                        score[team] = score[team] + 1
                        print(f'Score: {score}')

            if i == 45:
                print('Przerwa!')
                print(score)
                # time.sleep(3)
            i += 1
        print(score)
        # return render(request, 'simulate.html', {'score': score})
    else:
        print('You must enter the correct name of the team')
        return

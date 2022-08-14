from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import api_view
from django.utils import timezone

from .models import Market, Myteam, League, Team
from .forms import FootballTeamsForm, WelcomeForm
from . import simulator
import time
import random
# from teams import teams
from .actions import actions


# Create your views here.

def index(request):
    markets = Market.objects.all().order_by('position','-skills')

    return render(request, 'index.html', {'markets': markets})


def myteam(request):
    myteam = Myteam.objects.filter(pstatus='onstart').order_by('position','-skills')

    # statsint = myteam.skills

    myteamrez = Myteam.objects.filter(pstatus='reserve').order_by('position', '-skills')

    return render(request, 'myteam.html', {'myteam': myteam, 'myteamrez': myteamrez})


def lteam(request, id):

    lteam = Myteam.objects.filter(lteam_id=id)

    lteamn = League.objects.get(id=id)

    lmyteam = Myteam.objects.filter(pstatus='onstart', lteam_id=id).order_by('position','-skills')

    # statsint = myteam.skills

    lmyteamrez = Myteam.objects.filter(pstatus='reserve', lteam_id=id).order_by('position', '-skills')

    return render(request, 'lteams.html', {'lmyteam': lmyteam, 'lmyteamrez': lmyteamrez,'lteamn': lteamn })



def league(request):
    teams = League.objects.all().order_by('name')


    for team in teams:
        team.totalg = Myteam.objects.filter(lteam=team.id).aggregate(Sum('goals'))['goals__sum']
        team.save(update_fields=['totalg'])

    # tplayer.pstatus = 'reserve'
    #
    # tplayer.save(update_fields=['pstatus'])
    #

    # tgoals = Myteam.objects.get(lteam_id=teams[0].id).aggregate(Sum('goals'))['goals__sum']

    # tgoals = sum(goals)

    return render(request, 'league.html', {'teams': teams})



# @api_view(['GET'])
def buy(request, id):
    markets = Market.objects.all()
    myteam = Myteam.objects.all()

    marketp = Market.objects.get(id=id)

    marketp.delete()

    marketp.pk = None

    tplayer = Myteam()
    tplayer.name = marketp.name
    tplayer.position = marketp.position
    tplayer.age = marketp.age
    tplayer.experience = marketp.experience
    tplayer.skills = marketp.skills
    tplayer.date_buyed = timezone.now()

    tplayer.save()

    return render(request, 'myteam.html', {'myteam': myteam})


# @api_view(['GET'])
def sell(request, id):
    markets = Market.objects.all()
    myteam = Myteam.objects.all()

    tplayer = Myteam.objects.get(id=id)

    tplayer.delete()

    tplayer.pk = None

    marketp = Market()
    marketp.name = tplayer.name
    marketp.position = tplayer.position
    marketp.age = tplayer.age
    marketp.skills = tplayer.skills
    marketp.experience = tplayer.experience
    marketp.date_buyed = timezone.now()

    marketp.save()

    return render(request, 'index.html', {'markets': markets})


# @api_view(['GET'])
def reserve(request, id):
    myteam = Myteam.objects.all()

    tplayer = Myteam.objects.get(id=id)

    tplayer.pstatus = 'reserve'

    tplayer.save(update_fields=['pstatus'])

    teams = League.objects.all().order_by('name')

    tgoals = Myteam.objects.aggregate(Sum('goals'))['goals__sum']

    # tgoals = sum(goals)

    return render(request, 'league.html', {'teams': teams, 'tgoals': tgoals})

    # return HttpResponseRedirect('index')

# @api_view(['GET'])
def onstart(request, id):
    myteam = Myteam.objects.all()

    tplayer = Myteam.objects.get(id=id)

    tplayer.pstatus = 'onstart'

    tplayer.save(update_fields=['pstatus'])

    teams = League.objects.all().order_by('name')

    tgoals = Myteam.objects.aggregate(Sum('goals'))['goals__sum']

    # tgoals = sum(goals)

    return render(request, 'league.html', {'teams': teams, 'tgoals': tgoals})

    # return HttpResponseRedirect('index')


def match(request):
    teams = League.objects.all().order_by('name')


    for team in teams:
        team.totalg = Myteam.objects.filter(lteam=team.id).aggregate(Sum('goals'))['goals__sum']
        team.save(update_fields=['totalg'])

    # tplayer.pstatus = 'reserve'
    #
    # tplayer.save(update_fields=['pstatus'])
    #

    # tgoals = Myteam.objects.get(lteam_id=teams[0].id).aggregate(Sum('goals'))['goals__sum']

    # tgoals = sum(goals)

    return render(request, 'match.html', {'teams': teams})


# @api_view(['GET'])
def get_teams(request):
    '''
    view for the user input of two teams from specific years, when
    given a proper input it redirects to the results of the simulation
    '''
    if request.method == 'POST':
        form = FootballTeamsForm(request.POST)
        if form.is_valid(): #checks that a valid input has been given
            # year1 = form.cleaned_data['year_1']
            team1 = form.cleaned_data['team_1']
            print('team1: ', team1)

            # year2 = form.cleaned_data['year_2']
            team2 = form.cleaned_data['team_2']
            print('team2: ', team1)

            # t1 = Team(team_name=team1)
            t1 = Team(team_name=team1)
            t2 = Team(team_name=team2)
            t1.save()
            t2.save()

            print('t1: ', t1)

            print('t2: ',t2)

            #redirects to the simulate view, with parameters of the two teams
            return HttpResponseRedirect(reverse('transfer:simulate'))
    else:
        form = FootballTeamsForm()
    return render(request, 'teams.html', {'form': form})


appresult = []
tscore = []
tteam1 = []
tteam2 = []
comnt = []


# @api_view(['GET'])
def simulate(request):
    '''
    view for displaying the results of a given simulation
    '''
    #get team names and years
    teams = []
    team_names = []
    for t in Team.objects.all():
        team_names.append(t.team_name)
        teams.append(t.team_name)
        t.delete()
    print('teams: ', teams)    # teams: ['Barca', 'Chelsea']
    print('team_names[0]', team_names[0])    # Barca
    print('team_names[1]', team_names[1])    # Chelsea


    def generateRandomEvent(action):
        event = ''
        if action == 'attack':
            weights = [0.15, 0.05, 0.1, 0.2, 0.5]
            event = random.choice(random.choices(actions['attack'], weights))
        elif action == 'defense':
            weights = [0.2, 0.05, 0.15, 0.2, 0.2, 0.3]
            event = random.choice(random.choices(actions['defense'], weights))

        return event

    def generateAction():
        action = ''
        randomNumber = random.randint(1, 2)
        if randomNumber == 1:
            action = 'attack'
        elif randomNumber == 2:
            action = 'defense'

        return action

    def generateRandomTeam(team1, team2):
        randomTeam = random.randint(1, 2)
        if randomTeam == 1:
            team = team1
        else:
            team = team2

        return team



    def app():

        global appresult
        appresult.clear()

        global tteam1
        tteam1.clear()

        global comnt
        comnt.clear()

        team1 = team_names[0]

        tteam1.append(team1)
        print('team1: ', team1)

        global tteam2
        tteam2.clear()

        team2 = team_names[1]

        tteam2.append(team2)
        print('team2: ', team2)

        nteams = [team1, team2]
        if team1 == team2:
            team2 = random.choice(nteams)

        # if team1:
        #     return render(request, 'simulate.html')

        # player_team = input(f'Which team you choose? | {team1}, {team2}: ')
        player_team = random.choice(nteams)

        score = {team1: 0, team2: 0}

        if player_team == team1 or player_team == team2:

            score = {team1: 0, team2: 0}
            print(f'Match Start! {team1} vs {team2}')
            cmnt2 = 'Match Start!'
            comnt.append(cmnt2)


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

                    scomnt = ','.join(comnt)
                    astory = str(i) + '-min.    ' + team + ':   ' + event + '   ' + scomnt + '   ' + str(score)

                    comnt.clear()
                    # global appresult
                    appresult.append(astory)


                if event == "Foul":
                    possibilities = ['Red Card', 'Yellow Card', 'Free Kick', 'Penalty', '']
                    weights = [0.05, 0.3, 0.2, 0.05, 0.4]
                    event = random.choice(random.choices(possibilities, weights))
                    if event == '':
                        print('Referee starts game after foul')
                        cmnt2 = 'Referee starts game after foul'
                        comnt.clear()
                        comnt.append(cmnt2)
                    else:
                        print(f'Referee decide to: {event}')
                        cmnt2 = 'Referee decide to: Foul'
                        comnt.clear()
                        comnt.append(cmnt2)
                        # time.sleep(0.5)

                if event == "GOOAALL!":
                    score[team] = score[team] + 1
                    print(f'Score: {score}')
                    cmnt2 = 'GOOAALL!'
                    comnt.clear()
                    comnt.append(cmnt2)

                if event == "Free Kick":
                    randomNumber = random.randint(1, 10)
                    if randomNumber == 10:
                        score[team] = score[team] + 1
                        print('Co za piekna bramka z rzutu wolnego!')
                        print(f'Score: {score}')
                        cmnt2 = 'GOOAALL! Co za piekna bramka z rzutu wolnego!'
                        comnt.clear()
                        comnt.append(cmnt2)
                    else:
                        print('Niestety zmarnowali okazje na bramke z rzutu wolnego!')
                        cmnt2 = 'not goal! Niestety zmarnowali okazje na bramke z rzutu wolnego!'
                        comnt.clear()
                        comnt.append(cmnt2)

                if event == "Penalty":
                    sides = ['left', 'center', 'right']
                    if team == player_team:

                        # player_shoot = input('Where you want to shoot? (left, center, right) ')
                        player_shoot = random.choice(sides)

                        goalkeeper = random.choice(sides)
                        if player_shoot == goalkeeper:
                            print('Goalkeeper defends the penalty!!')
                            print(f'Goalkeeper go to: {goalkeeper}')
                            cmnt2 = 'not goal! Goalkeeper defends the penalty!!'
                            comnt.clear()
                            comnt.append(cmnt2)
                        else:
                            print('Goal!')
                            print(f'Goalkeeper go to: {goalkeeper}')
                            score[team] = score[team] + 1
                            print(f'Score: {score}')
                            cmnt2 = 'GOOAALL!'
                            comnt.clear()
                            comnt.append(cmnt2)
                    else:
                        playerGoalkeeper = random.choice(sides)
                        # playerGoalkeeper = input('Where you want to go with your goalkeeper? (left, center, right) ')

                        computerShoot = random.choice(sides)
                        if computerShoot == playerGoalkeeper:
                            print('Goalkeeper defends the penalty!!')
                            print(f'Shooter shoot to: {computerShoot}')
                            cmnt2 = 'not goal! Goalkeeper defends the penalty!!'
                            comnt.clear()
                            comnt.append(cmnt2)
                        else:
                            print('Goal!')
                            print(f'Shooter shoot to: {computerShoot}')
                            score[team] = score[team] + 1
                            print(f'Score: {score}')
                            cmnt2 = 'GOOAALL!'
                            comnt.clear()
                            comnt.append(cmnt2)

                if i == 45:
                    print('Перерыв!')
                    print(score)
                    cmnt2 = 'Перерыв!'
                    comnt.clear()
                    comnt.append(cmnt2)
                    # time.sleep(3)
                i += 1
            print(score)

            global tscore
            tscore.clear()

            tscore.append(score)
            print(appresult)


            return appresult, tscore, tteam1, tteam2

        else:
            print('You must enter the correct name of the team')
            return

    app()

    return render(request, 'simulate.html', {'appresult': appresult,
                                             'tscore': tscore,
                                             'tteam1': tteam1,
                                             'tteam2': tteam2})



# @api_view(['GET'])
def welcome(request):
    '''
    view for our welcome page
    '''
    if request.method == 'POST':
        form = WelcomeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('selection'))
        else:
            form = WelcomeForm()
    return render(request, 'welcome.html')


# @api_view(['GET'])
def split(roster):
    '''
    helper function for splitting roster dictionaries into lists of players
    '''
    qb = []
    wr = []
    rb = []
    k = []
    for position, players in roster.items():
        for key, player in players.items():
            if position == 'QB' and player != '':
                qb.append(player)
            elif position == 'WR' and player != '':
                wr.append(player)
            elif position == 'RB' and player != '':
                rb.append(player)
            elif position == 'K' and player != '':
                k.append(player)
    return (qb, wr, rb, k)
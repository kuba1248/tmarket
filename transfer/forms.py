from django import forms
from .models import Market, Myteam, League


# TEAMS = [('Browns', 'Browns'), ('Ravens', 'Ravens'), ('Packers', 'Packers'),
#          ('Vikings', 'Vikings'), ('Texans', 'Texans'), ('Chiefs', 'Chiefs'), ('Seahawks', 'Seahawks'),
#          ('Falcons', 'Falcons'), ('Bears', 'Bears'), ('Lions', 'Lions'), ('Chargers', 'Chargers'),
#          ('Bengals', 'Bengals'), ('Buccaneers', 'Buccaneers'), ('Saints', 'Saints'),
#          ('Steelers', 'Steelers'), ('Giants', 'Giants'), ('Redskins', 'Redskins'),
#          ('Eagles', 'Eagles'), ('Jets', 'Jets'), ('Bills', 'Bills'),
#          ('Dolphins', 'Dolphins'), ('Patriots', 'Patriots'), ('Colts', 'Colts'),
#          ('Jaguars', 'Jaguars'), ('Raiders', 'Raiders'), ('Panthers', 'Panthers'),
#          ('Cardinals', 'Cardinals'), ('49ers', '49ers'), ('Cowboys', 'Cowboys'), ('Rams', 'Rams'),
#          ('Titans', 'Titans'), ('Broncos', 'Broncos')]

TEAMS = League.objects.values_list('name', 'name')


class FootballTeamsForm(forms.Form):
    '''
    form for taking user input for two teams with team names and years
    '''
    team_1 = forms.ChoiceField(label="Choose Team 1 ", choices=TEAMS)

    team_2 = forms.ChoiceField(label="Choose Team 2 ", choices=TEAMS)


class WelcomeForm(forms.Form):
    '''
    form for a button that takes the user to the simulation page
    '''
    btn = forms.CharField()

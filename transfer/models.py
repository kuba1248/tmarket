from django.db import models


# Create your models here.
class League(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    totalg = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Market(models.Model):
    CATEGORIES = (
        ('legend', 'legend'),
        ('superstar', 'superstar'),
        ('young', 'young'),
        ('prof', 'prof'),
        ('quick', 'quick'),
        ('strong', 'strong')
    )

    pcategory = (
        ('fwd', 'fwd'),
        ('mfd', 'mfd'),
        ('def', 'def'),
        ('gk', 'gk')
    )

    #   💴💴   💶💶   💷💷    🔳
    #
    #   🟦🟦   🟩🟩    🟪🟪    🟫🟫      🟥🟥

    cskills = (
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦', '🟩🟩🟥🟥🟫🟫🟦🟦🟦'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦', '🟩🟩🟥🟥🟫🟫🟦🟦'),
        ('🟩🟩🟥🟥🟫🟫🟦', '🟩🟩🟥🟥🟫🟫🟦'),
        ('🟩🟩🟥🟥🟫🟫', '🟩🟩🟥🟥🟫🟫'),
        ('🟩🟩🟥🟥🟫', '🟩🟩🟥🟥🟫'),
        ('🟩🟩🟥🟥', '🟩🟩🟥🟥'),
        ('🟩🟩🟥', '🟩🟩🟥'),
        ('🟩🟩', '🟩🟩')
    )

    pstat = (
        ('reserve', 'reserve'),
        ('onstart', 'onstart')
    )

    name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=20,
        choices=pcategory
    )
    age = models.IntegerField()
    goals = models.IntegerField(default=0)
    pstatus = models.CharField(
        default='reserve',
        max_length=200,
        choices=pstat
    )
    experience = models.CharField(
        max_length=20,
        choices=CATEGORIES
    )
    skills = models.CharField(
        default='🟩🟩',
        max_length=200,
        choices=cskills
    )
    date_buyed = models.DateTimeField(auto_now_add=True, blank=True)
    lteam = models.ForeignKey(League, default=1, related_name='market', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position', '-skills', '-pstatus']

    def __str__(self):
        return self.lteam.name + '  -    ' + self.position + '      ' + self.name


class Myteam(models.Model):
    CATEGORIES = (
        ('legend', 'legend'),
        ('superstar', 'superstar'),
        ('young', 'young'),
        ('prof', 'prof'),
        ('quick', 'quick'),
        ('strong', 'strong')
    )

    pcategory = (
        ('fwd', 'fwd'),
        ('mfd', 'mfd'),
        ('def', 'def'),
        ('gk', 'gk')
    )

    #   💴💴   💶💶   💷💷    🔳
    #
    #   🟦🟦   🟩🟩    🟪🟪    🟫🟫      🟥🟥

    cskills = (
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦🟦', '🟩🟩🟥🟥🟫🟫🟦🟦🟦'),
        ('🟩🟩🟥🟥🟫🟫🟦🟦', '🟩🟩🟥🟥🟫🟫🟦🟦'),
        ('🟩🟩🟥🟥🟫🟫🟦', '🟩🟩🟥🟥🟫🟫🟦'),
        ('🟩🟩🟥🟥🟫🟫', '🟩🟩🟥🟥🟫🟫'),
        ('🟩🟩🟥🟥🟫', '🟩🟩🟥🟥🟫'),
        ('🟩🟩🟥🟥', '🟩🟩🟥🟥'),
        ('🟩🟩🟥', '🟩🟩🟥'),
        ('🟩🟩', '🟩🟩')
    )

    pstat = (
        ('reserve', 'reserve'),
        ('onstart', 'onstart')
    )

    name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=20,
        choices=pcategory
    )
    age = models.IntegerField()
    goals = models.IntegerField(default=0)
    pstatus = models.CharField(
        default='reserve',
        max_length=200,
        choices=pstat
    )
    experience = models.CharField(
        max_length=20,
        choices=CATEGORIES
    )
    skills = models.CharField(
        default='🟩🟩',
        max_length=200,
        choices=cskills
    )
    date_buyed = models.DateTimeField(auto_now_add=True, blank=True)
    lteam = models.ForeignKey(League, default=1, related_name='myteam', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position', '-skills', '-pstatus']

    def __str__(self):
        return self.lteam.name + '  -    ' + self.position + '      ' + self.name


class Team(models.Model):
    '''
    model for a team with team name and year
    '''
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name
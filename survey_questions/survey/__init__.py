from otree.api import *


doc = """
Survey questions in otree, including multiple choices (select one, select all that apply), questions with conditional logic, etc.
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # select one 
    favor_fruit = models.IntegerField(
        label='Selct your favorite fruit',
        choices=[
            [1,'Apple'],
            [2,'Banana'],
            [3,'Cherry'],
            [4,'Durian'],
        ],
        widget=widgets.RadioSelect,
    )
    # select all that apply
    favor_apple = models.BooleanField(
        label='Apple',
        widget=widgets.CheckboxInput,
        blank=True,
    )
    favor_banana = models.BooleanField(
        label='Banana',
        widget=widgets.CheckboxInput,
        blank=True,
    )
    favor_cherry = models.BooleanField(
        label='Cherry',
        widget=widgets.CheckboxInput,
        blank=True,
    )
    favor_durian = models.BooleanField(
        label='Durian',
        widget=widgets.CheckboxInput,
        blank=True,
    )
    # conditional logic
    tongue = models.IntegerField(
        label='What is your mother tongue?',
        choices=[
            [1,'Chinese'],
            [2,'English'],
            [3,'French'],
            [4,'Other']
        ],
        widget=widgets.RadioSelect,
    )
    tongue_other = models.StringField(
        label='Enter your mother tongue:',
        blank=True,
    )



# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['favor_fruit','favor_apple','favor_banana','favor_cherry','favor_durian','tongue','tongue_other']

    @staticmethod
    def error_message(player: Player, values):
        if values['favor_apple'] == False and values['favor_banana'] == False and values['favor_cherry'] == False and values['favor_durian'] == False:
            return 'At least select one!'
        if values['tongue'] == 4 and values['tongue_other'] == '':
            return 'Please enter your mother tongue!'

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage]

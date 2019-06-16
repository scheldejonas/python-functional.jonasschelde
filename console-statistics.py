import random

from options import DEFAULTS


dices = DEFAULTS['dices']

rounds_limit = 10000


def get_round_winner( dice_one, dice_two ):

    random_one = random.randint(0,5)

    random_two = random.randint(0,5)

    dice_one_value = dice_one[random_one]

    dice_two_value = dice_two[random_two]

    if ( dice_one_value > dice_two_value ):

        return 'one'

    else:

        return 'two'


def get_game_result( dice_one, dice_two ):

    i = 0

    dice_one_score = 0

    dice_two_score = 0

    while i < rounds_limit :

        winner = get_round_winner( dice_one, dice_two )

        if ( winner == 'one' ):

            dice_one_score += 1

        else :

            dice_two_score += 1

        i += 1

    return {
        'dice_one': dice_one_score,
        'dice_two': dice_two_score
    }


def simulate_choice_options( opponent_dice_color ):

    if ( opponent_dice_color == 'red' ):

        first_color = 'Red'
        first_dice = dices['red']

        second_color = 'Green'
        second_dice = dices['green']

        third_color = 'Blue'
        third_dice = dices['blue']

    elif ( opponent_dice_color == 'green' ):

        first_color = 'Green'
        first_dice = dices['green']

        second_color = 'Red'
        second_dice = dices['red']

        third_color = 'Blue'
        third_dice = dices['blue']

    else:

        first_color = 'Blue'
        first_dice = dices['blue']

        second_color = 'Green'
        second_dice = dices['green']

        third_color = 'Red'
        third_dice = dices['red']


    first_dice_vs_second_dice = get_game_result( first_dice, second_dice )
    print( first_color + ' vs ' + second_color )
    print( first_dice_vs_second_dice )

    first_dice_vs_third_dice = get_game_result( first_dice, third_dice )
    print( first_color + ' vs ' + third_color )
    print( first_dice_vs_third_dice )

    chose_opponent = ''

    if ( first_dice_vs_third_dice['dice_two'] > first_dice_vs_second_dice['dice_two']):
        chose_opponent = second_color
    else:
        chose_opponent = third_color

    print('If ' + first_color + ' is the opponent, biggest looser is: ' + chose_opponent)


simulate_choice_options('red')

simulate_choice_options('green')

simulate_choice_options('blue')
import json

import random

from flask import (Flask,
                   render_template,
                   request,
                   flash,
                   make_response,
                   redirect,
                   url_for)

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'esauhou>UO>au.sh35@<Uouo52%@#ouo.42!@#42'


rounds_limit = 1000

game_result = []

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('app_data'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():

    flash("Amazing, You choose to join the party!")

    return render_template('index.html',saves=get_saved_data())


@app.route('/the-game')
def the_game():

    return render_template(
        'the-game.html',
        saves = get_saved_data(),
        result=game_result,
        options = DEFAULTS
    )


@app.route('/save', methods=['POST'])
def save():

    flash("Amazing, We have saved your choice!")

    response = make_response(redirect(url_for('the_game')))

    data = get_saved_data()

    data.update(dict(request.form.items()))

    response.set_cookie('app_data', json.dumps(data))

    return response


@app.route('/play', methods=['POST'])
def play():

    # Prepare - arguments for the game
    dices = DEFAULTS['dices']
    print( dices )

    name = request.form.get('name')
    print( name )

    round_count = request.form.get('round_count')
    print( round_count )

    global rounds_limit
    rounds_limit = int(round_count)

    dice_choice = request.form.get('colors')
    print( dice_choice )

    if ( dice_choice ):
        dice = dices[dice_choice]
        print(dice)

        # Simulate game
        global game_result

        game_result = simulate_choice_options(dice_choice)


    # Respond
    response = make_response(redirect(url_for('the_game')))

    data = get_saved_data()
    print( data )

    data.update(dict(request.form.items()))

    response.set_cookie('app_data', json.dumps(data))

    return response


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

    global rounds_limit

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

    result = ''

    dices = DEFAULTS['dices']

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

    first_dice_vs_third_dice = get_game_result( first_dice, third_dice )

    chose_opponent = ''

    if ( first_dice_vs_third_dice['dice_two'] > first_dice_vs_second_dice['dice_two']):
        chose_opponent = second_color
    else:
        chose_opponent = third_color

    return {
        'first_color': first_color,
        'second_color': second_color,
        'third_color': third_color,
        'first_dice_vs_second_dice': first_dice_vs_second_dice,
        'first_dice_vs_third_dice': first_dice_vs_third_dice,
        'chose_opponent': chose_opponent,
    }


if __name__ == '__main__':
    app.run()

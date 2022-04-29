import datetime
import json
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except LookupError:
        flash("Sorry, this email cannot be found")
        return render_template('index.html'), 404
    else:
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):

    try:
        found_club = [c for c in clubs if c['name'] == club][0]
        found_competition = [c for c in competitions if c['name'] == competition][0]
        if found_club and found_competition:
            competition_date = datetime.datetime.strptime(found_competition['date'], "%Y-%m-%d %H:%M:%S")
            today = datetime.datetime.now()
            if today > competition_date:
                flash('Sorry, this competition has already taken place. Please choose another one')
                return render_template('welcome.html', club=found_club, competitions=competitions), 400
            else:
                return render_template('booking.html', club=found_club, competition=found_competition)
    except IndexError:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions), 400


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    points_required = places_required * 3
    if places_required > 12 or places_required <= 0:
        flash('You can reserve 1 minimum and 12 maximum places')
        return render_template('booking.html', club=club, competition=competition), 400
    elif places_required > int(competition['numberOfPlaces']):
        flash(f'there are only {competition["numberOfPlaces"]} places left in this competition')
        return render_template('booking.html', club=club, competition=competition)
    elif points_required > int(club["points"]):
        flash("Sorry, you need more points")
        return render_template('booking.html', club=club, competition=competition)
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-places_required
        club["points"] = int(club["points"]) - points_required
        flash('Great-booking complete!', f' {competition["name"]} reserved places: {places_required} - ')
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/clubsPoints')
def display_clubs_points():
    return render_template('clubs.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

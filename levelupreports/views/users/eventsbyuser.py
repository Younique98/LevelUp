"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Event
from levelupreports.views.connection import Connection


def userevent_list(request):
    """Function to build an HTML report of events by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all events, with related user info.
            db_cursor.execute("""
                SELECT
                    e.id,
                    e.date,
                    e.time,
                    e.game_id,
                    e.description,
                    e.organizer_id,
                    g.name
        
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_game g ON e.game_id = g.id
                JOIN
                    levelupapi_gamer gr ON gr.user_id = e.organizer_id
            """)

            dataset = db_cursor.fetchall()

            # Take the flat data from the database, and build the
            # following data structure for each gamer.
            #
            # {
            #     1: {
            #         "gamer_id": 1,
            #         "full_name": "Molly Ringwald",
            #         "events": [
            #             {
            #                 "id": 5,
            #                 "date": "2020-12-23",
            #                 "time": "19:00",
            #                 "game_name": "Fortress America"
            #             }
            #         ]
            #     }
            # }

            events_by_user = {}

            for row in dataset:
                # Crete a event instance and set its properties
                event = Event()
                event.name = row["name"]
                event.description = row["description"]
                event.date = row["date"]
                event.game_id = row["game_id"]
                event.organizer_id = row["organizer_id"]
                event.time = row["time"]

                # Store the user's id
                uid = row["organizer_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current event to the `events` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["id"] = uid
                    events_by_user[uid]["date"] = row["date"]
                    events_by_user[uid]["time"] = row["time"]
                    events_by_user[uid]["name"] = row["name"]
                    events_by_user[uid]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_users_with_events = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/list_with_events.html'
        context = {
            'userevent_list': list_of_users_with_events
        }

        return render(request, template, context)

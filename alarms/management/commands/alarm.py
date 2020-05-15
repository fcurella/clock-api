import djclick as click

from alarms.models import Alarm


@click.command()
@click.argument("time")
@click.argument("timezone")
def add_alarm(time, timezone):
    hours, minutes = map(int, time.split(":"))
    schedule = f"{minutes} {hours} * * *"

    Alarm.objects.create(
        schedule=schedule, timezone=timezone, active=True,
    )

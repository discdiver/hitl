import datetime
from prefect import flow, pause_flow_run


@flow(log_prints=True)
def get_date():
    date_to_meet = pause_flow_run(
        wait_for_input=datetime.date,
    )
    print(f"Let's meet on {date_to_meet}!")


if __name__ == "__main__":
    get_date()

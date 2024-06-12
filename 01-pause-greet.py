from prefect import flow, pause_flow_run


@flow(log_prints=True)
def greet_user():
    user = pause_flow_run(
        wait_for_input=str,
    )  # timeout=10)
    print(f"Hello, {user}!")


if __name__ == "__main__":
    greet_user()

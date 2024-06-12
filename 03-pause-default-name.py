import asyncio
from prefect import flow, pause_flow_run
from prefect.input import RunInput
dateteim

class UserNameInput(RunInput):
    name: str
    date: 


@flow(log_prints=True)
async def greet_user():
    user_input = await pause_flow_run(
        wait_for_input=UserNameInput.with_initial_data(
            description="Your first name, given at birth, please.", name="anonymous"
        )
    )

    if user_input.name == "anonymous":
        print("Hello, stranger!")
    else:
        print(f"Hello, {user_input.name}!")


if __name__ == "__main__":
    print("hi")
    asyncio.run(greet_user())
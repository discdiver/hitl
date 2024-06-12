from typing import Literal
import pydantic
from prefect import flow, pause_flow_run
from prefect.input import RunInput


class ShirtOrder(RunInput):
    size: Literal["small", "medium", "large", "xlarge"]
    color: Literal["red", "green", "black"]
    quantity: int

    @pydantic.validator("color")
    def validate_order(cls, value, values, **kwargs):
        if value == "green" and values["size"] == "small":
            raise ValueError("Green is only in-stock for medium, large, and XL sizes.")


@flow(log_prints=True)
def get_shirt_order():
    pause_flow_run(wait_for_input=ShirtOrder)


if __name__ == "__main__":
    get_shirt_order()
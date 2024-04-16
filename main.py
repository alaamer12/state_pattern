from enum import Enum


class OrderState(Enum):
    Cancelled = 0
    Draft = 1
    Confirmed = 2
    Processed = 3
    Shipped = 4
    Delivered = 5
    Returned = 6


class Order:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def set_state(self, new_state):
        if (self.status == OrderState.Draft and new_state != OrderState.Confirmed) \
                or (
                self.status == OrderState.Confirmed and new_state not in [OrderState.Cancelled, OrderState.Delivered]) \
                or (self.status == OrderState.Processed and new_state != OrderState.Shipped) \
                or (self.status == OrderState.Shipped and new_state != OrderState.Delivered) \
                or (self.status == OrderState.Delivered and new_state != OrderState.Returned):
            raise Exception("Invalid order state transition.")
        else:
            self.status = new_state


# Example usage
order = Order(1, OrderState.Draft)
print(order.status)  # Output: OrderState.Draft
order.set_state(OrderState.Confirmed)
print(order.status)  # Output: OrderState.Confirmed

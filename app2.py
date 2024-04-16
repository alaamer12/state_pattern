# Define the states
class TrafficLightState:
    def change(self, traffic_light):
        pass

    def __str__(self):
        pass

class GreenState(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = YellowState()

    def __str__(self):
        return "Green"

class YellowState(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = RedState()

    def __str__(self):
        return "Yellow"

class RedState(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = GreenState()

    def __str__(self):
        return "Red"

# Define the context
class TrafficLight:
    def __init__(self):
        self.state = GreenState()

    def change(self):
        self.state.change(self)

    def __str__(self):
        return f"Traffic light is {self.state}"

# Example usage
if __name__ == "__main__":
    traffic_light = TrafficLight()
    print(traffic_light)  # Output: Traffic light is Green

    traffic_light.change()
    print(traffic_light)  # Output: Traffic light is Yellow

    traffic_light.change()
    print(traffic_light)  # Output: Traffic light is Red

    traffic_light.change()
    print(traffic_light)  # Output: Traffic light is Green


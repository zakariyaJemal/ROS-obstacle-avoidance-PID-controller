import time

class PID:

    def __init__(self, Kp, Ki, Kd):

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.prev_error = 0.0
        self.integral = 0.0
        self.last_time = time.time()

    def compute(self, setpoint, measured):

        error = setpoint - measured

        now = time.time()
        dt = now - self.last_time

        if dt <= 0:
            dt = 0.01

        self.integral += error * dt
        derivative = (error - self.prev_error) / dt

        output = (
            self.Kp * error +
            self.Ki * self.integral +
            self.Kd * derivative
        )

        self.prev_error = error
        self.last_time = now

        return output

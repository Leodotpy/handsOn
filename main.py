import Physics.Math as m
import time

gravity = m.Vector3(0, -9.8, 0)

running = True

lastTime = time.time()
while running:
    # Calculate delta time in seconds
    currentTime = time.time()
    deltaTime = lastTime - currentTime
    lastTime = currentTime


import pybullet as p
import pybullet_data
import time

# Start the PyBullet physics engine in GUI mode
physicsClient = p.connect(p.GUI)

# Set the path to PyBullet's data to load models
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity for the simulation (9.8 m/s^2 along the Z-axis)
p.setGravity(0, 0, -9.8)

# Load a plane to serve as the ground
planeId = p.loadURDF("plane.urdf")

# Load the 6-DOF robotic arm model into the simulation
robotic_arm = p.loadURDF("kuka_iiwa/model.urdf", [0, 0, 0], useFixedBase=True)

# Run the simulation for 10 seconds
for i in range(1000):
    # Step through the simulation
    p.stepSimulation()
    
    # Add a time delay for realistic movement
    time.sleep(1.0 / 240.0)

# Disconnect from the simulation
p.disconnect()

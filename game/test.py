import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down City Traffic Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Road and grid settings
ROAD_WIDTH = 100
INTERSECTION_SIZE = 100
GRID_SIZE = 200

# Vehicle settings
VEHICLE_SIZE = 50
VEHICLE_SPEED = 2

# Clock
clock = pygame.time.Clock()

# Vehicle class
class Vehicle:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = random.choice([RED, GREEN, BLUE])

    def move(self):
        if self.direction == "right":
            self.x += VEHICLE_SPEED
        elif self.direction == "left":
            self.x -= VEHICLE_SPEED
        elif self.direction == "down":
            self.y += VEHICLE_SPEED
        elif self.direction == "up":
            self.y -= VEHICLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, VEHICLE_SIZE, VEHICLE_SIZE))

# Function to draw the city grid
def draw_city():
    # Draw horizontal roads
    for i in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.rect(screen, GRAY, (0, i + (GRID_SIZE - ROAD_WIDTH) // 2, WIDTH, ROAD_WIDTH))

    # Draw vertical roads
    for i in range(0, WIDTH, GRID_SIZE):
        pygame.draw.rect(screen, GRAY, (i + (GRID_SIZE - ROAD_WIDTH) // 2, 0, ROAD_WIDTH, HEIGHT))

    # Draw intersections
    for i in range(0, WIDTH, GRID_SIZE):
        for j in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.rect(screen, BLACK, (i + (GRID_SIZE - INTERSECTION_SIZE) // 2, j + (GRID_SIZE - INTERSECTION_SIZE) // 2, INTERSECTION_SIZE, INTERSECTION_SIZE))

# Function to spawn vehicles
def spawn_vehicles():
    vehicles = []
    for i in range(0, WIDTH, GRID_SIZE):
        vehicles.append(Vehicle(i + (GRID_SIZE - VEHICLE_SIZE) // 2, 0, "down"))
        vehicles.append(Vehicle(i + (GRID_SIZE - VEHICLE_SIZE) // 2, HEIGHT - VEHICLE_SIZE, "up"))
    for j in range(0, HEIGHT, GRID_SIZE):
        vehicles.append(Vehicle(0, j + (GRID_SIZE - VEHICLE_SIZE) // 2, "right"))
        vehicles.append(Vehicle(WIDTH - VEHICLE_SIZE, j + (GRID_SIZE - VEHICLE_SIZE) // 2, "left"))
    return vehicles

# Main function
def main():
    vehicles = spawn_vehicles()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw the city
        draw_city()

        # Move and draw vehicles
        for vehicle in vehicles:
            vehicle.move()
            vehicle.draw()

            # Reset vehicle position if it goes off-screen
            if vehicle.x > WIDTH or vehicle.x < -VEHICLE_SIZE or vehicle.y > HEIGHT or vehicle.y < -VEHICLE_SIZE:
                vehicles.remove(vehicle)
                vehicles.append(Vehicle(random.choice([0, WIDTH - VEHICLE_SIZE]), random.choice([0, HEIGHT - VEHICLE_SIZE]), random.choice(["right", "left", "up", "down"])))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
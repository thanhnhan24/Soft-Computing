import pygame
import math

def draw_neural_net(screen, input_nodes, hidden_nodes, output_nodes):
    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (200, 200, 200)
    red = (255, 0, 0)

    # Screen dimensions
    width, height = screen.get_size()

    # Node radius
    radius = 15

    # Spacing between layers
    layer_spacing = width // 4

    # Vertical spacing between nodes
    def get_layer_y_positions(num_nodes):
        if num_nodes == 1:
            return [height // 2]
        spacing = height // (num_nodes + 1)
        return [spacing * (i + 1) for i in range(num_nodes)]

    # Input layer positions
    input_x = layer_spacing // 2
    input_y_positions = get_layer_y_positions(input_nodes)

    # Hidden layer positions
    hidden_x = input_x + layer_spacing
    hidden_y_positions = get_layer_y_positions(hidden_nodes)

    # Output layer positions
    output_x = hidden_x + layer_spacing
    output_y_positions = get_layer_y_positions(output_nodes)

    # Draw connections
    for i, y1 in enumerate(input_y_positions):
        for j, y2 in enumerate(hidden_y_positions):
            pygame.draw.line(screen, gray, (input_x, y1), (hidden_x, y2), 1)

    for i, y1 in enumerate(hidden_y_positions):
        for j, y2 in enumerate(output_y_positions):
            pygame.draw.line(screen, gray, (hidden_x, y1), (output_x, y2), 1)

    # Draw input nodes
    for y in input_y_positions:
        pygame.draw.circle(screen, black, (input_x, y), radius, 2)

    # Draw hidden nodes
    for y in hidden_y_positions:
        pygame.draw.circle(screen, black, (hidden_x, y), radius, 2)

    # Draw output nodes
    for y in output_y_positions:
        pygame.draw.circle(screen, black, (output_x, y), radius, 2)

def main():
    pygame.init()

    # Screen dimensions
    screen_width, screen_height = 900, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Neural Network Visualization")

    # Define the number of nodes in each layer
    input_nodes = 3
    hidden_nodes = 5
    output_nodes = 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the background with white

        # Draw the neural network
        draw_neural_net(screen, input_nodes, hidden_nodes, output_nodes)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

# Main Game Script

from cli import CLI

if __name__ == "__main__":
	game = CLI(elapsed_time = 0.1, monte_carlo = False)
	game.run()

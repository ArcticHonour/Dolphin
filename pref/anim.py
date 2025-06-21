import sys
import time

def loading_animation(duration):
    """
    Displays a rotating loading animation in the console.

    Args:
        duration (int): The duration for the animation in seconds.
    """
    animation = "|/-\\"
    end_time = time.time() + duration
    idx = 0

    while time.time() < end_time:
        # Print the current animation character and flush output
        sys.stdout.write(f"\rLoading {animation[idx % len(animation)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1

    sys.stdout.write("\rLoading complete!   \n")

# Call the function for a 5-second animation
loading_animation(5)

import turtle  # Import the turtle module to create graphics

# Ask the user for background color, and validate the input
bg_color = input("Enter a background color (e.g., black, white, blue): ").strip().lower()
if bg_color not in ['black', 'white', 'blue', 'yellow', 'pink', 'orange']:
    print("Invalid color entered! Defaulting to black.")
    bg_color = 'black'

turtle.bgcolor(bg_color)  # Set the background color based on user input

# Define the sizes and colors lists
sizes = [4, 10, 5, 19, 20]  # List of sizes for circle patterns
colors = ['white', 'yellow', 'blue', 'orange', 'pink']  # List of colors for the patterns

# Function to draw concentric circles with decreasing sizes
def drawCircles(turt, size, sub):
    """
    Draws 10 concentric circles, reducing the size by 'sub' with each iteration.
    """
    for i in range(10):  # Loop 10 times
        turt.circle(size)  # Draw a circle with the current size
        size -= sub  # Decrease the size for the next circle

# Function to draw the complete circular pattern
def drawSpecial(turt, size, repeat, sub):
    """
    Draws multiple patterns of concentric circles, rotating by an angle after each.
    """
    for i in range(repeat):  # Repeat the pattern specified number of times
        drawCircles(turt, size, sub)  # Call the drawCircles function
        turt.right(360 / repeat)  # Rotate the turtle to create the pattern

# Create a turtle object
myTurtle = turtle.Turtle()
myTurtle.speed(0)  # Set drawing speed to the maximum

# Main drawing loop
for i in range(len(sizes)):  # Loop through the sizes and colors
    myTurtle.color(colors[i])  # Set the turtle's color
    drawSpecial(myTurtle, 100, 10, sizes[i])  # Call drawSpecial with the current size

# Let the user close the turtle graphics window manually
turtle.done()

from turtle import Turtle, Screen  #imports Turtle, screen from turtke module
import random
WIDTH = 400  ## defining dimensions of the screen
HEIGHT = 400

def no_of_turtle():  # This generates number of turtles the user wants in the race.
    count = 0
    while True:
        count = input("How many turtles do you want to participate (2 - 10): ")
        if count.isdigit():
            count = int(count)
            if 2 <= count <= 10: # Make sures there is a competition for 2 or more turtle
                return count
            else:
                print("Input is not in the given range. Please try again.")
        else:
            print("Please enter a digit between 2 - 10.")
turtles = no_of_turtle()

print("Number of turtles: ", turtles)

color_list = ["red", "blue", "pink","orange", "black", "purple", "green", "indigo", "violet", "grey" ]
X_SPACING = WIDTH//(turtles + 1)  ## Calculates spacing between turtles and divides the screen
s2 = Screen()
s2.setup(WIDTH, HEIGHT)  ## Setting up screen
turtle_list = []
for i in range(1, turtles+1):

    tom = Turtle()
    tom.shape("turtle")
    tom.left(90)
    
    tom.color(color_list[i-1])
    tom.penup()
    tom.goto(-WIDTH//2 + (i * X_SPACING) , -HEIGHT//2 + 10)  ## This code places the turtle in its starting position
    turtle_list.append(tom)  ### Adding each turtle to the list to start a race
def start():
    is_race_on = True
    while is_race_on:
        for t in turtle_list:
            distance = random.randrange(1,20)  ## Generating a number for the turtle to move forward
            t.forward(distance)  ## Turtle move forward
            x, y = t.pos()  ## This checks current position of the turtle
            if y >= HEIGHT//2:  ### Keeping a finish line
                print("The winner is ",t.pencolor(), "turtle")
                is_race_on = False  ## Ending race when we reached finish line
                
start()  ## Starts the turtle race


s2.exitonclick()   ### Game exits when we click on the screen

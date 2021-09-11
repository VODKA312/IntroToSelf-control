## PARAGRAPH_PRE_TUTRLE
### course name : intro to self-control
#### courses come from https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd0013
#### describe: my notes is prepare for people who have owned basic python programming skills.so  I will use more general way to organize this knowledge in my markdown notes.

#### As for beginner(like freshmen or even more young),I suggest you to watch some channels in coursera([Coursera | Online Courses & Credentials From Top Educators. Join for Free](https://www.coursera.org/)). If you are not really better in English,I recommend you to learn basic python knowledge in [Python教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400/)

#### This module will show you how to program in a  interactive way,take it easy,it's just a small test.

***

### Variable

- a connection between a name in the code and some data in the computer's memory.

| express        | meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| turtle.Turle() | create a turtle(obj)                                         |
| George         | create a variable,and give this turtle name(George).you can consider George as its data,and turtle's name is its meaning. |
| =              | to tell the computer that a particular data(obj) should have a particular name tag(George) |
- **Why  we use a variable to store turtle 's name?**

  Once the turtle data object(we create as turtle. Turtle()) has been placed in memory and given a name,we can use that name whenever we want to do something with the turtle. 

  for example,if we want the turtle(or George turtle)to go forward to run or turn.

  we can use such lines like that...

  ```python
  geroge.forward(100)
  ```

  or

  ```py
  geoge.right(90)
  ```

### Modules

modules

- If you want to use some specific methods in some specific modules(like math,turtle and so on),you should import it in the python code,like this.

  ```python
  import turtle
  ```

- **NOTICE**

  you can't import modules you hadn't download before(except some built-in modules,like math)

  you can use `pip` to download some specific modules.

### methods in turtle modules

methods

- if you have been imported modules in python,you can use these methods to programming.

  | methods               | meaning                                             |
  | --------------------- | --------------------------------------------------- |
  | amy.color("yellow")   | * my understand is use yellow pencil to draw.       |
  | amy = turtle.Turtle() | create a turtle object,and give its name tag as amy |
  | amy.forward(100)      | let amy to go forward,distance is 100.              |
  | amy.right(90)         | let amy go right in 90 angle.                       |
  | amy.penup()           | means you end use you pencil                        |
  | amy.pendown()         | means you start use you pencil                      |

### Practice1: draw a square

- **SOLUTION**

  ```python
  import turtle
  amy = turtle.Turtle()
  amy.color("yellow")
  amy.forward(100)
  amy.right(90)
  amy.forward(100)
  amy.right(90)
  amy.forward(100)
  amy.right(90)
  amy.forward(100)
  ```

  *we can use a more simple way to solve this problem,let me tell you how to use `circulation` next time.

### Comments

we can use comments to ....(do anything,by the way,I want to tell you that I really hate someone who write suck comments.)

### For Loop

- the aim to use circulation is avoid the same lines over and over again.

- As for square practice,we can use for loop to simple its code

  ```python
  for side in [1,2,3,4]:
      amy.forward(100)
      amy.right(90)
  ```

- **NOTICE**

  we use `indent` to start a circulation structure

  the count in lists is the circulation's time. You can even use["a","b","c","d"].

  my suggest is you should give this circulation list its specific meaning. You can understand [1,2,3,4]as one time,two times,three times,four times....

- **use variable in circulation list**

  you can create a variable to store a circulation list,like this

  ```python
  import turtle
  amy = turtle.Turtle()
  amy.color("cyan")
  
  some_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  
  for item in some_list:
      amy.forward(50)
      amy.right(30)
  ```

- **What is the length variable in for loop?**

  Remember that the loop will run once each of the items in the list.

  each time the loop run,it will take one of the items in the lists and assign the item to the length variable.

  for example:

  ```python
  for length in [10, 20, 30, 40, 50, 60]:
      dizzy.forward(length)
      dizzy.right(90)
  ```

  for the first time,the length is 10.

  for the second time,the length variable is assigned as 20.

  ***In my understand,length is a circulation variable.**

### Nested Loop

...... (next time to say. I'm so tired)

### Practice in circulation variable

- AIM: draw three different  color's arrow

  ![](C:\Users\15356\Desktop\red-orange-yellow-lines.png)

- SOLUTION

  ```python
  import turtle
  amy = turtle.Turtle()
  amy.width(5)
  # Move back without drawing anything
  amy.penup()
  amy.back(140)
  amy.pendown()
  for prettycolor in ["red","yellow","blue"]:
      amy.color(prettycolor)
      amy.forward(100)
      if prettycolor != "blue":
          amy.penup() #expect blue to control the white area
          amy.forward(50)
      amy.pendown()
  ```

### Practice in nesting loop

- **AIM:** draw three different color's square

- **SOLUTION:**

  ```python
  import turtle
  # create a turtle obj
  amy = turtle.Turtle()
  amy.width(5)
  # Move back without drawing anything
  amy.penup()
  amy.back(250)
  amy.pendown()
  # for loop start
  for pretty_color in ["red", "yellow", "blue"]:
      amy.color(pretty_color)
      # nesting loop start
      sides = [1, 2, 3, 4]
      for side in sides:
          amy.forward(100)
          amy.right(90)
      # nesting loop end
      amy.penup()
      amy.forward(200)
      amy.pendown()
  # for loop end
  ```

### Consider some wrong in programming

- **grammatical mistakes**

  use correct grammar in programming is essential important.

  like you say "hello" to Germen,and say "guten tag" to French.

  Spelling correct is also essential. You can check it in your IDE(I use pycharm)

- **logical mistakes**

  you should practice day-to-day,to consider your logic is confirmed computer's logic. 

- **indent mistakes**

  you should notice it. Because python use indent to start a loop or end a loop. Some programming language will use()

### Practice: Draw a rainbow

if we want to draw a real rainbow,we should use RGB color and circle methods.

the Udacity website provide rainbow as a hexagon. Use a simple nesting loop.

you can create a rainbow for your own.

### REVIEW

you should review these knowledge

- how to call a method?

- what decide cycle times in specific for loop?

  **answer:** number of cycle variable in lists

- What is `nameError`

  you use this variable before you assign it

- How to read Errors in python compelling consequence?

  - type of error: like `nameError`
  - what program file the error occurred in 
## PARAGRAPH_PRE_Basic python programming
### course name : intro to self-control
#### courses come from https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd0013
#### describe: my notes is prepare for people who have owned basic python programming skills.so  I will use more general way to organize this knowledge in my markdown notes.

#### As for beginner(like freshmen or even more young),I suggest you to watch some channels in coursera([Coursera | Online Courses & Credentials From Top Educators. Join for Free](https://www.coursera.org/)). If you are not really better in English,I recommend you to learn basic python knowledge in [Python教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400/)

#### This module will show you how to program in a  interactive way,take it easy,it's just a small test.

***

### LESSON1:intro to this module

#### INTRO

.... python NB!

#### WARNING: THREE ESSENTIAL POINTS IN PYTHON PROGRAMMING

- python is case sensitive

  is different with SQL

- **spacing is important in python**

- Use error message to help you learn how to write code

#### OVERVIEW

- **lesson1:**  intro
- **lesson2:**  data types and operators
- **lesson3:**  control flow
- **lesson4:**  function definition,variable scope and so on.
- **lesson5:**  scripting

### LESSON2: data types and operators

#### calculating operator

*operator use to calculate.

#### variable 

- left is variable,right is the value

- like:

  ```python
  my_population = 74
  ```

  but this value not equal to this variable(my population)

- use **routine alphabet,digit,and underline** to name variable

- WARNING: avoid to use keywords in python

  | False  | class    | finally | is       | return |
  | ------ | -------- | ------- | -------- | ------ |
  | None   | continue | for     | lambda   | try    |
  | True   | def      | from    | nonlocal | while  |
  | and    | del      | global  | not      | with   |
  | as     | elif     | if      | or       | yield  |
  | assert | else     | import  | pass     |        |
  | break  | except   | in      | raise    |        |

- we recommend use lowercase to name variable,like "snake case"

  ```python
  my_height = 58 #recommend
  MYLONG = 40 #hum....
  MyLat = 105 #all right
  ```

#### assigning operator

like `+=` and so on......

#### int and float
- use correct type to express variable
- like use int to express count for people,or obj,use float to express others
- division by zero?
- will happen `ZeroDivisionError `mistake

#### Boolean,logical,comparing operator
hold on,it's too easy.

#### string

hold on,it's too easy.

- use \ to divide ' ' in string

- len(string) 

- (string * n)

- string[0]

- **function in string**

  you can find many function in python website...
  
  [Built-in Types — Python 3.9.7 documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)

#### Basic Data Structure in python

If you want to use python more fluently,I recommend you to practice in these websites....

HackerRank:

[Python If-Else | HackerRank](https://www.hackerrank.com/challenges/py-if-else/problem)

Codewars:

[Sign in | Codewars](https://www.codewars.com/users/sign_in)

URL:[总结 (kjdfe.github.io)](https://kjdfe.github.io/ljl.github.io/无人驾驶入门/Part 03-Module 01-Lesson 02_数据类型与运算符/37. 总结.html)

| data structure | ordered | mutable | constructor   | Example                                  |
| -------------- | ------- | ------- | ------------- | ---------------------------------------- |
| int            | NA      | NA      | int()         | 5                                        |
| float          | NA      | NA      | float()       | 6.5                                      |
| string         |         |         |               |                                          |
| bool           |         |         |               |                                          |
| list           | Yes     | Yes     | [] or list()  | [5, 'yes', 5.7]                          |
| tuple          | Yes     | No      | () or tuple() | (5, 'yes', 5.7)           or 5,'yes',5.7 |
| set            | No      | Yes     |               |                                          |
| dictionary     |         |         |               |                                          |

#### TYPE & Type Conversion

- use type() function,you can judge the type of variable

#### Lists and Membership Operator

- lists
- splicing

#### List Methods

| method         | input                                                        | output                         |
| -------------- | ------------------------------------------------------------ | ------------------------------ |
| len()          | [1,2,3,4]                                                    | 4                              |
| max()          | digit: return maximum                [1,2,3,4]                                        string: return sort end in the alphabet | maximum                        |
| min()          | opposite of the max()                                        | minimum                        |
| sorted()       | [1,3,2,4]                                                    | [1,2,3,4]                      |
| "\".join(list) | ["fore", "aft", "starboard", "port"]                         | fore        aft starboard port |
| list.append()  | [a,b,c,d].append('z')                                        | [a,b,c,d,e]                    |
| n in list      | print("a" in list)                                           | True                           |

#### Tuple

- tuple is **ordered** and **immutable**

  like that

  ```python
  location = (13.4125, 103.866667)
  print("Latitude:", location[0])
  print("Longitude:", location[1])
  ```

- tuple can use dimensions to give variables values

  like that

  ```python
  dimensions = 52, 40, 100
  length, width, height = dimensions
  print("The dimensions are {} x {} x {}".format(length, width, height))
  ```

  or you can use

  ```python
  length, width, height = 52, 40, 100
  print("The dimensions are {} x {} x {}".format(length, width, height))
  ```

#### Set

- set contains unique elements,it's disordered but mutable

  like that

  ```python
  numbers = [1, 2, 6, 3, 1, 1, 6]
  unique_nums = set(numbers)
  print(unique_nums)
  ### output: {1,2,3,6}
  ```

- methods in set

- as same as methods in list ,we use `in` to judge if this element contains in this set

- add: add an element

- remove: *remove an random element

> *set in python is similar in math. You can use union, intersection ,difference* methods. it's quicker than other containers.

#### Dictionaries And Identify Operators

- constructing way

  ```python
  elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
  ```

- add element and assignment

  add:

  ```python
  elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
  ```

- search elements in dictionary

  if you use `in` methods return T/F

  if you use `get` methods return N/Y

  *seems like LEITS test

- **identify operators in dictionary**

- you can `is` or `is not` to judge if it exists. Then it will return True/False

  *may be you can use it in your LEITS test

-  **== is equal to is**

  ```python
  a = [1, 2, 3]
  b = a
  c = [1, 2, 3]
  
  print(a == b)
  print(a is b)
  print(a == c)
  print(a is c)
  # it will return T,T,T,F
  ```

#### Compound data structure

If you want to add some elements,you can use the methods `add` in dictionary

such as 

```python
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
```

#### Different use ways in Lists,dictionaries,sets

[练习：复合数据结构 (kjdfe.github.io)](https://kjdfe.github.io/ljl.github.io/无人驾驶入门/Part 03-Module 01-Lesson 02_数据类型与运算符/34. 练习：复合数据结构.html)

- For list
  - index start with 0
  - can sort
  - can use .append to add element
- For set
  - mutable
  - use .add to add element
  - disordered
- For dictionaries
  - can be compound
  - disordered
  - contains two parts (like dictionary people use)

### Lesson 3: control flow




So the first thing I want to talk about is dictionaries in Python.
Now,dictionaries in Python work kind of similarly to dictionaries in real life,
right? So if you were to look up a word in the dictionary say the word code, then you might find the definition as something as the lines of program instructions for the computer. And dictionaries are reallyuseful because they allow us to group together and tag related pieces of information.

The way I like to think about dictionaries is in the form of a table.
Every dictionary has two parts to it. On the left hand side is the key, and that is the equivalent of the word in the dictionary,and then it's also got an associated value. That would be the equivalent of the actual definition of the word.

Bug ->  An error in a program that prevents the program from running as expected,
Function-> A Peiece of Code that you can call over and over again
Loop-> The action of doing something over and over again

Now let's say that we took this variation simple table of definitions of programming words that we've come across so far and we go ahead and we try to convert it right into a dictionary, how would we do that? 

The first thing we want to do is we want them to create a dictionary. And to do that in Python, this is what the syntax looks like. We have a set of curly braces and everything that's inside
the curly brace is the content of our dictionary.
{<Key1>:<Value1>,
 <Key2 :<Value2>>,
 <Key3>:<Value3>}

The key goes first followed by a colon and then followed by the value. In our table we've got this word bug, which is the first key, so we can replace that over here in our dictionary. And the value that's associated with this key is the definition for a bug.

{"Bug":"An error in a program that prevents the program from running as expected",
 "Function":"A Peiece of Code that you can call over and over again",
 "Loop":"The action of doing something over and over again"}

that becomes the value and can be replaced here after the colon.

So now, we've created an actual dictionary using Python code.

What if you wanted to have more than one entry in your dictionary? Well,

you would separate each of the key value pairs using a comma,

and then you can continue adding key and value pairs until you get to the end of

your dictionary. 


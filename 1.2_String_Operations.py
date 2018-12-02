
# coding: utf-8

#  <a href="http://cocl.us/topNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 
# 

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>String Operations </font></h1>

# <br>

# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref0">Strings</a></li>
# <li><a href="#ref1">Indexing</a></li>
# <li><a href="#ref2">Escape Sequences </a></li>
# <li><a href="#ref3">String Operations</a></li>
# <li><a href="#ref4">Quizz </a></li>
# <br>
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

# <a id="ref0"></a>
# <h2 align=center>Strings </h2>

#  A string is contained within 2 quotes:

# In[ ]:

"Michael Jackson"


# You can also use single  quotes:

# In[ ]:

'Michael Jackson'


# A string can be spaces and digits: 

# In[ ]:

'1 2 3 4 5 6 '


# A string can also be special characters : 

# In[ ]:

'@#2_#]&*^%$'


# We can print our string using the print statement:

# In[ ]:

print("hello!")


# We can bind or assign a string to another variable:
# 

# In[ ]:

Name= "Michael Jackson"
Name


#  <a id="ref1"></a>
# <h2 align=center>Indexing </h2>

# It is helpful to think of a string as an ordered sequence. Each element in the sequence can be accessed using an index represented by the array of numbers:  

#  <img src = "https://ibm.box.com/shared/static/esdu9w118rm1aldff7ff8c9b3kpjdazc.png" width = 600, align = "center"></a>

#  The first index can be accessed as follows:

# In[ ]:

print(Name[13])


#  We can access index 6:

# In[ ]:

print(Name[6])


# Moreover, we can access the 13th index:

# In[ ]:

print(Name[13])


#  We can also use negative indexing with strings:

# <img src = "https://ibm.box.com/shared/static/rmq8akevtt6uufox3xai7q2kqs4j9kan.png" width = 600, align = "center"></a>

#  The last element is given by the  index -1: 

# In[ ]:

print(Name[-1])


#  The first element can be obtained by  index -15:

# In[ ]:

print(Name[-15])


#  We can find the number of characters in a string by using 'len', short for length:

# In[ ]:

len("Michael Jackson")


# We can obtain multiple characters from a string using slicing, we can obtain the 0 to 4th and 8th to the 12th element:  

#  <img src="https://ibm.box.com/shared/static/bva43bmp00cxeunqh4w7blkgniycbign.png" width=600,align="center"></a>
# 
# 

# In[ ]:

Name[0:4]


# In[ ]:

Name[8:12]


#  We can also  input a stride value as follows, with the '2' indicating that we are selecting every second variable:

#  <img src="https://ibm.box.com/shared/static/f49xvym409rxclhtbr30xrs9kc4l5419.png" width=600,align="center"></a>
# 
# 

# In[ ]:

Name[::2]


# We can also incorporate slicing  with the stride. In this case, we select the first five elements and then use the stride: 

# In[ ]:

Name[0:5:2]


# In[ ]:




# We can concatenate or combine strings by using the addition symbols, and the result is a new string that is a combination of both:
# 

# In[ ]:

Statement = Name + "is the best"
Statement


#  To replicate values of a string we simply multiply the string by the number of times we would like to replicate it. In this case, the number is three. The result is a new string, and this new string consists of three copies of the original string:
# 

# In[ ]:

3*"Michael Jackson "


# You can create a new string by setting it to the original variable. Concatenated  with a new string, the result is a new string that changes from Michael Jackson to “Michael Jackson is the best".
# 

# In[ ]:

Name= "Michael Jackson"
Name= Name+" is the best"
Name


#  <a id="ref2"></a>
# <h2 align=center>Escape Sequences  </h2>

# Back slashes represent the beginning  of escape sequences. Escape sequences represent strings that may be difficult to input. For example, back slash "n" represents a new line. The output is given by a new line after the back slash "n” is encountered:
# 

# In[ ]:

print(" Michael Jackson \n is the best" )


# Similarly, back slash  "t" represents a tab: 

# In[ ]:

print(" Michael Jackson \t is the best" )


#  If you want to place a back slash in your string, use a double back slash:

# In[ ]:

print(" Michael Jackson \\ is the best" )


#  We can also place an "r" before the string to display the backslash:

# In[ ]:

print(r" Michael Jackson \ is the best" )


# <a id="ref3"></a>
# <h2 align=center>String Operations</h2>

# There are many string operation methods in Python that can be used to manipulate the data. We are going to use some basic string operations on the data. 
# 
# 

# Let's try with the method "upper"; this method converts upper case characters to lower case characters:

# In[ ]:

A="Thriller is the sixth studio album"
print("before upper:",A)
B=A.upper()
print("After upper:",B)


# <br>

# The method replaces a segment of the string, i.e. a substring  with a new string. We input the part of the string we would like to change. The second argument is what we would like to exchange the segment with, and the result is a new string with the segment changed: 
# 

# In[ ]:

A="Michael Jackson is the best"
B=A.replace('Michael', 'Janet')
B


# The method "find" finds a sub-string. The argument is the substring you would like to find, and the output is the first index of the sequence. We can find the sub-string "jack" or "el".  
# 

#  <img src="https://ibm.box.com/shared/static/mc414goh1l8jfo9gb19yibuylk8zk7dh.png" width=600,align="center"></a>

# In[ ]:

Name="Michael Jackson"
Name.find('el')


# In[ ]:

Name.find('Jack')


# If the  sub-string is not in the string then the output is a negative one. For example, the string 'Jasdfasdasdf' is not a substring:

# In[ ]:

Name.find('Jasdfasdasdf')


#  <a id="ref4"></a>
# <h2 align=center> Quiz on Strings </h2>

# ##### What is the value of the variable "A" after the following code is executed? 
# A="1"

# In[ ]:




#  <div align="right">
# <a href="#String1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String1" class="collapse">
# ```
# "1"
# ```
# </div>
# 

# #### What is the value of the variable "B" after the following code is executed?
# `B="2"`

# In[ ]:




# <div align="right">
# <a href="#String2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String2" class="collapse">
# ```
# "2"
# ```
# </div>

# #### What is the value of the variable "C" after the following code is executed?
# `C=A+B`

# In[ ]:




#  <div align="right">
# <a href="#String3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String3" class="collapse">
# ```
# "12"
# ```
# </div>

# #### Consider the variable "D": use slicing to print out the first three elements: 
# 

# In[ ]:

D="ABCDEFG"


# In[ ]:




#  <div align="right">
# <a href="#String4" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String4" class="collapse">
# ```
# "print(D[:3]) or print(D[0:3])"
# ```
# </div>

# #### Use a stride value of 2 to print out every second character  of the string "E": 

# In[ ]:

E='clocrkr1e1c1t'


# In[ ]:




# <div align="right">
# <a href="#String6" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String6" class="collapse">
# ```
# "print(E[::2])"
# ```
# </div>

# #### Print out a backslash:

# In[ ]:




# <div align="right">
# <a href="#String7" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String7" class="collapse">
# ```
# print(" \\" )
# or
# print(r" \ " )
# ```
# </div>

# #### Convert the variable "F" to uppercase:

# In[ ]:

F="You are wrong"


# In[ ]:




#  <div align="right">
# <a href="#String8" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String8" class="collapse">
# ```
# F.upper()
# ```
# </div>

# #### Consider the variable "G", and find the first index of the sub-string 'snow':

# In[ ]:

G="Mary had a little lamb Little lamb, little lamb Mary had a little lamb Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"


# In[ ]:




#  <div align="right">
# <a href="#String9" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String9" class="collapse">
# ```
# G.find('snow')
# ```
# </div>

# #### In the variable "G", replace the sub-string Mary with "Bob":

# In[ ]:




#  <div align="right">
# <a href="#String10" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String10" class="collapse">
# ```
# G.replace("Mary","Bob")
# ```
# </div>

#  <a href="http://cocl.us/bottemNotebooksPython101Coursera"><img src = "https://ibm.box.com/shared/static/irypdxea2q4th88zu1o1tsd06dya10go.png" width = 750, align = "center"></a>

# # About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 

# In[ ]:




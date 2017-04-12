#A program to determine your reading speed
#This program is a precursor for a future program to investigate a correlation
#between reading speed and book format
#Python3 syntax used

#declare variables
introduction = " "
book_format = " "
book_name = " "
pages_read = 0.0
reading_time = 0.0

#get input
introduction = input("Hello! Please answer the following \
questions to the best of your ability. (Press enter to continue)")

book_format = input("What format is the book you're reading?")

book_name = input("Which book have you just read?")

pages_read = float(input("How many pages did you read?"))

reading_time = float(input("How long did you read?"))

#do processing
rs = pages_read / reading_time

#display output
print (introduction)
print (("Format:"),(book_format))
print (("Book Title:"),(book_name))
print (("Reading Speed ="),format(rs,'.2f'),("pgs/min"))

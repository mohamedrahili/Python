book_id = 12345   
book_title = "Python Programming and Application"  
publish_year = 2020  
print("Book ID: " + str(book_id))

current_year = 2024  
year_difference = current_year - publish_year
print("The book was published " + str(year_difference) + " years ago.")

print(book_title + " is a great book!")

print("First six characters: " + book_title[:6])

if 2010 < publish_year:
    print("2010 is earlier than the publication year.")
elif 2010 == publish_year:
    print("2010 is the same as the publication year.")
else:
    print("2010 is later than the publication year.")

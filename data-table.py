#going to try and seperate the data into mutiple tables to make it easier to analyze becuase it is so large 
#will do one table where review is the primary key- bc products can have multiple reviews 

amazon_reviews = [] #creates empty list 

with open('amazon-meta.txt') as file:
    product = {} #to store the information about each product
    reviewID = 1 #unique ID for each review becuase the table will be organized with each review as the primary key
    for line in file: 
        line = line.rstrip()
        #in the dataset there is a new product every time there is a line skipped, so if the information 
        #is not a blank line, than it is data 
        if not line.strip():
            #store the information for each product together
            product = {}
            elif line.startswith(' '):
                #handle 


#in the text file 
    #for every row 
        #if the row is blank 
            #create new item(each item is an individual review)
            #for each review 
                #unique review ID 
                #product information 
                #review information 

#going to try and seperate the data into mutiple tables to make it easier to analyze becuase it is so large 
#will do one table where review is the primary key- bc products can have multiple reviews 

amazon_reviews = [] #creates empty list 

with open('amazon-meta.txt') as file:
   # product = {} #to store the information about each product
    reviewID = 1 #unique ID for each review becuase the table will be organized with each review as the primary key
    for line in file: 
        line = line.rstrip() #removes trailing whitespace so we can tell if the line is empty or not 
        #in the dataset there is a new product every time there is a line skipped, so if the information is not a blank line, than it is data 
        if not line.strip(): #if this line has only whitespace- indicates that we are starting a new product 
            #create new review and store the product information for it 
          #  product = {}
            #decided to only include products that have reviews because we are interested in a product's reviews
            if 'reviews' in product: 
                if line.startswith('reviews'):
                    reviewOverview = line.strip().split() #sections each review(each line) into its parts(date, cust ID, rating etc)
                for eachReview in 'reviews':
                    singleReview = line.strip().split()
                #**QUESTION-the 'similar product ASIN' one should return a list of ASINs, does the code for this need to change bc its a list instead of a product?                      
                    #dont know to get the date bc its not labeled
                    amazon_reviews.append({'reviewID':reviewID, 'productID':product.get('Id'), 'productASIN':product.get('ASIN'), 'productTitle':product.get('title'), 'productGroup':product.get('group'), 'similarProductsASIN':product.get('similar'), 'numReviews':reviewOverview.get('total'), 'productAvgRating':reviewOverview.get('avg rating'), 'customerID':singleReview.get(cutomer), 'rating':singleReview.get('rating'), 'helpful':singleReview.get(helpful)})
                    reviewID += 1



#in the text file 
    #for every row 
        #if the row is blank 
            #create new item(each item is an individual review)
            #for each review 
                #unique review ID and review information
                #product information 
                #review information 
            

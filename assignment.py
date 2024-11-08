reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
def keyword_highligter(review):
   keywords = [ "good", "excellent", "bad", "poor","average"]
   highlighted_reviews = []
   for review in reviews:
    for keyword in keywords:
        if keyword in review:
         review = review.replace(keyword, keyword.upper())
         highlighted_reviews.append(review)        
   return highlighted_reviews
   
   
highlighted_reviews= keyword_highligter(reviews)
for review in highlighted_reviews:
    print(review)



def sentiment_tally():
   positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
   negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
   positive = len(positive_words)
   negative = len(negative_words)
   print(f"The total number of positive reviews is {positive}") 
   print(f"The total number of negative reviews is {negative}")

sentiment_tally()

def review_summary(review, length=30):
   if len(review) <= length:
      return review
   end = review.rfind(" ", 0, length)
   if end == -1:
      end = length
   return review[:end] + '...'

print("Review Summaries:")
for review in reviews:
   print(review_summary(review))


def username_check(name, length = 2):
   if len(name) <= length:
      return "Invalid name must be more than two characters"
   else :
      return True


while True:
    name = input("What do you want your username to be ")
    username = name
    check_username = username_check(name)
    if check_username == True:
        print (f"Your username is {username}")
        break
    else:
       print("Your username is too short Try again must be longer than 2 characters")
   
   

   


    


    
    





    
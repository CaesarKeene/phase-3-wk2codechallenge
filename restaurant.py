class Restaurant:
    
    all_restaurants = []

    def __init__(self, name):        
        self.name = name    
        self.reviews = []     
        Restaurant.all_restaurants.append(self)

    def average_star_rating(self):       
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews) if len(self.reviews) > 0 else "No ratings yet"
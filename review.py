class Review:
    # The list to store all the reviews
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        # The customer who wrote the review
        self.customer = customer
        # The restaurant which is being reviewed
        self.restaurant = restaurant
        # The rating given in the review
        self.rating = rating
        
        # Add this review to the customer's list of reviews
        self.customer.reviews.append(self)
        # Add this review to the restaurant's list of reviews
        self.restaurant.reviews.append(self)
        # Add this review to the list of all reviews
        Review.all_reviews.append(self)

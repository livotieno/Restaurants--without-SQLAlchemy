from customer import Customer
from restaurant import Restaurant
from review import Review

def main():
    
    customer1 = Customer("Samuel", "Otieno")
    customer2 = Customer("Bruce", "Keith")

    restaurant1 = Restaurant("Krusty Crub")
    restaurant2 = Restaurant("Plaktons")

    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant2, 5)

    
    print(customer1.full_name()) 
    print(restaurant2.average_star_rating())  
    print(customer2.num_reviews())  

if __name__ == '__main__':
    main()
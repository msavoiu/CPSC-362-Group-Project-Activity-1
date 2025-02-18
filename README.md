# CPSC-362-Group-Project-Activity-1

## Product vision
Vital is a online fashion brand for the everyday consumer. For those who aren’t willing to spend the heavy costs that come with the latest fashions and trends, Vital offers timeless basics which can be mixed and matched to elevate any closet. Unlike competitors like Uniqlo, Vital offers more competitive pricing for our apparel. Consumers can enjoy regular deals and sales on products use the same high-quality materials as these other brands.

## Requirements

### User requirements
#### Use case:
**ID**: Shop username and password

**Name**: Shopping for basics

**Description**: Shoppers have a selection of a variety of minimal, simple clothing including shirts, pants, jackets, and accessories to shop from to fit their style

**Primary Actor:** Casual clothing consumers

**Preconditions**: Shoppers taken to the front page of the store

**Postconditions**: Shoppers have a timeless, elevated closet

**Main success scenario**: 
1. Shoppers sign into their account or can use a guest account to purchase.
2. Front page displays different articles of clothing to choose from and allows users to sort by category.
3. Shoppers choose from a category they want to buy from.
4. Shoppers can select different sizes and colors tailored to their preferences.
5. Shoppers add the item to their shopping cart.
6. Shoppers input their payment information and shipping method, then purchase.

### Functional requirements
__Checkout__
* Secure checkout system that shows order summary and allows user to see total cost and place order

| Story Card    |           |
| -------------     |:---------:|
| Story ID: |1|
| Story Name: | Checkout Page|
| User: |  Actor   |
| Story Description: |A secure checkout system that shows the users order summary and allows them to see the total cost of their items as well as place the order. |


__Cart__
* Live updating cart that reflects number of items the user has added and shows summary of items / price of all items in cart combined


| Story Card    |           |
| ------------- |:---------:|
| Story ID:    |2|
| Story Name:      | Cart |
|User:         | Actor   |
| Story Description:     | A live updating cart that reflects the number of items the user has added and shows the summary of the items as well as the total price. |


__Inventory Information__
* Up-to-date inventory information for all offered products, this includes color and size availability 

| Story Card    |           |
| ------------- |:---------:|
| Story ID:    |3|
| Story Name:      | Inventory |
|User:         | Actor   |
| Story Description:     | An inventory system that shows availability of colors and sizes for different products. |


__Account information for tracking orders__

__Categorization by clothing type / style__


| ID: | xxx |
| ------------- |:-------------:|
| Name: | View and track purchases |
| Description: | Customer accesses their account page and is able to view orders placed. They can select an individual order to check its details and shipping status. |
| Primary Actor: | Customer |
| Preconditions: | Customer is logged into the system |
| Postconditions: | Customer is updated on their orders' shipping statuses |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks account icon from any page on the website.<br>2. System displays account dashboard listing all orders placed by the customer.<br>3. Customer selects a specific order to view it in more detail.<br>4. System displays selected order's information: date placed, total, payment method, and items purchased.<br>5. Student clicks the "Track" button.<br>6. System displays shipment tracking information from the carrier. |


| ID:  | xxx |
| ------------- |:-------------:|
| Name:      | Apparel type/style categories     |
| Description:      | Customer can view various clothing types and styles through a dropdown-style navigation bar at the top of each page on the website, and select specific categories to view their catalogs. |
| Primary Actor:      | Customer     |
| Preconditions: | Customer has accessed the website |
| Postconditions: | Customer has viewed specific Vital products they are interested in |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer hovers over the "Apparel" section of the navigation bar. <br> 2. System displays in a dropdown menu idsplaying the different types (e.g. tops, pants, denim, accessories) and styles (e.g. casual, business-casual, athleisure) of clothing Vital sells. <br> 3. Customer selects a specific category to view. <br> 4. System displays the category's corresponding catalog, from which customers can select specific items to view in more detail. |



### Non-functional requirements
- Desktop and mobile-friendly UI
- Clothing models with body measurements for customer reference 
- Encryption of sensitive customer data
- Secure payment processing (through a third-party service like Stripe)
- Convenient checkout options (Paypal, Apple Pay, etc.)
  
![Diagramming](https://github.com/msavoiu/CPSC-362-Group-Project-Activity-1/blob/09ccb42f5b07b26ddc2258c5af26541856db8f3b/fds.drawio.png)

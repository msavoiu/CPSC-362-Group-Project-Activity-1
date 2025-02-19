# Vital

## Product vision
Vital is a online fashion brand for the everyday consumer. For those who aren’t willing to spend the heavy costs that come with the latest fashions and trends, Vital offers timeless basics which can be mixed and matched to elevate any closet. Unlike competitors like Uniqlo, Vital offers more competitive pricing for our apparel. Consumers can enjoy regular deals and sales on products use the same high-quality materials as these other brands.

## Requirements

### User requirements
- Website has core product viewing, add-to-cart, and checkout functionalities
- Customers create accounts to keep track of items in their cart, view previous orders, and track shipments
- Convenient options for payment are provided for customers

### Functional requirements
| ID:  | FR001 |
| ------------- |:-------------:|
| Name:      | Checkout page |
| Description:      | Customers use a secure checkout system to send payments and place orders |
| Primary Actor:      | Customer     |
| Preconditions: | Customer has added at least one item to cart |
| Postconditions: | Customer has successfully placed an order which will be sent to and fulfilled by Vital |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer navigates to their cart and confirms the contents. <br> 2. Customer clicks "Checkout". <br> 3. System displays a summary of the items in their cart and input fields for shipping address, billing address, and payment method.. <br> 4. Customer completes the required fields and clicks "Place Order". <br> 5. System receives the order and updates a database for employees to receive and begin fulfilling it. |

| ID:  | FR002 |
| ------------- |:-------------:|
| Name:      | Cart |
| Description:      | Customer can see what they've currently selected to purchase via live updating cart that reflects the number of items the user has added. It shows the summary of the items as well as the total price. |
| Primary Actor:      | Customer     |
| Preconditions: | Customer has logged in and and clicked "Add to Cart" on at least one item |
| Postconditions: | Customer is aware of what items will be included in their order and can proceed to checkout |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks on the cart icon above the navigation bar. <br> 2. If the system cannot find a valid session token, customer is redirected to the login page to log in first. <br> 3. System displays a list of the items currently in the cart with size, color/pattern, quantity, and price. |

| ID:  | FR003 |
| ------------- |:-------------:|
| Name:      | Store inventory |
| Description:      | An inventory system that keeps track of availability of colors/patterns and sizes for different products. |
| Primary Actor:      | Employee |
| Preconditions: | Inventory database has been updated by an employee who has manually audited product stock |
| Postconditions: | Customer-facing website has up-to-date information on the amount of certain products available |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Employee connects to Vital's database via a command-line tool like Postgres or ORM (e.g. Prisma). <br> 2. When queried, system displays a list of the items currently in stock. <br> 3. Employee adds/modifies entries to reflect changes in real-life inventory. <br> 4. Customer-facing website is automatically updated when inventory data is fetched from the database upon visit. |

| ID:  | FR004 |
| ------------- |:-------------:|
| Name:      | Login page |
| Description:      | Page with a form that accepts a username and password to authenticate a login attempt |
| Primary Actor:      | Customer |
| Preconditions: | Customer has an active account |
| Postconditions: | Customer has been logged in and issued the necessary authentication tokens |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer fills input fields with their email and password. <br> 2. System uses the supplied credentials to query a user database for matching credentials. <br> 4. If credentials are validated, the client is issued an authentication token for the session. The customer is then redirected back to the home page. <br> 5. If credentials are invalid, the system displays: "Email and/or password is incorrect." |

| ID:  | FR005 |
| ------------- |:-------------:|
| Name:      | Register page |
| Description:      | Page with a form that accepts a username and password to register a new account with |
| Primary Actor:      | Customer |
| Preconditions: | Customer can navigate to the website |
| Postconditions: | Customer has an active Vital account and can log in to it |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer fills input fields with their email and password. <br> 2. System uses the supplied credentials to query a user database to check if the email is already in use. <br> 3. If the email is already in use, the system displays: "Email is already in use." <br> 4. If the email is available, a new entry in the user database is created with the customer's credentials. <br> 5. Client is issued an authentication token for their session. <br> 6. Customer is redirected to their account dashboard. |

| ID:  | FR007 |
| ------------- |:-------------:|
| Name:      | Search for products on the website |
| Description:  | A search functionality that user can search for product with keywords |
| Primary Actor:      | Customer |
| Preconditions: | Products are added to the inventory |
| Postconditions: | Customer is viewing products they're interested in purchasing |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks the search button from the navigation bar. <br> 2. Customer searches for products they're interested in by providing keywords <br> 3. System displays products tagged with at least one of the provided keywords. |

| ID: | FR008 |
| ------------- |:-------------:|
| Name: | View and track purchases |
| Description: | Customer accesses their account page and is able to view orders placed. They can select an individual order to check its details and shipping status. |
| Primary Actor: | Customer |
| Preconditions: | Customer is logged into the system |
| Postconditions: | Customer is updated on their orders' shipping statuses |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks account icon from any page on the website.<br>2. System displays account dashboard listing all orders placed by the customer.<br>3. Customer selects a specific order to view it in more detail.<br>4. System displays selected order's information: date placed, total, payment method, and items purchased.<br>5. Student clicks the "Track" button.<br>6. System displays shipment tracking information from the carrier. |


| ID:  | FR009 |
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

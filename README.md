# Vital

## Product vision
Vital is a online fashion brand for the everyday consumer. For those who aren’t willing to spend the heavy costs that come with the latest fashions and trends, Vital offers timeless basics which can be mixed and matched to elevate any closet. Unlike competitors like Uniqlo, Vital offers more competitive pricing for our apparel. Consumers can enjoy regular deals and sales on products use the same high-quality materials as these other brands.

## Requirements

### User requirements
- Website has core product viewing, add-to-cart, and checkout functionalities
- Customers create accounts to keep track of items in their cart, view previous orders, and track shipments
- Convenient options for payment are provided for customers
- Customers can visit the website from both their computers/laptops and smartphones

### Functional requirements
| ID:  | FR001 |
| ------------- |:-------------:|
| Name:      | Home page |
| Description: | Customer is brought to the main page of the website |
| Primary Actor: | Customer |
| Preconditions: | Customer has pointed browser to https://vital.com |
| Postconditions: | Customer can view the homepage |
| Main Success Scenario: | 1. Customer navigates to the website URL. <br> 2. System displays all the components of the homepage.  |

| ID:  | FR002 |
| ------------- |:-------------:|
| Name:      | Search for products on the website |
| Description:  | A search functionality that user can search for product with keywords |
| Primary Actor:      | Customer |
| Preconditions: | Products are added to the inventory |
| Postconditions: | Customer is viewing products they're interested in purchasing |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks the search button from the navigation bar. <br> 2. Customer searches for products they're interested in by providing keywords <br> 3. System displays products tagged with at least one of the provided keywords. |

| ID:  | FR003 |
| ------------- |:-------------:|
| Name:      | Apparel type/style categories     |
| Description:      | Customer can view various clothing types and styles through a dropdown-style navigation bar at the top of each page on the website, and select specific categories to view their catalogs. |
| Primary Actor:      | Customer     |
| Preconditions: | Customer has accessed the website |
| Postconditions: | Customer has viewed specific Vital products they are interested in |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer hovers over the "Apparel" section of the navigation bar. <br> 2. System displays in a dropdown menu idsplaying the different types (e.g. tops, pants, denim, accessories) and styles (e.g. casual, business-casual, athleisure) of clothing Vital sells. <br> 3. Customer selects a specific category to view. <br> 4. System displays the category's corresponding catalog, from which customers can select specific items to view in more detail. |

| ID:  | FR004 |
| ------------- |:-------------:|
| Name:      | Product page |
| Description: | Displays relevant information regarding the product selected (colors/patterns, sizes, availability, model photos) |
| Primary Actor: | Customer has selected a specific product |
| Preconditions: | Customer has added at least one item to cart |
| Postconditions: | Customer is able to view details about the product and add it to cart |
| Main Success Scenario: | 1. Customer clicks on a specific product. <br> 2. System displays the relevant information, grabbing inventory status from the inventory database. |

| ID:  | FR005 |
| ------------- |:-------------:|
| Name:      | Cart |
| Description:      | Customer can see what they've currently selected to purchase via live updating cart that reflects the number of items the user has added. It shows the summary of the items as well as the total price. |
| Primary Actor:      | Customer     |
| Preconditions: | Customer has logged in and and clicked "Add to Cart" on at least one item |
| Postconditions: | Customer is aware of what items will be included in their order and can proceed to checkout |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks on the cart icon above the navigation bar. <br> 2. If the system cannot find a valid session token, customer is redirected to the login page to log in first. <br> 3. System displays a list of the items currently in the cart with size, color/pattern, quantity, and price. |

| ID:  | FR006 |
| ------------- |:-------------:|
| Name:      | Checkout page |
| Description:      | Customers use a secure checkout system to send payments and place orders |
| Primary Actor:      | Customer     |
| Preconditions: | Customer has added at least one item to cart |
| Postconditions: | Customer has successfully placed an order which will be sent to and fulfilled by Vital |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer navigates to their cart and confirms the contents. <br> 2. Customer clicks "Checkout". <br> 3. System displays a summary of the items in their cart and input fields for shipping address, billing address, and payment method.. <br> 4. Customer completes the required fields and clicks "Place Order". <br> 5. System receives the order and updates a database for employees to receive and begin fulfilling it. |

| ID:  | FR007 |
| ------------- |:-------------:|
| Name:      | Login page |
| Description:      | Page with a form that accepts a username and password to authenticate a login attempt |
| Primary Actor:      | Customer |
| Preconditions: | Customer has an active account |
| Postconditions: | Customer has been logged in and issued the necessary authentication tokens |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer fills input fields with their email and password. <br> 2. System uses the supplied credentials to query a user database for matching credentials. <br> 4. If credentials are validated, the client is issued an authentication token for the session. The customer is then redirected back to the home page. <br> 5. If credentials are invalid, the system displays: "Email and/or password is incorrect." |

| ID:  | FR008 |
| ------------- |:-------------:|
| Name:      | Register page |
| Description:      | Page with a form that accepts a username and password to register a new account with |
| Primary Actor:      | Customer |
| Preconditions: | Customer can navigate to the website |
| Postconditions: | Customer has an active Vital account and can log in to it |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer fills input fields with their email and password. <br> 2. System uses the supplied credentials to query a user database to check if the email is already in use. <br> 3. If the email is already in use, the system displays: "Email is already in use." <br> 4. If the email is available, a new entry in the user database is created with the customer's credentials. <br> 5. Client is issued an authentication token for their session. <br> 6. Customer is redirected to their account dashboard. |

| ID: | FR009 |
| ------------- |:-------------:|
| Name: | View and track purchases |
| Description: | Customer accesses their account page and is able to view orders placed. They can select an individual order to check its details and shipping status. |
| Primary Actor: | Customer |
| Preconditions: | Customer is logged into the system |
| Postconditions: | Customer is updated on their orders' shipping statuses |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks account icon from any page on the website.<br>2. System displays account dashboard listing all orders placed by the customer.<br>3. Customer selects a specific order to view it in more detail.<br>4. System displays selected order's information: date placed, total, payment method, and items purchased.<br>5. Student clicks the "Track" button.<br>6. System displays shipment tracking information from the carrier. |

| ID:  | FR010 |
| ------------- |:-------------:|
| Name:      | Secure payment processing |
| Description:      | Orders placed by customers are handled by a third-party financial service like Stripe. |
| Primary Actor:      | System  |
| Preconditions: | Customer has placed an order |
| Postconditions: | Customer's order has been securely processed and confirmed |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer clicks "Place order" to send their order to the system. <br> 2. System sends requests to the payment API to process the order. <br> 3. API responds back indicating whether the payment was successful or not. <br> 4. System displays the appropriate response message for the customer, either indicating that the payment was successful or prompting them to try again/try a different payment method, etc. |

| ID:  | FR011 |
| ------------- |:-------------:|
| Name:      | Store Inventory |
| Description:      | An inventory system that keeps track of availability of colors/patterns and sizes for different products. |
| Primary Actor:      | Employee |
| Preconditions: | Inventory database has been updated by an employee who has manually audited product stock |
| Postconditions: | Customer-facing website has up-to-date information on the amount of certain products available |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Employee connects to Vital's database via a command-line tool like Postgres or ORM (e.g. Prisma). <br> 2. When queried, system displays a list of the items currently in stock. <br> 3. Employee adds/modifies entries to reflect changes in real-life inventory. <br> 4. Customer-facing website is automatically updated when inventory data is fetched from the database upon visit. |

### Non-functional requirements
| ID:  | NFR001 |
| ------------- |:-------------:|
| Name:      | Desktop and mobile-friendly UI |
| Description:  | Customers can visit the website on a variety of devices and be presented with a visually appealing, easy to navigate interface every time. |
| Primary Actor: | Customer |
| Preconditions: | Customer has navigated to the website on their device of choice |
| Postconditions: | Customer is able to browse and perform necessary actions on the website |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer navigates to the Vital website. <br> 2. System sends the necessary data for rendering the application depending on what kind of device they're using. <br> 4. System displays the frontend for customer to interact with. |

| ID:  | NFR002 |
| ------------- |:-------------:|
| Name:      | Encryption of sensitive customer data |
| Description:  | Customers' data is encrypted to prevent data exfiltration that may be attempted by cyber attackers. API requests/responses are also sent over HTTPS. |
| Primary Actor: | System |
| Preconditions: | Customer has provided data to the system |
| Postconditions: | Customer data is stored securely |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Database server is configured to encrypt and decrypt data with a specific key/password. <br> 2. System provides the server with the key after confirming a customer's login is authenticated to fetch their data. <br> 4. System displays customer's data. |

| ID:  | NFR003 |
| ------------- |:-------------:|
| Name:      | Convenient checkout options |
| Description:  | Customer has a choice between regular credit card checkout and additional methods like Paypal, Apple Pay etc., adding flexibility to the software. |
| Primary Actor: | Customer |
| Preconditions: | Customer has added at least one item to cart |
| Postconditions: | Customer has placed an order with the Customer has placed an order with the payment method of their choice |
| Main Success Scenario:<br><br>(Normal Flow) | 1. Customer selects their preferred payment method. <br> 2. Customer fills out the necessary fields/completes the necessary steps for that payment method. <br> 3. Customer clicks "Place order." |
  
![Diagramming](https://github.com/msavoiu/CPSC-362-Group-Project-Activity-1/blob/706b8d486aa337414dddcde24064687a4e64fe00/diagram.drawio.png)

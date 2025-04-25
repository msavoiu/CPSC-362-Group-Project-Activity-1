# Register and login
Customer_register("testuser@gmail.com", "testpassword")
Customer_login("testuser@gmail.com", "testpassword")
view_all_customers()

add_product("yellow", "small", "30", "Small Yellow Windbreaker", "small_yellow_windbreaker.png")
add_product("white", "medium", "25", "Medium White Tshirt", "medium_white_tshirt.png")
add_product("black", "large", "15", "Large Black Jacket", "large_black_jacket.png")
add_product("blue", "small", "12", "Small Blue Hoodie", "small_blue_hoodie.png")
add_product("green", "medium", "18", "Medium Green Cargo Pants", "medium_green_button_up.png")
add_product("red", "large", "8", "Large Red Sweatpants", "large_red_sweatpants.png")

view_all_products()

# Search by color, size, or item
search_inventory_by_description("pants")
search_inventory_by_description("small")

#add_to_cart(customer_id, product_id, quantity)
add_to_cart(1, 5, 1)
add_to_cart(1, 3, 1)
place_order_from_cart(1)
view_order_history(1)

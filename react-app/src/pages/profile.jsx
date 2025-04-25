import { useState, useEffect } from "react";

export default function ProfilePage() {
  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const fetchProfileData = async () => {
      try {
        setLoading(true);
        const response = await fetch("http://localhost:5000/api/profile", {
          credentials: "include" // Important for including cookies in the request
        });
        
        if (!response.ok) {
          if (response.status === 401) {
            throw new Error("Please log in to view your profile");
          } else if (response.status === 404) {
            throw new Error("User profile not found");
          } else {
            throw new Error("Failed to load profile data");
          }
        }
        
        const data = await response.json();
        setProfileData(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    
    fetchProfileData();
  }, []);
  
  if (loading) return <div>Loading profile...</div>;
  if (error) return <div>{error}</div>;
  if (!profileData) return <div>No profile data available</div>;

  const { user } = profileData.data;
  const orderHistory = profileData.order_history || [];
  
  // Group orders by order_id
  const orderGroups = orderHistory.reduce((groups, item) => {
    const group = groups[item.order_id] || [];
    group.push(item);
    groups[item.order_id] = group;
    return groups;
  }, {});
  
  return (
    <div>
      <div>
        <h1>Your Profile</h1>
        <div>
          <span>Customer ID:</span> {user.customer_id}
        </div>
        <div>
          <span>Email:</span> {user.email}
        </div>
      </div>
      
      <div>
        <h2>Your Order History</h2>
        
        {orderHistory.length === 0 ? (
          <div>
            <p>You haven"t placed any orders yet.</p>
          </div>
        ) : (
          Object.entries(orderGroups).map(([orderId, orderItems]) => (
            <div key={orderId}>
              <div>
                <div>
                  <h3>Order #{orderId}</h3>
                  <span>{new Date(orderItems[0].order_date).toLocaleDateString()}</span>
                </div>
              </div>
              
              <div>
                {orderItems.map((item, index) => (
                  <div key={`${orderId}-${item.product_id}-${index}`}>
                    <div>
                      {/* Placeholder for product image */}
                      <span>Item</span>
                    </div>
                    <div>
                      <div>{item.description || "Product name unavailable"}</div>
                      <div>
                        Product ID: {item.product_id}
                      </div>
                      <div>
                        {item.color && `Color: ${item.color}`} 
                        {item.size && item.color && " | "}
                        {item.size && `Size: ${item.size}`}
                      </div>
                    </div>
                    <div>
                      <div>Quantity: {item.quantity}</div>
                    </div>
                  </div>
                ))}
              </div>
              
              <div>
                <button>
                  View Order Details
                </button>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

// import React from "react";
// import "./profile.css";
// // import Order from "./../components/order.jsx";

// function Profile() {
//     const [profileData, setProfileData] = useState<ProfileData | null>(null);
//     const [isLoading, setIsLoading] = useState(true);
//     const [hasError, setHasError] = useState(false);

//     useEffect(() => {
//         const fetchProfileData = async () => {
//             try {
//                 const response = await fetch(
//                     "http://localhost:5000/api/profile",
//                     {
//                         method: "GET"
//                     }
//                 );
//                 const res = await response.json();

//                 if (res.status != 200) {
//                     setHasError(true);
//                 } else {
//                     setProfileData(res);
//                 }
//             } catch (error) {
//                 setHasError(true);
//                 console.error(error.message);
//             } finally {
//                 setIsLoading(false);
//             }
//         };

//         fetchProfileData();
//     }, [userId]);

//     if (isLoading) return <p>Loading...</p>;
//     if (hasError) return <p>An error has occurred. Please try again later.</p>
//     if (!profileData) return <p>No profile data available.</p>

//     // Create render-able components for the user"s orders
//     const { user } = profileData.data;
//     const orderHistory = profileData.order_history || [];

//     const orderGroups = orderHistory.reduce((groups, item) => {
//         const group = groups[item.order_id] || [];
//         group.push(item);
//         groups[item.order_id] = group;
//         return groups;
//     }, {});

//     // const orders = profileData.order_history.map((tag, index) =>
//     //     (
//     //         <li>
//     //             <h3>Order {}</h3>
//     //         </li>
//     //     )
//     // );

//     return (
//         <>
//             <div className="profile-block">
//                 <img src="../static/usericon.png" alt="User icon"></img>
//                 <h1>profile</h1>
//                 <h3>user.</h3>
//             </div>

//             <h2>orders</h2>
//             {/* <ul>
//                 {orders}
//             </ul> */}
//         </>
//     );
// }

// export default Profile;

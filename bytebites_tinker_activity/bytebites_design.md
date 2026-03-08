# ByteBites Revised Class Diagram

```mermaid
classDiagram
    class Customer {
        -string name
        -list~Order~ purchaseHistory
        +Customer(string name)
        +string getName()
        +list~Order~ getPurchaseHistory()
        +void addPurchase(Order order)
        +bool verifyRealUser()
        +int getTotalOrders()
    }

    class Food {
        -string name
        -float price
        -string category
        -float popularityRating
        +Food(string name, float price, string category)
        +string getName()
        +float getPrice()
        +string getCategory()
        +float getPopularityRating()
        +void setPrice(float price)
        +void updateRating(float rating)
    }

    class Menu {
        -list~Food~ items
        +Menu()
        +void addItem(Food food)
        +void removeItem(Food food)
        +list~Food~ getAllItems()
        +list~Food~ filterByCategory(string category)
        +Food findItemByName(string name)
        +int getItemCount()
    }

    class Order {
        -string orderId
        -Customer customer
        -list~Food~ items
        -float totalCost
        -datetime orderDate
        +Order(string orderId, Customer customer)
        +void addItem(Food food)
        +void removeItem(Food food)
        +float computeTotal()
        +list~Food~ getItems()
        +Customer getCustomer()
        +string getOrderId()
        +datetime getOrderDate()
    }

    Customer "1" --> "0..*" Order : places
    Order "*" --> "1" Customer : belongs to
    Order "0..*" --> "1..*" Food : contains
    Menu "1" --> "0..*" Food : manages
```

## Design Rationale

### Customer Class
- Tracks `name` for customer identification
- `purchaseHistory` list maintains all past orders for verification
- `verifyRealUser()` method checks purchase history to confirm real users
- `addPurchase()` maintains the history when new orders are placed

### Food Class
- Includes all required attributes: `name`, `price`, `category`, `popularityRating`
- `updateRating()` allows dynamic adjustment of popularity
- Getters provide access to immutable attributes

### Menu Class
- `items` collection holds all available food items
- `filterByCategory()` enables filtering by categories like "Drinks", "Desserts"
- `findItemByName()` supports item lookup
- Acts as a container/manager for all Food items

### Order Class
- Groups selected items in the `items` list
- `computeTotal()` calculates total cost from all items
- Links to the `customer` who placed the order
- `orderId` and `orderDate` provide transaction tracking

## Relationships
- **Customer ↔ Order**: One-to-many bidirectional (each customer can have multiple orders, each order belongs to one customer)
- **Order → Food**: Many-to-many (orders contain multiple food items, food items can appear in multiple orders)
- **Menu → Food**: One-to-many composition (menu manages the collection of all food items)

This design satisfies all spec requirements while maintaining clean object-oriented principles.

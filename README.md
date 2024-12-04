# reto_03

El siguiente código simula un sistema de pedidos de un restaurante. Contiene clases para representar elementos del menú como bebidas, aperitivos y platos principales, cada uno con atributos específicos. La clase `Menu` gestiona los items disponibles y la clase `Order` permite agregar elementos al pedido, aplicar descuentos y calcular el total teniendo en cuenta la cantidad de items y los descuentos. El sistema también permite al usuario ingresar detalles adicionales para cada ítem del pedido, como la temperatura de las bebidas o el tiempo de preparación de los platos.

``` python
class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, temperature: float = 0, is_sugared: bool = False) -> None:
        super().__init__(name, price)
        self.temperature = temperature
        self.is_sugared = is_sugared

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, calories: float = 0) -> None:
        super().__init__(name, price)
        self.calories = calories

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, is_vegetarian: bool = False, prep_time: float = 0) -> None:
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian
        self.prep_time = prep_time

class Menu:
    def __init__(self) -> None:
        self.items = [
            Beverage("Soda", 2),
            Beverage("Tea", 3),
            Beverage("Coffee", 5),
            Beverage("Juice", 4),
            Beverage("Water", 4),
            Appetizer("Fruit", 2),
            Appetizer("Cookies", 4),
            Appetizer("Popcorn", 4),
            MainCourse("Pizza", 10),
            MainCourse("Burger", 12),
            MainCourse("Spaghetti", 14),
            MainCourse("Salad", 8)
        ]

    def get_item(self, name: str) -> "MenuItem":
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

class Order:
    def __init__(self, menu: Menu) -> None:
        self.menu = menu
        self.menu_items = []
        
    # Add an item to the order
    def add_item(self, name: str) -> None:
        item = self.menu.get_item(name)  
        if item:
            self.menu_items.append(item)
        else:
            print(f"Item '{name}' is not in the menu")

    # Apply a discount
    def apply_discount(self) -> float:
        total_price = 0
        beverage_count = 0
        appetizer_count = 0
        main_course_count = 0

        for item in self.menu_items:
            total_price += item.price

            if type(item) == Beverage:
                beverage_count += 1
            elif type(item) == Appetizer:
                appetizer_count += 1
            elif type(item) == MainCourse:
                main_course_count += 1

        discount = 0
        if total_price >= 50:
            discount = 0.2  # 20% discount for orders above $50
        elif total_price >= 30:
            discount = 0.1  # 10% discount for orders above $30

        if beverage_count >= 2:
            discount += 0.05  # 5% extra discount for 2 or more beverages
        if appetizer_count >= 2:
            discount += 0.1  # 10% extra discount for 2 or more appetizers
        if main_course_count >= 1 and appetizer_count >= 1:
            discount += 0.1  # 10% combo discount for having a main course and appetizer

        return discount

    # Calculate total price
    def calculate_total_price(self) -> float:
        total_price = 0
        for item in self.menu_items:
            total_price += item.price

        discount = self.apply_discount()
        total_price -= total_price * discount  # Apply the discount
        return total_price

menu = Menu()
order = Order(menu)

# Show the menu
print("Menu:")
for item in menu.items:
    print(f"{item.name} - ${item.price}")

print("\nType the name of the item you want to order. Type 'done' to finish your order\n")

# Allow the user to add more items
while True:
    item_name = input("Enter item name: ").strip()
    if item_name.lower() == "done":
        break
    order.add_item(item_name)


if order.menu_items:
    print("\nYour order:")
    for item in order.menu_items:
        print(f"- {item.name}: ${item.price}")
    
    # Obtain more details about the order
    for item in order.menu_items:
        if type(item) == Beverage:
            item.temperature = float(input(f"Indicate the temperature of the {item.name.lower()}: "))
            item.is_sugared = input(f"Would you like your {item.name.lower()} with sugar? (y/n): ").strip().lower() == "y"
        elif type(item) == Appetizer:
            item.calories = float(input(f"Indicate the amount of calories for your {item.name.lower()}: "))
        elif type(item) == MainCourse:
            item.is_vegetarian = input(f"Would you like the {item.name.lower()} to be vegetarian? (y/n): ").strip().lower() == "y"
            item.prep_time = float(input(f"Indicate the preparation time for your {item.name.lower()} (in minutes): "))
else:
    print("\nNo items were ordered")
    

# Calculate the total price
total_price = order.calculate_total_price()
print(f"\nThe total price is: ${total_price}")
```
***

### Diagrama de clases 

``` mermaid
classDiagram
    class MenuItem {
        + name: str
        + price: float
        + __init__(name: str, price: float)
    }

    class Beverage {
        + temperature: float
        + is_sugared: bool
        + __init__(name: str, price: float, temperature: float=0, is_sugared: bool=False)
    }

    class Appetizer {
        + calories: float
        + __init__(name: str, price: float, calories: float=0)
    }

    class MainCourse {
        + is_vegetarian: bool
        + prep_time: float
        + __init__(name: str, price: float, is_vegetarian: bool=False, prep_time: float=0)
    }

    class Menu {
        + items: List[MenuItem]
        + __init__()
        + get_item(name: str): MenuItem
    }

    class Order {
        + menu: Menu
        + menu_items: List[MenuItem]
        + __init__(menu: Menu)
        + add_item(name: str)
        + apply_discount(): float
        + calculate_total_price(): float
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Menu "1" *-- "1..*" MenuItem : contains
    Order "1" *-- "1" Menu : uses
    Order "1" *-- "0..*" MenuItem : contains
```
***

### Ejemplo de uso

En este ejemplo, el usuario selecciona tres ítems del menú: una soda, un café y una pizza. El sistema solicita detalles sobre las bebidas (temperatura y si lleva azúcar) y la pizza (si es vegetariana y su tiempo de preparación). Después, se calcula el total de la compra aplicando el descuento del 5% del pedido al haber 2 bebidas. Finalmente, el precio total con el descuento aplicado es de $16.15.

``` bash
Menu:
Soda - $2
Tea - $3
Coffee - $5
Juice - $4
Water - $4
Fruit - $2
Cookies - $4
Popcorn - $4
Pizza - $10
Burger - $12
Spaghetti - $14
Salad - $8

Type the name of the item you want to order. Type 'done' to finish your order


Your order:
- Soda: $2
- Coffee: $5
- Pizza: $10

The total price is: $16.15
```

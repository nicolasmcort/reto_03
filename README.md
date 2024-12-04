# reto_03

Descripción breve del código

``` python

```

Diagrama de clases 

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

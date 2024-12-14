import os
import django
import json
from datetime import date, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlateSync.settings')
django.setup()

# Import models
from inventory.models import Supplier, Ingredient, MenuItem, Order

def create_suppliers():
    suppliers = [
        {
            'name': 'Fresh Produce Inc.',
            'contact_info': 'Contact: John Smith\nEmail: john@freshproduce.com\nPhone: (555) 123-4567'
        },
        {
            'name': 'Meat Masters',
            'contact_info': 'Contact: Sarah Johnson\nEmail: sarah@meatmasters.com\nPhone: (555) 987-6543'
        },
        {
            'name': 'Dairy Delights',
            'contact_info': 'Contact: Mike Brown\nEmail: mike@dairydelights.com\nPhone: (555) 246-8135'
        }
    ]
    
    created_suppliers = []
    for supplier_data in suppliers:
        supplier, created = Supplier.objects.get_or_create(**supplier_data)
        created_suppliers.append(supplier)
    
    return created_suppliers

def create_ingredients(suppliers):
    ingredients = [
        {
            'name': 'Tomatoes',
            'stock_quantity': 50.5,
            'unit': 'kg',
            'expiry_date': date.today() + timedelta(days=14),
            'supplier': suppliers[0]
        },
        {
            'name': 'Beef Sirloin',
            'stock_quantity': 25.0,
            'unit': 'kg',
            'expiry_date': date.today() + timedelta(days=7),
            'supplier': suppliers[1]
        },
        {
            'name': 'Mozzarella Cheese',
            'stock_quantity': 15.5,
            'unit': 'kg',
            'expiry_date': date.today() + timedelta(days=21),
            'supplier': suppliers[2]
        },
        {
            'name': 'Chicken Breast',
            'stock_quantity': 30.0,
            'unit': 'kg',
            'expiry_date': date.today() + timedelta(days=10),
            'supplier': suppliers[1]
        }
    ]
    
    created_ingredients = []
    for ingredient_data in ingredients:
        ingredient, created = Ingredient.objects.get_or_create(**ingredient_data)
        created_ingredients.append(ingredient)
    
    return created_ingredients

def create_menu_items(ingredients):
    menu_items = [
        {
            'name': 'Classic Beef Burger',
            'recipe': json.dumps({
                'Beef Sirloin': 0.2,  # 200g of beef
                'Tomatoes': 0.05      # 50g of tomatoes
            }),
            'price': 12.99
        },
        {
            'name': 'Margherita Pizza',
            'recipe': json.dumps({
                'Tomatoes': 0.1,       # 100g of tomatoes
                'Mozzarella Cheese': 0.1  # 100g of cheese
            }),
            'price': 10.50
        },
        {
            'name': 'Grilled Chicken Salad',
            'recipe': json.dumps({
                'Chicken Breast': 0.15,  # 150g of chicken
                'Tomatoes': 0.07         # 70g of tomatoes
            }),
            'price': 11.75
        }
    ]
    
    created_menu_items = []
    for menu_item_data in menu_items:
        menu_item, created = MenuItem.objects.get_or_create(**menu_item_data)
        created_menu_items.append(menu_item)
    
    return created_menu_items

def create_orders(menu_items):
    orders = [
        {
            'menu_item': menu_items[0],  # Beef Burger
            'quantity': 5
        },
        {
            'menu_item': menu_items[1],  # Margherita Pizza
            'quantity': 3
        },
        {
            'menu_item': menu_items[2],  # Grilled Chicken Salad
            'quantity': 4
        }
    ]
    
    created_orders = []
    for order_data in orders:
        order, created = Order.objects.get_or_create(**order_data)
        created_orders.append(order)
    
    return created_orders

def populate_database():
    # Clear existing data
    Supplier.objects.all().delete()
    Ingredient.objects.all().delete()
    MenuItem.objects.all().delete()
    Order.objects.all().delete()
    
    # Create data
    suppliers = create_suppliers()
    ingredients = create_ingredients(suppliers)
    menu_items = create_menu_items(ingredients)
    orders = create_orders(menu_items)
    
    print("Database populated successfully!")
    print(f"Created {len(suppliers)} suppliers")
    print(f"Created {len(ingredients)} ingredients")
    print(f"Created {len(menu_items)} menu items")
    print(f"Created {len(orders)} orders")

if __name__ == '__main__':
    populate_database()

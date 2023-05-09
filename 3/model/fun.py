from model.models import *
def add_menu_element(entity, menu_element):
    entity.menu_elements.append(menu_element)

def get_total_cost(entity):
    total = 0
    for element in entity.menu_elements:
        total += element.price
    return total

def get_order_items(entity):
    items = []
    for element in entity.menu_elements:
        items.append(element.get_info())
    return items

def serve_table(entity, table:Table):
    if table.is_available:
        table.mark_as_unavailable(entity.name)##################################
        entity.tables_served.append(table)
        return f"Table {table.number} is now served by {entity.name}."
    else:
        return f"Table {table.number} is already served by {table.waiter}."


def mark_as_available(entity):
    entity.is_available = True
    entity.order = None

def mark_as_unavailable(entity, waiter):
    entity.is_available = False
    entity.waiter = waiter
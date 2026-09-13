def calculate_total(quantity,price):
    """Calculates Total"""
    return quantity * price

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"
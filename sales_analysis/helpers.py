def calculate_total(quantity,price):
    #helper function to calculate total sales amount
    """Calculates Total"""
    return quantity * price

def format_currency(amount):
    #helper function to format number as currency
    """Format number as currency"""
    return f"${amount:,.2f}"
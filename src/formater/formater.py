from decimal import Decimal, getcontext

def format_commission_rates(commission_rates):
    rate = int(commission_rates['rate']) / 1e18
    max_rate = int(commission_rates['max_rate']) / 1e18
    max_change_rate = int(commission_rates['max_change_rate']) / 1e18
    return {
        'rate': f"{rate:.18f}",
        'max_rate': f"{max_rate:.18f}",
        'max_change_rate': f"{max_change_rate:.18f}"
    }

def large_int_to_string(number: str, precision: int = 18) -> str:
    try:
        if '.' in number:
            return number
        else:
            number_decimal = Decimal(int(number))
        
        getcontext().prec = precision + 21
        
        divisor = Decimal(1e18)
        result = number_decimal / divisor
        
        format_string = f'{{:.{precision}f}}'
        formatted_result = format_string.format(result)
        
        return formatted_result
    
    except (ValueError, OverflowError, ArithmeticError) as e:
        print(f"Error converting or processing the number: {e}")
        return number
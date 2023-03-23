def pearson_correlation_coefficient(houses):
    n = len(houses)
    
    mean_bedrooms = sum([house['bedrooms'] for house in houses]) / n
    mean_prices = sum([house['price'] for house in houses]) / n
    
    var_bedrooms = sum((house['bedrooms'] - mean_bedrooms)**2 for house in houses)
    var_prices = sum((house['price'] - mean_prices)**2 for house in houses)
    covariance = sum((house['bedrooms'] - mean_bedrooms) * (house['price'] - mean_prices) for house in houses)
    
    correlation_coefficient = covariance / (var_bedrooms*var_prices)**0.5
    
    return correlation_coefficient
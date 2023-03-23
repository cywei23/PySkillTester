def pearson_correlation_coefficient(houses):
    n = len(houses)
    
    mean_bedrooms = sum([house['bedrooms'] for house in houses]) / n
    mean_prices = sum([house['price'] for house in houses]) / n
    
    var_bedrooms = sum((house['bedrooms'] - mean_bedrooms)**2 for house in houses)
    var_prices = sum((house['price'] - mean_prices)**2 for house in houses)
    covariance = sum((house['bedrooms'] - mean_bedrooms) * (house['price'] - mean_prices) for house in houses)
    
    correlation_coefficient = covariance / (var_bedrooms*var_prices)**0.5
    
    return correlation_coefficient


houses = [
    {"bedrooms": 2, "bathrooms": 1, "square_footage": 800, "price": 250000},
    {"bedrooms": 3, "bathrooms": 2, "square_footage": 1200, "price": 350000},
    {"bedrooms": 4, "bathrooms": 3, "square_footage": 2000, "price": 500000},
    {"bedrooms": 5, "bathrooms": 4, "square_footage": 3000, "price": 750000},
]

output = pearson_correlation_coefficient(houses)
print(output)  # Should be close to 1, as there is a strong positive correlation
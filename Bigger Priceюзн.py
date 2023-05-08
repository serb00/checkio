def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    """
    TOP most expensive goods
    """
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

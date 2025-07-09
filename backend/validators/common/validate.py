def validate_payload(data: dict, schema: dict, custom_rules=None) -> bool:
    try:
        for field, expected_type in schema.items():
            if field not in data:
                return False
            if not isinstance(data[field], expected_type):
                return False
            
        if custom_rules:
            return custom_rules(data)
        
        return True
    except Exception:
        return False
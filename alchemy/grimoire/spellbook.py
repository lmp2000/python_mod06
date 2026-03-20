def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    val_output = validate_ingredients(ingredients)
    if 'INVALID' in val_output:
        return f"Spell rejected: {spell_name} ({val_output})"
    elif 'VALID' in val_output:
        return f"Spell recorded: {spell_name} ({val_output})"
    else:
        return None
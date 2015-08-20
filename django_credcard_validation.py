# -*- coding:utf-8 -*-
def valid_card_brand(brand, card_number):
    """
    Validação de CC de acordo com a bandeira (DJANGO)
    """
    # Validando Numero Cartão (Algoritmo de Luhn)
    try:
        int(card_number)
    except:
        raise ValidationError("Cartão inválido")
        return False
    card_list = [int(x) for x in card_number]
    total = 0
    for pos in range(0, len(card_list), 2):
        card_list[pos] = card_list[pos] * 2
    card_join = "".join(str(e) for e in card_list)
    for i in card_join:
        total += int(i)
    if not total % 10 is 0:
        raise ValidationError("Numero de cartão inválido")
        return False
    # Validando bandeira
    brands = {
        "vi": r"^4\d{3}-?\d{4}-?\d{4}-?\d{4}$",
        "mv": r"^5[1-5]\d{2}-?\d{4}-?\d{4}-?\d{4}$",
        "ae": r"^3[4,7]\d{13}$",
        "dc": r"^3[0,6,8]\d{12}$"
    }

    regex = re.compile(brands.get(brand))
    if not re.search(regex, card_number):
        raise ValidationError("Cartão não pertence a bandeira selecionada")
        return False
    return card_number

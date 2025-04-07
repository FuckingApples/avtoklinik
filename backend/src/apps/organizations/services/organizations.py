def build_permission_mask(bits: list[int]) -> int:
    """
    Создает битовую маску разрешений на основе списка битов. Пример: [0, 1, 2] -> 0b111
    """
    mask = 0
    for bit in bits:
        mask |= 1 << bit
    return mask

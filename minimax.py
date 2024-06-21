def minimax(state, is_maximizer):
    children = state.children()

    if len(children) == 0:
        return state.value()

    if is_maximizer:
        max_value = float('-inf')
        for child in children:
            value = minimax(child, not is_maximizer)
            max_value = max(value, max_value)
        return max_value
    else:
        min_value = float('inf')
        for child in children:
            value = minimax(child, not is_maximizer)
            min_value = min(value, min_value)
        return min_value

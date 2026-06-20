def optimize_weights(current_weights, policy, participants, history):
    # псевдоградиентный подъём субъектности
    grad = compute_subjectivity_gradient(current_weights, participants, history)
    return current_weights.update_from_gradient(grad)

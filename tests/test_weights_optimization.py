def test_weights_update():
    w = Weights()
    initial = w.as_vector().copy()
    grad = np.array([0.1, 0.2, 0.0, -0.1, 0.05, 0.15])
    w.update_from_gradient(grad, eta=1.0)
    assert np.allclose(w.as_vector(), initial + grad)

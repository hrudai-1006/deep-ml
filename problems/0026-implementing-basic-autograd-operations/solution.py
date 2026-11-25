class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
    def __repr__(self):
        def fmt(x):
            return int(x) if float(x).is_integer() else round(x, 4)
        return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"

    def __add__(self, other):
         # Implement addition here
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")
        out._backward = lambda: (
            setattr(self, "grad", self.grad + out.grad),
            setattr(other, "grad", other.grad + out.grad),
        )
        return out

    def __mul__(self, other):
        # Implement multiplication here
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")
        out._backward = lambda: (
            setattr(self, "grad", self.grad + other.data * out.grad),
            setattr(other, "grad", other.grad + self.data * out.grad),
        )
        return out

    def relu(self):
        # Implement ReLU here
        out = Value(max(0, self.data), (self,), "ReLU")
        out._backward = lambda: setattr(
            self, "grad", self.grad + (out.data > 0) * out.grad
        )
        return out
    def backward(self):
        # Implement backward pass here
        topo, visited = [], set()
        def build(v):
            if v not in visited:
                visited.add(v)
                for c in v._prev: build(c)
                topo.append(v)
        build(self)
        self.grad = 1
        for v in reversed(topo): v._backward()
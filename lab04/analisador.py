class Analisador:
    def init(self):
        pass

    def acha_sequencia(self, valores, probs) -> int:
        num = len(valores)
        indices_ordenados = sorted(range(num), key=lambda i: (-valores[i], probs[i]))
        return indices_ordenados

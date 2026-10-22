def validar_duracao(valor):
    try:
        duracao = int(valor)
    except (TypeError, ValueError):
        raise ValueError("Informe a duração em minutos usando um número inteiro.") from None

    if duracao <= 0:
        raise ValueError("A duração deve ser maior que zero.")
    return duracao


def formatar_tempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    return f"{minutos:02d}:{segundos:02d}"


class Pomodoro:
    def __init__(self, foco_minutos=25, descanso_minutos=5):
        self.foco_minutos = validar_duracao(foco_minutos)
        self.descanso_minutos = validar_duracao(descanso_minutos)
        self.modo = "foco"
        self.segundos_restantes = self.foco_minutos * 60
        self.executando = False

    def configurar(self, foco_minutos, descanso_minutos):
        foco_minutos = validar_duracao(foco_minutos)
        descanso_minutos = validar_duracao(descanso_minutos)
        self.foco_minutos = foco_minutos
        self.descanso_minutos = descanso_minutos
        self.reiniciar()

    def iniciar(self):
        self.executando = True

    def pausar(self):
        self.executando = False

    def reiniciar(self):
        self.executando = False
        duracao = self.foco_minutos if self.modo == "foco" else self.descanso_minutos
        self.segundos_restantes = duracao * 60

    def avancar_segundo(self):
        if not self.executando:
            return None

        self.segundos_restantes -= 1
        if self.segundos_restantes > 0:
            return None

        modo_concluido = self.modo
        self.modo = "descanso" if self.modo == "foco" else "foco"
        duracao = self.foco_minutos if self.modo == "foco" else self.descanso_minutos
        self.segundos_restantes = duracao * 60
        return modo_concluido

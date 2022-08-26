def it_s_7_am():
    import time

    segundos = time.time()
    tempo_local = time.localtime(segundos)
    hora_atual = tempo_local.tm_hour

    if (hora_atual == 7):
        return True
    else:
        return False
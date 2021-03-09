from pypro.modulos import facade


def listar_modulos(resquest):
    return {'MODULOS': facade.listar_modulos_ordenados()}

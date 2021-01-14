from flask import flash
CADASTRADO_COM_SUCESSO = "{0} (a) Cadastrado com sucesso"
ATUALIZADO_COM_SUCESSO = "{0} (a) Atualizado com sucesso"
ERRO_FORMULARIO = "{0} (a) Erro ao realizar o cadastro"
SMS_ENVIO_ERRO = "Problema ao enviar a SMS"
SMS_FALTA_PARAMETROS ="PREENCHA TODOS OS PARAMETROS NECESSÁRIOS"
SMS_ENVIO_SUCESSO = "SMS (s) Enviado com sucesso"
ITEM_JA_CADASTRADO = "{0}  Já cadastrado(a)!"

class MESSAGES:

    @staticmethod
    def CADASTRADO_COM_SUCESSO(model='',default='success'):
        return flash(CADASTRADO_COM_SUCESSO.format(model), default)

    def ATUALIZADO_COM_SUCESSO(model='',default='success'):
        return flash(ATUALIZADO_COM_SUCESSO.format(model), default)
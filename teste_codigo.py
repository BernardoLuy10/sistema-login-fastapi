from app.core.security import gerar_codigo_verificacao

for _ in range(10):
    codigo = gerar_codigo_verificacao()
    assert len(codigo) == 6
    assert codigo.isdigit()
    print(codigo)

print("Todos os códigos possuem 6 dígitos")
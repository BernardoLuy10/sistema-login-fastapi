from app.core.security import(
    gerar_codigo_verificacao,
    gerar_hash_codigo,
    verificar_codigo
    )

for _ in range(10):
    codigo = gerar_codigo_verificacao()
    assert len(codigo) == 6
    assert codigo.isdigit()
    print(codigo)

codigo = gerar_codigo_verificacao()
codigo_hash = gerar_hash_codigo(codigo)

codigo_incorreto = "000000" if codigo != "000000" else "999999"

assert codigo != codigo_hash
assert verificar_codigo(codigo, codigo_hash)
assert not verificar_codigo(codigo_incorreto, codigo_hash)


print("Todos os códigos possuem seis dígitos.")
print("O código correto foi validado.")
print("O código incorreto foi rejeitado.")
gerente = 8500.0
analista = 5000.0
suporte = 3000.0

aumentogerente_analista = 0.12
aumentosuporte = 0.15

salariogerente = gerente * (1 + aumentogerente_analista)
salarioanalista = analista * (1 + aumentogerente_analista)
salariosuporte = suporte * (1 + aumentosuporte)

print(f"Gerente: R$ {salariogerente:.2f}")
print(f"Analista: R$ {salarioanalista:.2f}")
print(f"Suporte: R$ {salariosuporte:.2f}")
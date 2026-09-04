from datetime import datetime, timezone

def codigo_esta_expirado(expira_em: str) -> bool:
    data_expiracao = datetime.fromisoformat(expira_em)
    data_atual = datetime.now(timezone.utc)

    return data_atual >= data_expiracao

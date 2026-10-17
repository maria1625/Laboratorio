# feature_flags.py
import os
import configcatclient


SDK_KEY = os.getenv("CONFIGCAT_SDK_KEY", "configcat-sdk-1/lyzfCBF7X02E9OY-bbNjyw/bxOwDCc59Um19ovki-HgRQ")

client = configcatclient.get(
    SDK_KEY,
    configcatclient.PollingMode.auto_poll(poll_interval_seconds=30)
)

def is_toggle_enabled(flag_key: str, default_value: bool = False) -> bool:
    """
    Pregunta a ConfigCat si la bandera está en ON o en OFF.
    Si no hay conexión o la clave no existe, devuelve default_value (False por seguridad).
    """
    return client.get_value(flag_key, default_value)
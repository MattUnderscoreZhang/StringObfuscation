import obfuscator


def lambda_handler(event, context) -> dict[str, str]:
    obfuscated_string = obfuscator.obfuscate_string(event["input"])
    return {"output": obfuscated_string}

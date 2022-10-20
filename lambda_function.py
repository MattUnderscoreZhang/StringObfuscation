import obfuscator
from typing import Any


def lambda_handler(event, context) -> dict[str, Any]:
    obfuscated_string = obfuscator.obfuscate_string(event["input"])
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'origin, content-type, accept',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': obfuscated_string
    }

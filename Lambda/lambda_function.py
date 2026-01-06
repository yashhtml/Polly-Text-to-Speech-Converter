import boto3
import base64

polly = boto3.client('polly')

def lambda_handler(event, context):
    text = event.get('text', 'Hello! This is AWS Polly text to speech.')

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    audio_stream = response['AudioStream'].read()
    audio_base64 = base64.b64encode(audio_stream).decode('utf-8')

    return {
        'statusCode': 200,
        'audio_base64': audio_base64
    }

from .serializers import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        **UserSerializer(user, context={'request': request}).data
    }
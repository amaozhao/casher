from dj_rest_auth.serializers import JWTSerializer

class CustomJWTSerializer(JWTSerializer):
    def to_representation(self, instance):
        return {
            'access': instance['access'],  # JWT access token
            'refresh': instance['refresh'],  # JWT refresh token
            'user': {
                'id': instance['user'].id,
                'username': instance['user'].username,
            }
        }

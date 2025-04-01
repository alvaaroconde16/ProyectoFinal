from rest_framework import serializers
from .models import *
from datetime import datetime
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class PeluqueriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peluqueria
        fields = '__all__'


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'



class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, error_messages={
        "min_length": "La contraseña debe tener al menos 8 caracteres"
    })

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'telefono', 'foto_perfil', 'rol', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'rol': {'required': True},
        }

    def validate_email(self, email):
        """ Verifica si el correo ya está en uso """
        usuario_existente = Usuario.objects.filter(email=email).first()
        if usuario_existente and (self.instance is None or usuario_existente.id != self.instance.id):
            raise serializers.ValidationError('Ya existe un usuario con este correo electrónico')
        return email

    def validate_telefono(self, telefono):
        """ Verifica que el teléfono tenga un formato válido """
        if telefono and (not telefono.isdigit() or len(telefono) < 9):
            raise serializers.ValidationError('El teléfono debe contener al menos 9 dígitos')
        return telefono

    def create(self, validated_data):
        """ Crea un usuario con la contraseña encriptada """
        password = validated_data.pop('password')
        usuario = Usuario.objects.create_user(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        """ Actualiza un usuario y encripta la nueva contraseña si se proporciona """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.foto_perfil = validated_data.get('foto_perfil', instance.foto_perfil)
        instance.rol = validated_data.get('rol', instance.rol)

        # Si el usuario proporciona una nueva contraseña, la encripta
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance


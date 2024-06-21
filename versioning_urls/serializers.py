import random

from rest_framework import serializers


class URLPathVersioningClassSerializer(serializers.Serializer):
    patient_name = serializers.SerializerMethodField(read_only=True, method_name='get_patient_name')
    patient_disease = serializers.SerializerMethodField(read_only=True, method_name='get_patient_disease')
    versioning = serializers.SerializerMethodField(read_only=True, method_name='get_versioning')

    def get_patient_name(self, obj):
        request = self.context.get("request")
        if request.version == 'v1':
            return random.choice(["V1 abc", "V1 bcd", "V1 cde"])
        else:
            return random.choice(["abc", "bcd", "cde"])

    def get_patient_disease(self, obj):
        request = self.context.get("request")
        if request.version == 'v1':
            return random.choice(["V1 fever", "V1 cold", "V1 cough"])
        else:
            return random.choice(["fever", "cold", "cough"])

    def get_versioning(self, obj):
        return "URLPathVersioning"


    class Meta:
        fields = ('patient_name', 'patient_disease', 'versioning')


class AcceptHeaderVersioningClassSerializer(serializers.Serializer):
    patient_name = serializers.SerializerMethodField(read_only=True, method_name='get_patient_name')
    patient_disease = serializers.SerializerMethodField(read_only=True, method_name='get_patient_disease')
    versioning = serializers.SerializerMethodField(read_only=True, method_name='get_versioning')

    def get_patient_name(self, obj):
        request = self.context.get("request")
        if request.version == 'v1':
            return random.choice(["V1 abc", "V1 bcd", "V1 cde"])
        else:
            return random.choice(["abc", "bcd", "cde"])

    def get_patient_disease(self, obj):
        request = self.context.get("request")
        if request.version == 'v1':
            return random.choice(["V1 fever", "V1 cold", "V1 cough"])
        else:
            return random.choice(["fever", "cold", "cough"])

    def get_versioning(self, obj):
        return "AcceptHeaderVersioningClass"


    class Meta:
        fields = ('patient_name', 'patient_disease', 'versioning')

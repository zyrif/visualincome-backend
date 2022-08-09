from rest_framework import serializers
from .models import Income

CONST_RETIREMENT_AGE = 65
CONST_MAXIMUM_AGE = 100
CONST_NATIONAL_GDP = 25347000000000


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"
        extra_kwargs = {
            "end_age": {
                "required": False,
                "default": CONST_RETIREMENT_AGE - 1,
            },
            "final_amount": {
                "required": False,
            },
        }

    def validate_start_age(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "You need to at least be born to use this service."
            )

        if value > CONST_RETIREMENT_AGE:
            raise serializers.ValidationError(
                "Age cannot be greater than the retirement age of {}".format(
                    CONST_RETIREMENT_AGE
                )
            )

        return value

    def validate_init_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Your annual income must be at least 1$")

        if value > CONST_NATIONAL_GDP:
            raise serializers.ValidationError(
                "Your income cannot be greater than the GDP of United States!"
            )

        return value

    def validate(self, data):
        if data["start_age"] >= CONST_RETIREMENT_AGE:
            data["end_age"] = CONST_MAXIMUM_AGE

        if data.get("final_amount", 0) <= 0:
            data["final_amount"] = data["init_amount"]

        return data
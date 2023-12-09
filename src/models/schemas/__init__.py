from pydantic import BaseModel, create_model, Field

from .channel import ChannelSmall, ChannelMedium, ChannelLarge

class FieldCollectorMixin:
    @classmethod
    def get_fields(cls):
        fields = {}
        for base_cls in reversed(cls.mro()):
            if issubclass(base_cls, BaseModel) and hasattr(base_cls, '__annotations__'):
                fields.update({k: v for k, v in base_cls.__annotations__.items() if not k.startswith("_")})
        return fields

    @classmethod
    def create_custom(cls, fields):
        dynamic_model_attrs = {}
        for field_name in fields:
            field_type = cls.__annotations__.get(field_name)
            if field_type:
                dynamic_model_attrs[field_name] = (field_type, Field(...))

        # Добавим возможность обработки вложенных моделей
        for field_name, field_type in cls.__annotations__.items():
            if hasattr(field_type, '__annotations__'):
                dynamic_model_attrs[field_name] = (field_type, Field(...))

        custom_schema = create_model(cls.__name__, **dynamic_model_attrs)
        return custom_schema
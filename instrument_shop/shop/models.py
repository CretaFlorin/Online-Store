from django.db.models import Model, ForeignKey, TextField, DO_NOTHING


class Category(Model):
    name = TextField(max_length=50)


class Instrument(Model):
    name = TextField(max_length=255)
    role = ForeignKey(Category, on_delete=DO_NOTHING)

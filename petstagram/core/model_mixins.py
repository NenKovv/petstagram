class StrFromFieldsMixin:
    str_fields = ()

   # I will upgrade the code
   # def __str__(self):
    #    return '; '.join(
    #        f'{str_field}={getattr(self, str_field, None)}' for str_field in self.str_fields
    #   )

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f' {name}={value}' for (name, value) in fields)
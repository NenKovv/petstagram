from django import forms
from django.core.exceptions import ValidationError

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.core.form_mixin import DisabledFormMixin
from petstagram.pets.forms import PetBaseForm
from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date',)

class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')

class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many-to-many
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()  # one-to-many
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()  # one-to-many
            self.instance.delete()

        return self.instance




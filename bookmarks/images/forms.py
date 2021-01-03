import urllib.request as urlrq
import certifi
import ssl
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.split('.')[-1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not '
                                        'match valid image extensions')
        return url

    def save(self, force_insert=False, force_update=False,
             commit=True):
        """
        Overriding the save method.
        1. create a new image instance by calling the save() method
        of the form with commit=False
        2. Get the url form the cleaned_data
        3. Generate a name of the image by combining the name and extension.
        4. Use the python urllib modeule to download the image and then call
        the save() method of the image field, passing it a ContentFile object
        that is instantiated with the downloaded file content.
        In this way you save the file to the media directory of your project.
        You pass save=False parameter to avoid saving the object to the
        database yet.
        5. In order to maintain the same behavior as the save() method we
        override, you save the form to the database only when the commit
        parameter is True.
        To use urllib to retrieve images served through https, we need to
        install certifi with pip.
        :param force_insert:
        :param force_update:
        :param commit:
        :return:
        """
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.split('.')[-1].lower()
        image_name = f'{name}.{extension}'

        # download the image from the given URL
        response = urlrq.urlopen(image_url, context=ssl.create_default_context(cafile=certifi.where()))
        image.image.save(
            image_name, ContentFile(response.read()),
            save=False
        )
        if commit:
            image.save()
        return image

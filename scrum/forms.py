from django.core.exceptions import ValidationError
from django.core.validators import validate_comma_separated_integer_list

import floppyforms as forms

from scrum.models import Project, Sprint, Team, BZProduct


date5 = forms.DateInput(attrs={
    'placeholder': 'YYYY-MM-DD',
})


class SlugInput(forms.TextInput):

    def get_context_data(self):
        self.attrs['pattern'] = "[-.\w]+"
        return super(SlugInput, self).get_context_data()


class ProjectForm(forms.ModelForm):
    template_title = 'Project'

    class Meta:
        model = Project
        widgets = {
            'slug': SlugInput,
        }
        fields = (
            'name',
            'slug',
            'team',
            'whiteboard_name',
            'wiki_page',
        )


class CreateProjectForm(ProjectForm):
    """Form for creating new projects."""

    def save(self, commit=True):
        return super(CreateProjectForm, self).save(commit)


class SprintForm(forms.ModelForm):
    template_title = 'Sprint'

    class Meta:
        model = Sprint
        widgets = {
            'name': forms.TextInput,
            'slug': SlugInput,
            'start_date': date5,
            'end_date': date5,
            'notes': forms.Textarea(attrs={
                'class': 'span5',
            }),
        }
        fields = (
            'name',
            'slug',
            'start_date',
            'end_date',
            'notes',
            'team',
        )


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = (
            'name',
            'slug',
        )


class SprintBugsForm(forms.ModelForm):
    add_bugs = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validate_comma_separated_integer_list],
    )
    remove_bugs = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validate_comma_separated_integer_list],
    )

    class Meta:
        model = Sprint
        fields = ('add_bugs', 'remove_bugs')

    def _clean_bugs_list(self, field_name):
        bugs = self.cleaned_data[field_name]
        bugs_list = []
        if bugs:
            bugs_list = [int(b) for b in bugs.split(',')]
        return bugs_list

    def clean_add_bugs(self):
        return self._clean_bugs_list('add_bugs')

    def clean_remove_bugs(self):
        return self._clean_bugs_list('remove_bugs')

    def save(self, commit=True):
        add_bugs = self.cleaned_data['add_bugs']
        remove_bugs = self.cleaned_data['remove_bugs']
        self.instance.update_bugs(add_bugs, remove_bugs)
        self.instance._clear_bugs_data_cache()
        return self.instance


class ProjectBugsForm(SprintBugsForm):
    class Meta:
        model = Project
        fields = ('add_bugs', 'remove_bugs')


class CreateTeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = (
            'name',
            'slug',
        )


class BZProductForm(forms.ModelForm):

    class Meta:
        model = BZProduct
        fields = (
            'name',
            'component',
            'project',
        )

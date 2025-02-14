from django.views import generic

from contributors.models import Repository


class DetailView(generic.DetailView):
    """Repository's details."""

    model = Repository
    template_name = 'repository_details.html'

    def get_context_data(self, **kwargs):
        """Add additional context for the repository."""
        context = super().get_context_data(**kwargs)

        contributors_dict = {}
        for contributor in self.object.contributors.filter(is_visible=True):
            contributors_dict[contributor] = (
                contributor.contribution_set.filter(repository=self.object)[0]
            )

        context['contributors'] = contributors_dict
        return context

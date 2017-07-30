import factory

from django.utils import timezone

from polls.models import Poll


class PollFactory(factory.django.DjangoModelFactory):
    question_text = 'factory question'
    pub_date = timezone.now()

    class Meta:
        model = Poll

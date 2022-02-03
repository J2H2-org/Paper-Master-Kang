# management/commands/addpost.py

from django.core.management.base import BaseCommand, CommandError

from chat_redis.models import Post


class Command(BaseCommand):
    help = 'Add as many posts as you want'

    def add_arguments(self, parser):
        parser.add_argument('post_cnt', type=int)

    def handle(self, *args, **options):
        post_cnt = options['post_cnt']
        if post_cnt > 0:
            Post.objects.bulk_create(
                [Post(text="Sample Text #{}".format(i))
                 for i in range(post_cnt)]
            )
            self.stdout.write(self.style.SUCCESS(
                'Successfully add {} posts'.format(post_cnt)))

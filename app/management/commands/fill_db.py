from django.core.management import BaseCommand
from faker import Faker

from app.models import Question, Answer, Tag, Profile, Rate, User

fake = Faker()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("num", type=int)

    def handle(self, *args, **kwargs):
        num = kwargs['num']
        # profiles = [
        #     Profile(
        #         user=User.username,
        #         nickname=fake.name(),
        #         avatar=fake.file_name()
        #     ) for _ in range(num)
        # ]
        # Profile.objects.bulk_create(profiles)
        # profiles = Profile.objects.all()
        # profiles_count = profiles.count()
        # tags = [
        #     Tag(
        #         tag_name=fake.word()
        #     ) for _ in range(num)
        # ] ready
        # Tag.objects.bulk_create(tags)
        # tags = Tag.objects.all()
        # tags_count = tags.count() ready
        # users = [
        #     User(
        #         first_name=fake.first_name(),
        #         last_name=fake.last_name(),
        #         password='12345678910',
        #         username='Miss '+fake.user_name()
        #     ) for _ in range(num)
        # ]
        # User.objects.bulk_create(users)
        # users = User.objects.all()
        # users_count = users.count()
        # users = User.objects.all()
        # profiles = [
        #     Profile(
        #         user=users[i],
        #         nickname=users[i].username,
        #     ) for i in range(1, num+1)
        # ]
        # Profile.objects.bulk_create(profiles)
        # profiles = Profile.objects.all()
        # users_count = profiles.count()

        users = User.objects.all()
        # rates = [
        #     Rate(
        #         author=users[int(j / 200)],
        #     ) for j in range(1950201, num + 1950201)
        # ]
        # Rate.objects.bulk_create(rates)


        answers = [
            Answer(
                title=fake.sentence(nb_words=5),
                content=fake.text(),
                author=users[int(j / 100)],
            ) for j in range(450101, num + 450101)
        ]
        Answer.objects.bulk_create(answers)
        tag_list = Tag.objects.all()
        questions = [
            Question(
                title=fake.sentence(nb_words=7),
                content=fake.text(),
                author=users[int(j / 10)],

            ) for j in range(12, num + 11)
        ]
        Question.objects.bulk_create(questions)

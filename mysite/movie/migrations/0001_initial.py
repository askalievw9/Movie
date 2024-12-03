# Generated by Django 5.1.3 on 2024-11-24 13:29

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=32)),
                ('actor_name_en', models.CharField(max_length=32, null=True)),
                ('actor_name_ru', models.CharField(max_length=32, null=True)),
                ('actor_bio', models.TextField()),
                ('actor_bio_en', models.TextField(null=True)),
                ('actor_bio_ru', models.TextField(null=True)),
                ('actor_age', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(110)])),
                ('actor_image', models.ImageField(upload_to='actor_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=32, unique=True)),
                ('country_name_en', models.CharField(max_length=32, null=True, unique=True)),
                ('country_name_ru', models.CharField(max_length=32, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=32)),
                ('director_name_en', models.CharField(max_length=32, null=True)),
                ('director_name_ru', models.CharField(max_length=32, null=True)),
                ('director_bio', models.TextField()),
                ('director_bio_en', models.TextField(null=True)),
                ('director_bio_ru', models.TextField(null=True)),
                ('director_age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(70)])),
                ('director_image', models.ImageField(upload_to='director_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=32, unique=True)),
                ('genre_name_en', models.CharField(max_length=32, null=True, unique=True)),
                ('genre_name_ru', models.CharField(max_length=32, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(70)])),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('status', models.CharField(choices=[('pro', 'pro'), ('simple', 'simple')], default='simple', max_length=16)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=64)),
                ('movie_name_en', models.CharField(max_length=64, null=True)),
                ('movie_name_ru', models.CharField(max_length=64, null=True)),
                ('year', models.DateField()),
                ('types', multiselectfield.db.fields.MultiSelectField(choices=[('144p', '144p'), ('360p', '360p'), ('480p', '480p'), ('720p', '720p'), ('1080p', '1080p')], max_length=16)),
                ('movie_time', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('movie_trailer', models.FileField(upload_to='movie_trailers/')),
                ('movie_image', models.ImageField(upload_to='movie_images/')),
                ('movie_status', models.CharField(choices=[('pro', 'pro'), ('simple', 'simple')], max_length=16)),
                ('actor', models.ManyToManyField(to='movie.actor')),
                ('country', models.ManyToManyField(to='movie.country')),
                ('director', models.ManyToManyField(to='movie.director')),
                ('genre', models.ManyToManyField(to='movie.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Moments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_moments', models.ImageField(upload_to='movie_moments/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.favorite')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=32)),
                ('video', models.FileField(upload_to='movieLanguages/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('text', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.rating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

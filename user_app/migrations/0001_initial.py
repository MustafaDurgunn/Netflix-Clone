# Generated by Django 4.2.5 on 2023-09-17 16:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetflixUser',
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
                ('tel', models.CharField(blank=True, max_length=50, verbose_name='Telefon Numarası')),
                ('is_premiumUser', models.BooleanField(default=False, verbose_name='Abone mi')),
                ('kidProtect', models.BooleanField(default=False, verbose_name='Ebeveyn Koruması')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
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
            name='MovieCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50, verbose_name='Film Adı')),
                ('movie_description', models.TextField(max_length=350, verbose_name='Açıklama')),
                ('movie_banner', models.ImageField(upload_to='Banners', verbose_name='Banner')),
                ('movie_likes', models.PositiveIntegerField(default=0, verbose_name='Beğeni Sayısı')),
                ('movie_source', models.FileField(upload_to='Movies', verbose_name='Source')),
                ('movie_createdAt', models.DateTimeField(auto_now=True)),
                ('movie_recommended_age', models.PositiveIntegerField(default=15, verbose_name='Yaş Aralığı')),
                ('movie_category', models.ManyToManyField(to='user_app.moviecategory', verbose_name='Kategoriler')),
            ],
        ),
        migrations.CreateModel(
            name='MovieType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Tür')),
            ],
        ),
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickedId', models.CharField(default=user_app.models.generateRandomId, max_length=50, unique=True, verbose_name='Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Hesap')),
            ],
        ),
        migrations.CreateModel(
            name='NetflixProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='static/img/smile-icon.jpg', upload_to='Avatars', verbose_name='Avatar')),
                ('name', models.CharField(max_length=50, verbose_name='Hesap Adı')),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('list', models.ManyToManyField(blank=True, to='user_app.movies', verbose_name='Film/Dizi Listesi')),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='movie_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.movietype', verbose_name='Türü'),
        ),
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim Soyisim')),
                ('cardName', models.CharField(max_length=50, verbose_name='Karttaki Ad/Soyad')),
                ('email', models.CharField(max_length=50, verbose_name='E-mail')),
                ('adress', models.TextField(verbose_name='Adres')),
                ('zip', models.PositiveIntegerField(verbose_name='Zip Kod')),
                ('debitNo', models.PositiveIntegerField(verbose_name='Kredi Kart Numarısı')),
                ('expiredMonth', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2)], verbose_name='Ay')),
                ('expiredYear', models.PositiveIntegerField(verbose_name='Yıl')),
                ('cvv', models.PositiveIntegerField(verbose_name='Güvenlik kod')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kayıtlı')),
            ],
        ),
        migrations.AddField(
            model_name='netflixuser',
            name='profiles',
            field=models.ManyToManyField(to='user_app.netflixprofile', verbose_name='Yan Hesaplar'),
        ),
        migrations.AddField(
            model_name='netflixuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]

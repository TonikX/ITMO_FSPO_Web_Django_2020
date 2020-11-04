from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0005_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
